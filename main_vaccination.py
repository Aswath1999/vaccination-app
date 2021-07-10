from stdiomask import getpass
import os
import pandas as pd
import re
from Userlogin import userlogin
clear = lambda: os.system('cls')


class vaccinations: 

    def __init__(self,Name,Vaccination,dateofvaccination,QRcode,dateofbirth,Gender,Location,vaccinemanufacturer,country,issuedby):
        self.__Name=Name
        self.__vaccination=Vaccination
        self.__vaccinationdate=dateofvaccination
        self.__code=QRcode
        self.__dateofbirth=dateofbirth
        self.__Gender=Gender
        self.__Loction=Location
        self.__vaccinemanufacturer=vaccinemanufacturer
        self.__country=country
        self.__issuedby=issuedby
    def writeinfo(self):       #saves the instance from __init__ constructor in a cvv file 
        info=pd.DataFrame([[self.__Name,self.__vaccination,self.__vaccinationdate,self.__code,self.__dateofbirth,self.__Gender,self.__Loction,self.__vaccinemanufacturer,self.__country,self.__issuedby]])
        info.to_csv("Vaccination.csv",mode="a",header=False,index=False)
    
    def readinfo(self):       #reads the csv file and outputs the vaccination details of a particular user.
        clear()
        col_names=["Name","Vaccination","Date","QR code","dateofbith","Gender","Location","vaccinemanufacturer","country","issuedby"]
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
                raise SystemExit("You can now login")
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
                    info=pd.read_csv('Vaccination.csv',names=col_names)
                    return(info[info['Name']==self.__Name].drop_duplicates(subset=['QR code'],keep='last').reset_index(drop=True))
                else:
                    return "Your details haven't been updated yet.We will contact you in email as soon as possible"
        else:
            return "Please give a valid number"


    def infoforprofessionals(self,vaccination="Polio"): 
        clear()   #displays details of all users for a particular vaccination 
        self.vaccination=vaccination
        col_names=["Name","Vaccination","Date","QR code","dateofbith","Gender","Location","vaccinemanufacturer","country","issuedby"]
        info=pd.read_csv('Vaccination.csv',names=col_names).drop_duplicates(keep='last')
        return info[info["Vaccination"]==vaccination].reset_index(drop=True)

    def getcertificate(self):  
        clear()
        details=["Name: "+self.__Name,"\nVaccination:"+self.__vaccination,"\nQR code: "+self.__code,"\nDateofbirth:"+self.__dateofbirth,
            "\nGender: "+self.__Gender,"\nLocation: "+self.__Loction,"\nManufacturer: "+self.__vaccinemanufacturer,"\ncountry: "+self.__country,
            "\nissued by: "+self.__issuedby]
        with open('certificate.txt','w') as certificate:
            certificate.write("Vaccination certificate\n")
            certificate.write("-------------------------\n")
            certificate.writelines(details)
            certificate.close()
        with open("certificate.txt","r") as certificate:
            print(certificate.read())
            print(certificate.readlines())
            certificate.close()
       
                