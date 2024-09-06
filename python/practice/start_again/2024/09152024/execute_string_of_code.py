#   https://www.geeksforgeeks.org/execute-string-code-python/

def Execute(code):
    print (eval(code))

if __name__ == "__main__":
    code = '["a", "b", "c"][1]'
    # code = '"hello" + "world"'
    result = Execute(code)
    # print (result)