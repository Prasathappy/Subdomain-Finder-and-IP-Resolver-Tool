import dns.resolver
import argparse
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(domain, subdomain):
    full_domain = f"{subdomain}.{domain}"
    try:
        dns.resolver.resolve(full_domain, 'A')
        print(f"[+] Found: {full_domain}")
        return full_domain
    except dns.resolver.NXDOMAIN:
        pass  
    except dns.exception.Timeout:
        print(f"[-] Timeout on {full_domain}")
    except Exception as e:
        print(f"[!] Error on {full_domain}: {e}")
    return None

def get_ip_address(subdomain):
    try:
        answers = dns.resolver.resolve(subdomain, 'A')
        ips = [answer.to_text() for answer in answers]
        return ips
    except dns.resolver.NXDOMAIN:
        print(f"[!] {subdomain} does not exist.")
    except dns.resolver.Timeout:
        print(f"[!] Timeout resolving {subdomain}.")
    except Exception as e:
        print(f"[!] Error resolving {subdomain}: {e}")
    return None

def find_subdomains_and_ips(domain, wordlist, threads):
    print(f"Starting subdomain scan for: {domain}")
    found_subdomains = {}
    with open(wordlist, 'r') as file:
        subdomains = [line.strip() for line in file]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda sub: check_subdomain(domain, sub), subdomains)

    for result in results:
        if result:
            ips = get_ip_address(result)
            if ips:
                found_subdomains[result] = ips
                print(f"[+] {result} -> {', '.join(ips)}")

    if found_subdomains:
        with open("subdomains_with_ips.txt", "w") as outfile:
            for subdomain, ips in found_subdomains.items():
                outfile.write(f"{subdomain}: {', '.join(ips)}\n")
        print("\n[+] Results saved to 'subdomains_with_ips.txt'.")
    else:
        print("\n[!] No subdomains found.")
