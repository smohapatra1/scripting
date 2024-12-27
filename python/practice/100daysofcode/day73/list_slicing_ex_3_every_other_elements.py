#List Slicing Exercise 3 (Every Other Element)
#Write a function that accepts a list as input and returns a new list which includes every other element in the original list. Keep the first element, i.e. input_list[0]. For example if:

#input_list = ["we", "love", "python", "so","much"]
#then your function should return a list such as:
#['we', 'python', 'much']

#https://courses.edx.org/courses/course-v1:UTArlingtonX+CSE1309x+1T2018/courseware/805b89dcf6cb49fcb5ab8165c377c378/07f686dcb0b84a0cbce6d7a4f624e8a1/?child=first
def every():
    lists=[]
    list = ["we", "love", "python", "so","much"]
    list_len=len(list)
    lists.append(list[0])
    for i in range(1, list_len):
        if i % 2 == 0:
            lists.append(list[i])
    print (lists)

every()
