#Exit loop, Print the letters of a string, if a space found exit the loop
def exit_loop(a):
    for i in a:
        print (i)
        if i == " ":
            print (f"Space found, exiting.. ")
            break
exit_loop(input("Enter a string : "))
