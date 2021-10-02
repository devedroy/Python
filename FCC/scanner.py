

import nmap

scanner = nmap.PortScanner()

print("Welcome, This is a simple Nmap automation tool")
print("<---------------------------------------------->")

ip_addr = input("Please enter a IP address you want to scan: ")
print("The IP address you entered is: ", ip_addr)
type(ip_addr)
