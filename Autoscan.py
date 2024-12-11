#!/bin/bash

url=$1
output_dir=$url-web-scan

# Vytvoření výstupního adresáře
mkdir -p $output_dir
mkdir -p $output_dir/recon

# Nmap skenování portů
echo "[+] Running Nmap scan..."
nmap -p- -T4 -A --script=http-enum -oN $output_dir/recon/nmap_scan_results.txt $url

# Nikto skenování
echo "[+] Running Nikto scan..."
nikto -h http://$url -o $output_dir/recon/nikto_scan_results.txt

# Fuzzing parametrů pomocí Wfuzz
echo "[+] Running Wfuzz..."
wfuzz -c -z file,/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://$url/FUZZ -o $output_dir/recon/wfuzz_results.txt

# Gobuster pro vyhledání skrytých cest
echo "[+] Running Gobuster..."
gobuster dir -u http://$url -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o $output_dir/recon/gobuster_results.txt

echo "[*] Done! 🎉️"
