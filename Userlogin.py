from stdiomask import getpass
import os

class userlogin:
    def clear():
        return os.system('cls')

    def main():
        userlogin.clear()
        print("WELCOME")
        print("---------")
        print("\n1- REGISTER")
        print("\n2- LOGIN")
        useroption= int(input("\nChoose an option:"))
        if useroption==1:
            userlogin.Register()
        elif useroption==2:
            userlogin.login()
        else:
            print ("Please give a correct number")

    def Register():
        userlogin.clear()
        print("Register")
        print("--------")
        username = input("Please enter Username/emailid: ")
        password = getpass("Please enter Password: ")
        confirmpassword=getpass("Please confirm your password: ")
        with open ("userInfo.txt","r") as info:
            users=[]
            passwords=[]
            for i in info:
                user,pas=i.split(",")
                pas=pas.strip() 
                users.append(user)
                passwords.append(pas)
            if  not username==None:
                if username in users:
                    print("Username exits")
                    userlogin.Register()
                else:
                    if password==confirmpassword:
                       with open ("userInfo.txt","a") as info:
                                info.write(username+","+password+"\n")
                                print("User created successfully")
                                print("you can now log in")
                    else:
                        print("Passwords doesn't match. Please register again")
                        userlogin.Register()
                        
        
    def login():
        username = input("Please enter your username: ")
        password = getpass("Please enter your password: ")  
        if len(username and password)>1:
            with open ("userInfo.txt","r") as info:
                users=[]
                passwords=[]
                for i in info:
                    user,pas=i.split(",")
                    pas=pas.strip()
                    users.append(user)
                    passwords.append(pas)
                data=dict(zip(users,passwords))

                try:
                    if data[username]:
                        try:
                            if password==data[username]:
                               print("Login successfull")
                               print("Welcome back ",username)
                            else:
                                print("Incorrect password")
                        except:
                            print("Incorrect password")
                    else:
                        print("Incorrect passsword")
                except:
                    print("Username or password doesn't exist")
        else:
            print("Error in login.Please try again")
            userlogin.login()


print(userlogin.main())
