#Alarm Clock - A simple clock where it plays a sound 
#after X number of minutes/seconds or 
#at a particular time.

from datetime import datetime
import pyglet
import time

def sound(h,m):
    print ("Time is : " + h+":"+m)
    time=h+":"+m
    print (time)
    curr_time = datetime.now().time()
    date = datetime.now().date()
    print ("Date is %s and Time is %s" %(date, curr_time))
    try:
        if time == "10:00":
            print ("Time matches, playing a sound")
            #song = pyglet.media.load('bin/sound.wav')
            song = pyglet.media.load('/Users/smohapatra/Downloads/invalid_keypress.mp3')
            song.play() # play the sound
            pyglet.app.run()
        else:
            print ("Enter new time: ")
    except:
        ValueError


def main():
    h=input("Enter an hour: ")
    m=input("Enter minutes: ")
    sound(h,m)


if __name__ == "__main__":
    main()