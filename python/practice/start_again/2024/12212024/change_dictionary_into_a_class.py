#   https://www.geeksforgeeks.org/how-to-change-a-dictionary-into-a-class/

class Dict2Class(object):
    def __init__(self,my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
if __name__ == "__main__":
    my_dict = {"Name": "Sar",
                "Age": "30",
                "gender": "unknown"}
    result = Dict2Class(my_dict)
    print ("After converting Dictionary to Class : ")
    print (result.Name, result.Age, result.gender)
    print (type(result))

