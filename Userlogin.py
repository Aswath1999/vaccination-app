from stdiomask import getpass
import os
import pandas as pd
import re
import time

class userlogin:


    def register(self):
        while 1:
            userid=input("Enter userid/email address: ")
            username=input("Enter username:")
            password=getpass("Enter password:")
            confirmpassword=getpass("confirm password: ") 
            info=pd.DataFrame([[userid,password,username]])
            if password==confirmpassword:
                if re.search(r'[A-Za-z].{4,}[0-9]*',userid) and re.search(r'[A-Za-z].{4,}[0-9]*',password):
                    if os.path.exists('userinfo.csv'):
                        with open("userinfo.csv","r")as userinfo:
                            users=[]
                            for i in userinfo:
                                user,pas,name=i.split(",")
                                users.append(user) 
            
                        if userid in users:
                            print("Userid already exits.Please try again")
                            print("Please register below with a different userid")
                            a=userlogin()
                            a=a.register()
                        else:
                            info.to_csv("userinfo.csv",mode="a",header=False,index=False)       #Make sure the csv file is present. use w when writing first time
                            print("registration successfull")
                            time.sleep(1)
                            break
                    else:
                        info.to_csv('userinfo.csv',index=False)
                        print("registration successfull!!You can now log in")
                        time.sleep(1)
                        os.system('cls')
                        break
                else:
                    print("The userid should contain atleast 5 letters.")   
                    return False          
            else:
                print("Password doesn't match")
                return False
                

              
    def login(self):
        os.system('cls')
        userid=input("Enter userid/emailaddress: ")
        password=getpass("Enter Password: ")
        if re.search(r'[A-Za-z].{4,}[0-9]*',userid)and re.search(r'[A-Za-z].{4,}[0-9]*',password):
            with open("userinfo.csv","r") as userinfo:
                users=[]
                passwords=[]
                names=[]
                for i in userinfo:
                    user,pas,name=i.split(",")
                    name=name.strip()
                    users.append(user)
                    passwords.append(pas)
                    names.append(name)
                data=dict(zip(users,passwords))
                username=dict(zip(users,names))     #Added this to display the name of the user in the homepage
                try:
                    if data[userid]:                   #checks whether user is in database
                        if password==data[userid]: 
                            os.system('cls')   
                            print(("Login successfull"))
                            print("Welcome back",username[userid])
                            return username[userid]
                        else:
                            print("Incorrect Username/Password")
                            return False
                except:
                    print("Username doesn't exist")
                    return False
        else:
            print("Userid/password should atleast have 4 characters and should include letters.")
            return False
                    
 
            
        


        