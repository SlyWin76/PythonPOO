from scapy.all import IP, TCP, UDP, DNSQR, DNS
from scapy.all import *

def syn_scan(target_ip, port_range):

    for port in port_range:

        response = sr1(IP(dst=target_ip) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

        if response is None:
            print(f"{target_ip} : {port} is open.")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags & 0x02 == 0x02:
                print(f"{target_ip} : {port} is open.")
            else:
                print(f"{target_ip} : {port} is closed.")


def dns_scan(target_ip):

    response = sr1(IP(dst=target_ip) / UDP(dport=53) / DNSQR(qname="google.com"), timeout=1, verbose=0)

    if response is None:
        print(f"{target_ip} is not a DNS server.")
    elif response.haslayer(DNS):
        if response.getlayer(DNS).ancount > 0:
            print(f"{target_ip} is a DNS server.")


target_ip = "8.8.8.8"

syn_scan(target_ip, [80, 443, 53, 25, 110])
dns_scan(target_ip)