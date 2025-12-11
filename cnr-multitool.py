import argparse
import sys
import subprocess


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

# ----------------------------------------------
# SUBCOMMAND 3: EXEC
# ----------------------------------------------

exec_parser = subparsers.add_parser("exec", help="Execute a system command")
exec_parser.add_argument("--cmd", required=True, help="System command to execute")

# ----------------------------------------------

args = parser.parse_args()

# if no subcommand provided, show help and exit
if not args.command:
    parser.print_help()
    sys.exit(1)



# ----------------------------------------------
# === COMMAND HANDLERS ===
# ----------------------------------------------



if args.command == "scan":
    print(f"[SCAN MODE] Target: {args.target}, Ports: {args.ports}")


elif args.command == "brute":
    print(f"[BRUTE MODE] URL: {args.url}")
    if args.single:
        print(f"Single: {args.single}")
    elif args.wordlist:
        print(f"Wordlist: {args.wordlist}")

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