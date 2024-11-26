import argparse
from includes import act
from units import banner,network

parser = argparse.ArgumentParser(description="Subdomain Finder and IP Resolver")
parser.add_argument("-d", "--domain", required=True, help="Target domain to scan (e.g., example.com)")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads to use (default: 10)")
args = parser.parse_args()

def choose_wordlist():
    wordlists = {
        1: ("wordlist.txt", "Level 1"),
        2: ("wordlist1.txt", "Level 2"),
        3: ("wordlist2.txt", "Level 3")
    }

    print("\nAvailable Wordlist Files:")
    for key, (filename, level) in wordlists.items():
        print(f"{key}: {filename} ({level} wordlist)")

    while True:
        try:
            choice = int(input("\nChoose a wordlist (1/2/3): "))
            if choice in wordlists:
                selected_wordlist, level = wordlists[choice]
                try:
                    with open(selected_wordlist, 'r') as f:
                        print(f"\n[+] Selected wordlist: {selected_wordlist} ({level} wordlist)")
                        return selected_wordlist  
                except FileNotFoundError:
                    print(f"[!] File '{selected_wordlist}' does not exist. Please check the file.")
            else:
                print("[!] Invalid choice. Please choose a valid option.")
        except ValueError:
            print("[!] Invalid input. Please enter a number (1/2/3).")


def main():
    banner.banner()
    selected_wordlist = choose_wordlist()
    act.find_subdomains_and_ips(args.domain, selected_wordlist, args.threads)
            

if __name__ == "__main__":
    if network.net():
        main()
    else:
        print("\ncheck internet")
