import requests
import sys
import argparse

# logs into a web app

parser = argparse.ArgumentParser(description="AUTH DIR BRUTEFORCER")

parser.add_argument(
    "--login-url", 
    help="URL to login account",
    required=True
)

parser.add_argument(
    "--target-url",
    help="Target URL to brute force",
    required=True
)

parser.add_argument(
    "--username",
    help="Username to login Account",
    required=True
)

parser.add_argument(
    "--password",
    help="Password to login",
    required=True
)

parser.add_argument(
    "--wordlist",
    help="Wordlist of DIR to bruteforce"
)

# parse arguments
args = parser.parse_args()

# ----------------------------------------------
# === AUTHENTICATION LOGIC ===
# ----------------------------------------------

session = requests.Session()
login_data = {
    "username": args.username,
    "password": args.password
}

response = session.post(
    args.login_url,
    data=login_data,
    verify=False
)

print("\n=========================================")
print("=== YOUR MULTITOOL AUTH DIR BRUTEFORCER ===")
print("=========================================\n")

# Check if login was successful with keywords and status code and response lengthS

keywords = ["logout", "welcome", "dashboard", "hello", "sign out"]

if response.status_code == 200:
    if any(keyword in response.text.lower() for keyword in keywords):
        print("[+] Login successful! (Keyword found)")
    else:
        print("[-] Login failed: Keywords not found")
        sys.exit(1)

elif response.status_code == 302 or response.status_code == 301:
    print("[+] Login successful! (Redirected)")
else:
    print(f"[-] Login failed: Status code {response.status_code}")
    sys.exit(1)


#Bruteforce Logic
if args.wordlist:
    try:
        with open(args.wordlist, 'r') as f:
            dirs = f.read().splitlines()
    except FileNotFoundError:
        print(f"[-] WOrdlist file not found: {args.wordlist}")
        sys.exit(1)
    print("[*] Starting directory bruteforce...")
  
  
    for dir in dirs:
         url = f"{args.target_url}/{dir}"
         res = session.get(url, verify=False)
         # Check for valid responses

         fake_url = f"{args.target_url}/this_should_not_exist_123"
         baseline = session.get(fake_url, verify=False)

         baseline_len = len(baseline.content)
         baseline_code = baseline.status_code

         if res.status_code == 200 and len(res.content) != baseline_len:
             print(f"[+] Found valid directory: {url} (Status: {res.status_code})")
        
         elif res.status_code in [301, 302, 303, 307, 308]:
             print(f"[+] Found Redirect: {url} (Status: {res.status_code})")
