#   https://www.geeksforgeeks.org/validate-an-ip-address-using-python-without-using-regex/

import ipaddress
import re

def ValidateIp(ip):
    try:
        ipaddress.IPv4Address(ip)
        print ("Valid IP")
    except ValueError:
        print ("Invalid IP")


def ValidateIp2(ip):
    pattern = r'((255[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        print ("Valid IP2")
    print ("Invalid IP2")


if __name__ == "__main__":
    ip = "192.168.0.1"
    ip1 = "192.168.0.1.5"
    ValidateIp(ip)
    ValidateIp(ip1)
    ValidateIp2(ip)
    ValidateIp2(ip1)