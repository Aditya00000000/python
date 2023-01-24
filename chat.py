import time 
import random
from AppOpener import open
import pywhatkit as kit

print()
print("HLW I AM A CHAT BOT")
print()


def help():
    print("YOU CAN CHAT WITH THE FOLLOWING:")
    print()
    print("1: hii")
    print()
    print("2: what are you")
    print()
    print('3: How are you')
    print()
    print("4: what is the time")
    print()
    print('5: roll a dice')
    print()
    print("6: open application")
    print()
    print('7: play song')
    print()
    print('8: google search')

print()
print('TYPE START TO START THE BOT OR END FOR THE BOT TO STOP')
print()
start=input('START/END: ')
print()
print("To see the commands list you can type HELP ")

def search():
    search=input("BOT: What do you want to search: ")
    kit.search(search)
    print('BOT: SEARCHING',search)

def yt():
    sname=input('BOT: Enter song name: ')
    kit.playonyt(sname)
    print('BOT: NOW PLAYING',sname)

def app():
    nm=input("BOT:  APP NAME: ")
    open(nm.lower(),match_closest=True)
    print('BOT: ',nm,' OPENED')

def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1


def decide(start):
    if(start=='start'):
        countdown(3)
        print()    
        print('BOT: WELCOME..')
        print()
    elif(start=='end'):
        countdown(3)
        print()
        print("BOT: SIGNING OUT...")
        
        
if(start.lower()=='end'):
    decide("end")
else:    
    decide("start")
    while(start.lower()=='start'):
        msg=input('YOU: ')
        if(msg.lower()=='hii' or msg == '1'):
            print("BOT: Hey There..")
        elif(msg.lower()=='help'):
            help()
        elif(msg.lower()=='what are you' or msg == '2'):
            print('BOT: I am a Narrow AI who can do a limited no. of tasks.')
        elif(msg.lower()=='how are you' or msg=='3'):
            print("BOT: I am perfectly fine and hope u too")
        elif(msg.lower()=='what is the time'or msg == '4'):
            ctime=time.strftime("%H:%M:%S")
            print("BOT: ",ctime)
        elif(msg.lower()=='roll a dice'or msg == '5'):
            print("BOT: ",str(random.randint(1,6)))
        elif(msg.lower()=='open application' or msg == '6'):
            app()
        elif(msg.lower()=='play song'or msg=='7'):
            yt()
        elif(msg.lower()=='google search'or msg=='8'):
            search()
        elif(msg.lower()=='end'):
            print('BOT: Bye Bye....')
            break
        else:
            print('BOT: sorry didn\'t get it....')
    decide('end')
    print()


