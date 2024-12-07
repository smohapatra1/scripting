#   https://www.geeksforgeeks.org/python-program-to-find-the-type-of-ip-address-using-regex/

#   Given an IP address as input, write a Python program to find the type of IP address i.e. either IPv4 or IPv6. If the given is neither of them then print neither.

# Solution - 01 

# import ipaddress
# def ValidateIp(n):
#     try:
#         ipaddress.IPv4Address(n)
#         return "IPV4"
#     except ValueError:
#         try:
#             ipaddress.IPv6Address(n)
#             return "IPV6"
#         except ValueError:
#             return 'NEITHER'

# Solution - 02 

import re 

def ValidateIp(n):
    # Make a regular expression 
    # for validating an Ipv4
    ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    
    # Make a regular expression 
    # for validating an Ipv6
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
    if re.search(ipv4, n):
        return "IPV4"
    elif re.search(ipv6, n):
        return "IPV6"
    else:
        return "NEITHER"

if __name__ == "__main__":
    n = input("Enter ip address : ")
    print (ValidateIp(n))
