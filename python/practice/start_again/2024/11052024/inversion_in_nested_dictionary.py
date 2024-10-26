#   https://www.geeksforgeeks.org/python-inversion-in-nested-dictionary/

def Inversion(test_dict):
    stack = [(test_dict, None)]
    inverted_dict = {}
    while stack:
        d, parent_key = stack.pop()
        for k, v in d.items():
            if parent_key is not None:
                inverted_dict.setdefault(k, {}).update({parent_key: {}})
            if isinstance(v, dict):
                stack.append((v, k ))
    return inverted_dict

if __name__ == "__main__":
    test_dict = {"a": {"b": {}}, "d": {"e": {}}, "f": {"g": {}}}
    print ("Results after inversion : ", Inversion(test_dict))