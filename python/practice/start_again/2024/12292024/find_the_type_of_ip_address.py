#   https://www.geeksforgeeks.org/python-program-to-find-the-type-of-ip-address-using-regex/

import ipaddress
import re

def TypeIp(ip):
    try:
        ipaddress.IPv4Address(ip)
        print ("IPV4")
    except ValueError:
        try:
            ipaddress.IPv4Address(ip)
            print ("IPV4")
        except ValueError:
            try: 
                ipaddress.IPv6Address(ip)
                print ("IPV6")
            except ValueError:
                print ("NEITHER")


def TypeIp2(ip):
    ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    ipv6 = '''(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|
        ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:)
        {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1
        ,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}
        :){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{
        1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA
        -F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a
        -fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0
        -9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,
        4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}
        :){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9
        ])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0
        -9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]
        |1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]
        |1{0,1}[0-9]){0,1}[0-9]))'''
    if re.search(ipv4, ip):
        print ("IPV4")
    elif re.search(ipv6, ip):
        print ("IPV6")
    else:
        print ("NEITHER")


if __name__ == "__main__":
    ip = "10.20.30.30"
    ip1 = "11:22:33:44:11:22:22"
    ip3 = "3001:0da8:75a3:0000:0000:8a2e:0370:7334"
    TypeIp(ip)
    TypeIp(ip1)
    TypeIp(ip3)
    TypeIp2(ip)
    TypeIp2(ip1)
    TypeIp2(ip3)