#   https://www.geeksforgeeks.org/validate-an-ip-address-using-python-without-using-regex/


def ValidateIp(ip):
    if ip.count('.') != 3:
        print ("Invalid IP")
    l = list(map(str, ip.split('.')))
    for ele in i:
        if int(ele) < 0 or int(ele) > 255 or (ele[0] == '0' and len(ele) != 1):
            print ("Invalid Ip addresses")
    print ("Valid Ip addresses")

if __name__ == "__main__":
    ip = "192.168.24.1"
    ip1 = "192.168.2.1.1"
    ValidateIp(ip)
    ValidateIp(ip1)