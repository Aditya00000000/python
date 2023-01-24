import time
import random


print()
print("HLW I AM A CHAT BOT")
print("YOU CAN CHAT  WITH THE FOLLOWING:")
print()
print("1: hii")
print()
print("2: who are u")
print()
print('3: how to earn 30 lakhs in 30 days')
print()
print("4: what is the time")
print()
print('5: roll a dice')
print()
print("6: clock time plz")
print()
start=input("START/END: ")
while(start.lower()=='start'):
    messages=input("YOU: ")
    if(messages.lower()=="hii"):
        print('BOT: Jai Maharastraa....')
    elif(messages.lower()=="who are u"):
        print('BOT: Mein Baborao Ganpatrao Apte')
    elif(messages.lower()=="how to earn 30 lakhs in 30 days"):
        print('BOT: Are Baba Re Baba Yeh Bahut Kaam Time Nahi Ho Gaya Akhir 30 Saal Ka Time To Dena Chahiye Na!!')
    elif(messages.lower()=="what is the time"):
        print('BOT: Time To Tera Kharap Chal Raha Hai ')
    elif(messages.lower()=='roll a dice'): 
        print(str(random.randint(1,6)))
    elif(messages.lower()=='clock time plz'): 
        ctime=time.strftime("%H:%M:%S")
        print("BOT: ",ctime)
    else:
        print('BOT: Are Kahana Kya Caha Rahe Ho')
        break
        
start=="end"