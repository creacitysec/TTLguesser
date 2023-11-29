import subprocess
import re
import platform
import argparse

def ping_ip(ip):
    # Détermine la syntaxe de la commande ping selon le système d'exploitation
    ping_command = ["ping", "-n", "1", ip] if platform.system() == "Windows" else ["ping", "-c", "1", ip]

    try:
        # Exécute la commande ping
        output = subprocess.check_output(ping_command, stderr=subprocess.STDOUT, universal_newlines=True)

        # Recherche la valeur TTL dans la sortie
        ttl_pattern = r'TTL=(\d+)' if platform.system() == "Windows" else r'ttl=(\d+)'
        match = re.search(ttl_pattern, output, re.IGNORECASE)
        if match:
            ttl = int(match.group(1))

            # Devine le système d'exploitation basé sur la valeur TTL
            os_guess = "Probably Linux/Unix" if ttl <= 64 else "Probably Windows"
            return f"TTL: {ttl}\n{os_guess}"
        else:
            return "TTL not found in ping response"
    except subprocess.CalledProcessError:
        return "Ping failed"

def process_ips(ip_list):
    results = {}
    for ip in ip_list:
        results[ip] = ping_ip(ip)
    return results

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Configuration de l'analyse des arguments de ligne de commande
parser = argparse.ArgumentParser(description="OS Guessing based on Ping TTL")
parser.add_argument("-i", "--ip", help="IP address to ping")
parser.add_argument("-l", "--list", help="File containing list of IP addresses, one per line")

args = parser.parse_args()

if args.ip:
    ips = [args.ip]
elif args.list:
    ips = read_ips_from_file(args.list)
else:
    print("No IP address or list file provided.")
    parser.print_help()
    exit(1)

results = process_ips(ips)
for ip, result in results.items():
    print(f"{ip}: {result}")
