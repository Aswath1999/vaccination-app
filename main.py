from main_vaccination import vaccinations
from stdiomask import getpass
from Userlogin import userlogin
from Admin import Admin
import os
import time
 
if __name__=="__main__":
    os.system('cls')
    print("*************************WELCOME TO VACCIFICATE*************************")
    print("Download your vaccination certificate")
    Admin_password='123'

    while 1:
        user_detail = int(input("\n1.Register\n\n2.Login\n\n3.Admin\n\n4.Quit\n\nSelect a option: "))
        if user_detail == 1:
            a=userlogin()
            a=a.register()
            if a== False:
                print("Please try again")
            else:
                print('************************************************************************')
                print('************************************************************************')
                print('************************************************************************')
                print("\tVaccination Details has still not been updated \n\tHave Some patience")
                print("\tYour Certificate will be sent through mail")
                print('************************************************************************')
                print('************************************************************************')
                print('************************************************************************')
                time.sleep(5)
                os.system('cls')

        elif user_detail==2:
            a=userlogin()
            username=a.login()
            if username ==False:
                print("Please try again")
                time.sleep(2)
            else:
                option=int(input("1.Do you want to see all your vaccination details\n\n2.Do you want to download your certificate?\n\nSelect an option:"))
                if option==1:
                    info=vaccinations(username)
                    a=info.readinfo()
                    print(a)
                    time.sleep(6)
                    os.system('cls')
                if option==2:
                    certificate=input("Which certificate do you want to download? ")
                    info=vaccinations(username)
                    info.getcertificate(certificate)
                    time.sleep(2)
                    os.system('cls')
            
        elif user_detail==3:
           while 1:
                password=getpass("Enter the admin password: ")
                if password==Admin_password:
                    Option=int(input("1.Enter details of user\n2.Do you want to view any vaccination details for analysis?\n\nSelect an option: "))
                    if Option==1:
                        Name=input("Name: ")
                        Vaccination=input("Vaccination: ")
                        dateofvaccination=input("date of Vaccination: ")
                        QRcode=input(" QRcode: ")
                        dateofbirth=input("date of birth: ")
                        Gender=input("Gender: ")
                        Location=input("Location: ")
                        vaccinemanufacturer=input("Name of vaccine manufacuturer: ")
                        Country=input("Name of Country: ")
                        issuedby=input("Issued by: ")
                        registerdetails=Admin(Name,Vaccination,dateofvaccination,QRcode,Gender,Location,vaccinemanufacturer,Country,issuedby)
                        registerdetails.writeinfo()
                        print("The data has been saved")
                    elif Option==2:
                        vaccine_details=Admin.infoforprofessionals()
                        print(vaccine_details)
                        time.sleep(3)
                        break

                    else:
                        print("Please give a valid number")
                else:
                    print("Wrong password")
        elif user_detail == 4:
            break
        else:
            print("Please enter a Valid Number")
                
    













#Need to create an instance of a class
# a=vaccinations("Dhinakar","Covid","20.10.2020","C1024512")
# a=vaccinations("Aswath","Polio","20.10.2020","C024512","01.01.2000","Male",
# "South east Bayern","BioNTech","Germany","Government of Bayern")

# # # Need to save the details of the user and vaccination in a databaseas
# # # a.writeinfo()

# # """The homepage of the app asks the user to login. After login, the user will get all the details of the 
# # vaccinations. The user can then decide on what vaccine certificate he wants and download it."""
# print(a.readinfo())

# # """After clicking the certificate he wants, the user can then download the certificate. We do not have any 
# # login system here as it is the second step and the user already has logged in to get details on all his/her vaccinations"""
# a.getcertificate()


# """As health professionals, we are more interested in the analyzing the vaccination details. We can get details of how
# many people had taken a particular vaccine and can also be used to administer vacciantions for a particular place.
# The vaccination details of all users are only given after consent from the user. Only certified professionals will have access to the details. """
# # print(a.infoforprofessionals("Polio"))


# """The codes below is a basic program that uses getters and setters.We removed login system for a quicker presentation"""
# a=vaccination("asw",["Covid","Polio","TB"],["19-05-2020","20-05-1999","19-08-2016"])
# print(a.getName())
# a.setName("Aswath")
# print(a.getName())
# print(a.info())

"""The codes can be improved in a lot of ways. It is practically impossible to have a database of all vaccincation details
of all user in a system. The codes should be improved to send api requests to the vaccination websites and collect
details from the website.For example, If a user wants a polio certificate, The user can type the QRcode and 
in the app and the app sends a api request to the official database/website and get the details from there.
 The app should have a cloud function where the users can access the details from any system and 
place.There are a lot of redundant codes in this program and the codes can be reduced in some places. There are many 
repeated nested if statements which can also be reduced. The passwords saved in csv file should be hashed as well.
"""

      


