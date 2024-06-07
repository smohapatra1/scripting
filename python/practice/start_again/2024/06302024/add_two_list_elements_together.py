# Add two lists elements together

def add_list(n, m ):
    res_list = []
    for i in range(0, len(n)):
        res_list.append(n[i] + m[i])
    print (res_list)

if __name__ == "__main__":
    n = [1, 2, 3]
    m = [4, 5, 6]
    res = add_list(n,m)