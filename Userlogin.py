from stdiomask import getpass
import os
import pandas as pd
import re
clear = lambda: os.system('cls')

class userlogin:

    @staticmethod
    def register(userid,password,username):
        info=pd.DataFrame([[userid,password,username]])
        with open("userinfo.csv","r")as userinfo:
            users=[]
            for i in userinfo:
                user,pas,name=i.split(",")
                users.append(user) 
            
            if userid in users:
               print("Userid already exits.Please try again")
               print("Please register below with a different userid")
               userid=input("Enter userid: ")
               username=input("Enter username:")
               password=input("Enter password:")
               confirmpassword=input("confirm password: ") 
               if re.search(r'[A-Za-z]{5,12}[0-9]*',userid) and re.search(r'[A-Za-z]{5,12}[0-9]*',password) :
                   if password==confirmpassword:              
                        userlogin.register(userid,password,username)
                   else:
                        print("Password doesn't match")
               else:
                   raise SystemExit("The userid and password should contain letters and characters should be greater than 5")

            else:
                if re.search(r'[A-Za-z]{5,12}[0-9]*',userid):
                    info.to_csv("userinfo.csv",mode="a",header=False,index=False) 
                    print("registration successfull")
                else:
                    raise SystemExit("The userid should contain letters and characters should be greater than 5.")
                    
    @staticmethod
    def login(userid,password):
        clear()
        if re.search(r'[A-Za-z]{5,12}[0-9]*',userid)and re.search(r'[A-Za-z]{5,12}[0-9]*',password):
            with open("userinfo.csv","r") as userinfo:
                users=[]
                passwords=[]
                names=[]
                for i in userinfo:
                    user,pas,name=i.split(",")
                    pas=pas.strip()
                    users.append(user)
                    passwords.append(pas)
                    names.append(name)
                data=dict(zip(users,passwords))
                username=dict(zip(users,names))     #Added this to display the name of the user in the homepage


                try:
                    if data[userid]:                   #checks whether user is in database
                        if password==data[userid]:     #checks whether username and password matches
                            print(("Login successfull"))
                            print("Welcome back ",username[userid])   #The name of user is displayed
                        else:
                            raise SystemExit("Incorrect Username/Password")
                except:
                    raise SystemExit("Username doesn't exist")
        else:
            raise SystemExit("Userid/password should atleast have 5 characters and should include letters.Please try again")
                    
