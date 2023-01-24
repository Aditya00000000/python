from datetime import datetime 
import random
def responses(messages)-> str:
    if(messages.lower()=="hii"):
        return 'Namaste'
    elif(messages.lower()=="who are u"):
        return 'Mein Baborao Ganpatrao Apte'
    elif(messages.lower()=="how to earn 30 lakhs in 30 days?"):
        return 'ARE BABA RE BABA YEH BAHUT KAAM TIME NAHI HO GAYA AKHIR 30 SAAL KA TIME TO DENA CHAHIYE NA!!'
    elif(messages.lower()=="what is the time now"):
        return 'Time to tera kharap chal raha hai '
    elif(messages.lower()=='roll a dice '): 
        return str(random.randint(1,6))
    elif(messages.lower()==''): 
        return 'Rakh teri maa ki rakh'
    else:
        return 'kahana kya caha rahe ho yaar'