#   https://www.geeksforgeeks.org/python/spam-bot-using-pyautogui/
import pyautogui, time, datetime
time.sleep(1)
while True:
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Drink Water!")
    pyautogui.press("enter")
    time.sleep(3)
    print(datetime.datetime.now())
    pyautogui.typewrite("Reminder: Take Medicine")
    pyautogui.press("enter")
    time.sleep(30)
