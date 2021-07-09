from stdiomask import getpass
import os
import pandas as pd
import re
from Userlogin import userlogin
clear = lambda: os.system('cls')


class vaccinations: 

    def __init__(self,Name,Vaccination,dateofvaccination,QRcode):         
        self.__Name=Name
        self.__vaccination=Vaccination
        self.__vaccinationdate=dateofvaccination
        self.__code=QRcode
    
    def writeinfo(self):       #saves the instance from __init__ constructor in a cvv file 
        info=pd.DataFrame([[self.__Name,self.__vaccination,self.__vaccinationdate,self.__code]])
        info.to_csv("Vaccination.csv",mode="a",header=False,index=False)
    
    def readinfo(self):       #reads the csv file and outputs the vaccination details of a particular user.
        clear()
        print("Vaccificate ")
        print("---------------\n")
        print("1.Register \n2.Login")
        option=int(input("\nPlease enter an option: "))
        if option==1:
            userid=input("enter your userid/emailaddress: ")
            username=input("Enter a username: ")
            password=getpass("Enter your password: ")
            confirmpassword=getpass("Confirm your password: ")
            if password==confirmpassword:
                userlogin.register(userid,password,username)
            else:
                return("password doesn't match")
        elif option==2:
            userid=input("enter your userid/emailaddress: ")
            password=getpass("Enter your password: ")
            userlogin.login(userid,password)
            with open("userinfo.csv","r") as userinfo:
                users=[]
                names=[]
                for i in userinfo:
                    user,pas,name=i.split(",")
                    users.append(user)
                    name=name.strip()
                    names.append(name)
                    username=dict(zip(users,names))
                if username[userid]==self.__Name:
                    info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
                    return(info[info['Name']==self.__Name].drop_duplicates(subset=['QR code'],keep='last').reset_index(drop=True))
                else:
                    return "Your details haven't been updated yet.We will contact you in email as soon as possible"
        else:
            return "Please give a valid number"
            
        

    def updateinfo(self,Oldinfo,newinfo):  #to change the value.Changes all values in the database
        self.__oldinfo=Oldinfo
        self.__newinfo=newinfo
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
        info=info.replace(Oldinfo,newinfo)
        return info


    def infoforprofessionals(self,vaccination="Polio"):    #displays details of all users for a particular vaccination 
        self.vaccination=vaccination
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"]).drop_duplicates(keep='last')
        return info[info["Vaccination"]==vaccination].reset_index(drop=True)

    def getcertificate(self):  
        clear()
        print("Vaccination certificate")
        print("------------------------")
        print (f'Name: {self.__Name}\nVaccination:{self.__vaccination}\nManufacturer:  \nQR code:{self.__code}')
                
      
