#   https://www.geeksforgeeks.org/how-to-keep-a-python-script-output-window-open/

try:
    print ("Hello World")
    raise KeyboardInterrupt
except KeyboardInterrupt:
    input("Press Enter to Exit: ")
