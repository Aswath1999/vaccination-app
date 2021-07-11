from main_vaccination import vaccinations
from stdiomask import getpass
from Userlogin import userlogin
from Admin import Admin
from Generaldetails import vaccinationdetails
from Generaldetails import Appinfo
import os   
import time
 
if __name__=="__main__":
    os.system('cls')
    print("*************************WELCOME TO VACCIFICATE*************************")
    print("Download your vaccination certificate")
    Admin_password='123'

    while 1:
        user_detail = int(input("\n1.Register\n\n2.Login\n\n3.Admin\n\n4.Vaccine Information\n\n5.About us\n\n6.Quit\n\nSelect a option: "))
        if user_detail == 1:
            os.system('cls')
            a=userlogin()
            a=a.register()
            time.sleep(1)
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
                print("Your Vaccination details")
                info=vaccinations(username)
                a=info.readinfo()
                print(a)
                certificate=input("\n\nWhich certificate do you want to download? ")
                info=vaccinations(username)
                info.getcertificate(certificate)
                time.sleep(2)
                os.system('cls')
        elif user_detail==3:
                os.system('cls')
                password=getpass("Enter the admin password: ")
                while 1:
                    if password==Admin_password:
                        Option=int(input("1.Enter details of user\n\n2.Do you want to view any vaccination details for analysis?\n\nSelect an option: "))
                        if Option==1:
                            Name=input("Name: ")
                            Vaccination=input("Vaccination: ")
                            dateofvaccination=input("Date of Vaccination: ")
                            QRcode=input("QRcode: ")
                            dateofbirth=input("Date of birth: ")
                            Gender=input("Gender: ")
                            Location=input("Location: ")
                            vaccinemanufacturer=input("Name of vaccine manufacuturer: ")
                            Country=input("Name of Country: ")
                            issuedby=input("Issued by: ")
                            registerdetails=Admin(Name,Vaccination,dateofvaccination,QRcode,dateofbirth,Gender,Location,vaccinemanufacturer,Country,issuedby)
                            registerdetails.writeinfo()
                            print("The data has been saved")
                            time.sleep(1)
                            os.system('cls')
                            break
                        elif Option==2:
                            vaccine_details=Admin.infoforprofessionals()
                            print(vaccine_details)
                            time.sleep(3)
                            os.system('cls')
                            break

                        else:
                            print("Please give a valid number")
                    else:
                        print("Admin password is wrong")
                        time.sleep(1)
                        os.system('cls')
                        break
        elif user_detail==4:
            os.system('cls')
            userpreference=input("Which vaccination do you want to know about?")
            a=vaccinationdetails(userpreference.upper())
            a.vacci_description()
            time.sleep(3)
            os.system('cls')
        elif user_detail==5:
            os.system('cls')
            Appinfo.Aboutus()
            time.sleep(3)
            os.system('cls')

        elif user_detail == 6:
            break
        else:
            print("Please enter a Valid Number")
                
    














"""The codes can be improved in a lot of ways. It is practically impossible to have a database of all vaccincation details
of all user in a system. The codes should be improved to send api requests to the vaccination websites and collect
details from the website.For example, If a user wants a polio certificate, The user can type the QRcode and 
in the app and the app sends a api request to the official database/website and get the details from there.
 The app should have a cloud function where the users can access the details from any system and 
place.There are a lot of redundant codes in this program and the codes can be reduced in some places. There are many 
repeated nested if statements which can also be reduced. The passwords saved in csv file should be hashed as well.
"""

      


