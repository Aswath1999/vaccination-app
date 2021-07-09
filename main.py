from main_vaccination import vaccinations
from Vaccination import vaccination
import os
clear = lambda: os.system('cls')

#Need to create an instance of a class
a=vaccinations("Gokul","Polio","20.10.2020","C024512")

"""Need to save the details of the user and vaccination in a database"""
# a.writeinfo()

"""The homepage of the app asks the user to login. After login, the user will get all the details of the 
vaccinations. The user can then decide on what vaccine certificate he wants and download it."""
# print(a.readinfo())

"""After clicking the certificate he wants, the user can then download the certificate. We do not have any 
login system here as it is the second step and the user already has logged in to get details on all his/her vaccinations"""
# a.getcertificate()

"""As health professionals, we are more interested in the analyzing the vaccination details. We can get details of how
many people had taken a particular vaccine and can also be used to administer vacciantions for a particular place.
The vaccination details of all users are only given after consent from the user. Only certified professionals will have access to the details. """
#a.infoforprofessionals()


"""The codes below is a basic program that uses getters and setters.We removed login system for a quicker presentation"""
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
repeated nested if statements which can also be reduced.  
"""

      


    



