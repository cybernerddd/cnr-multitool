import argparse
import sys
import subprocess
import requests


parser = argparse.ArgumentParser(description="===  Cybernnerddd Multi-Tool   ====")

subparsers = parser.add_subparsers(dest="command", help="Available commands")

# ----------------------------------------------
# SUBCOMMAND 1: SCAN
# ----------------------------------------------


scan_parser = subparsers.add_parser("scan", help="Perform a port scan")

# required_scan = scan_parser.add_argument_group("required arguments") # Create a group for required arguments
# group = required_scan.add_mutually_exclusive_group(required=True) # Meaning the user can choose one, but never both.

scan_parser.add_argument("target", help="Target IP address or domain")


scan_parser.add_argument(
    "--ports",
    type=int,
    nargs="+",
    default=[80, 443],
    help="List of ports to scan (default: 80, 443)",
)

# ----------------------------------------------

# ----------------------------------------------
# SUBCOMMAND 2: BRUTE
# ----------------------------------------------

brute_parser = subparsers.add_parser("brute", help="Bruteforce directories")

required = brute_parser.add_argument_group("required arguments") # Create a group for required arguments
group = required.add_mutually_exclusive_group(required=True) # Meaning the user can choose one, but never both.

group.add_argument(
    "--single",
    help="Single directory name to brute force",
)


group.add_argument(
    "--wordlist",
    help="Wordlist file for brute forcing",
)

brute_parser.add_argument("url", help="Target URL for bruteforcing")
brute_parser.add_argument(
    "--username",
    help="Username for authentication",
    required=True
)
brute_parser.add_argument(
    "--password",
    help="Password for authentication",
    required=True
)

brute_parser.add_argument(
    "--login-url",
    help="Login URL for authentication",
    required=True
)










# ----------------------------------------------
# SUBCOMMAND 3: EXEC
# ----------------------------------------------

exec_parser = subparsers.add_parser("exec", help="Execute a system command")
exec_parser.add_argument("--cmd", required=True, help="System command to execute")



args = parser.parse_args()

# if no subcommand provided, show help and exit
if not args.command:
    parser.print_help()
    sys.exit(1)

# ----------------------------------------------
# === COMMAND HANDLERS ===
# ---------------------------------1-------------


if args.command == "scan":
    print(f"[SCAN MODE] Target: {args.target}, Ports: {args.ports}")


elif args.command == "brute":
    print(f"\n===== [BRUTE MODE] Target URL: {args.url} =========")

    session = requests.Session()

    # -------------------------------
    # AUTHENTICATION
    # -------------------------------
    login_data = {
        "username": args.username,
        "password": args.password
    }

    try:
        response = session.post(args.login_url, data=login_data, verify=False, allow_redirects=True)
    except Exception as e:
        print(f"[-] Login request failed: {e}")
        sys.exit(1)

    keywords = ["logout", "dashboard", "welcome", "sign out"]

    if response.status_code in [200, 302, 301]:
        if any(k in response.text.lower() for k in keywords) or session.cookies:
            print("[+] Authentication successful")
        else:
            print("[-] Authentication failed (no indicators)")
            sys.exit(1)
    else:
        print(f"[-] Login failed (status {response.status_code})")
        sys.exit(1)

    # -------------------------------
    # LOAD DIRECTORIES
    # -------------------------------
    if args.wordlist:
        try:
            with open(args.wordlist, "r") as f:
                dirs = f.read().splitlines()
        except FileNotFoundError:
            print(f"[-] Wordlist not found: {args.wordlist}")
            sys.exit(1)
    else:
        dirs = [args.single]

    print("[*] Establishing baseline...")
    fake_url = f"{args.url}/this_should_not_exist_123"
    baseline = session.get(fake_url, verify=False)
    baseline_len = len(baseline.content)
    baseline_code = baseline.status_code

    print("[*] Starting directory bruteforce...\n")

    for directory in dirs:
        target = f"{args.url}/{directory}"
        res = session.get(target, verify=False)

        if res.status_code == 200 and len(res.content) != baseline_len:
            print(f"[+] FOUND: {target} (200 | len diff)")
        elif res.status_code in [301, 302, 307, 308]:
            print(f"[+] REDIRECT: {target} ({res.status_code})")



elif args.command == "exec":
    print(f"\n===== [EXEC MODE] Command: \"{args.cmd}\"  =========")
    try:
        result = subprocess.run(args.cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print("\nCommand Output:")
            print(result.stdout if result.stdout else "NO OUTPUT")
        
        if result.stderr:
            print("Error found:", result.stderr)
        
    except Exception as e:
        print(f"An error occurred while executing the command: {e}")
else:
    parser.print_help()
