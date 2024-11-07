#   https://www.geeksforgeeks.org/python-convert-a-set-into-dictionary/

def set_to_dict(s):
    keys = list(s)
    values = [0] * len(s)
    return {k: v for k, v in zip(keys, values)}
if __name__ == "__main__":
    s = {1, 2, 3, 4, 5}
    print ("After converting sets into Dictionary : ", set_to_dict(s))