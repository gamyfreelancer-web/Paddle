
list_users=[]    
import os
import time

def clear():
    os.system( "cls" if os.name=="nt" else "clear")


class Users:
    
    def __init__(self,first_name,last_name,email,password,state):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.state=state
        
        
        
        
    def Didplay_users (self):
        
        print(f" the first name : {self.first_name}") 
        print(f" the last name : {self.last_name}") 
        print(f" your email is {self.email}") 
        print(f" your password is : {self.password}")
        print(f' your state  is : {self.state}')
     
    


def add():
    name=input(" enter the first name: ")
    last_name=input(" enter the last name: ")
    email=input(" enter the your email : ")
    password=input(" enter the first name: ")
    return Users(name,last_name,email,password,state="inactive")



while True:
    print(""" 
          *****wellcom to massege********
          1- add user
          2-display all users
          3- exit
          """)
    choice=input(" enter your choice : ")  
    if choice=="1":
        list_users.append(add())
        time.sleep(2)
        print(" sucssfuly add new user....")
        
    elif choice=="2":
        if list_users:
            clear()
            time.sleep(2)
            for _ in list_users:
                _.Didplay_users ()
        else:
            print(" there is not user")  
            time.sleep(2)
            clear()      
    
    elif choice=="3":    
        do=input(" do you want to exit (y/n): ")
        if do=="y":
            print(" thanks for you to use the app ")
            break
    else:
        print(" this choise not found")
        time.sleep(2)
        clear()