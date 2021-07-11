from main_vaccination import vaccinations
import pandas as pd
import os
class Admin(vaccinations):

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
    
    
    def writeinfo(self): 
        while 1:     
            info=pd.DataFrame([[self.__Name,self.__vaccination,self.__vaccinationdate,self.__code,self.__dateofbirth,self.__Gender,self.__Loction,self.__vaccinemanufacturer,self.__country,self.__issuedby]])
            if os.path.exists("Vaccination.csv"):
                info.to_csv("Vaccination.csv",mode="a",header=False,index=False)
            else:
                info.to_csv("Vaccination.csv",header=False,index=False)


            check = input('Enter Y to update more details or N to quit: ')
            if check.upper() == 'Y':
                pass
            else:
                break
    @staticmethod
    def infoforprofessionals(): 
        os.system('cls')  
        a=input("Enter the name of the vaccination: ")
        col_names=["Name","Vaccination","Date","QR code","dateofbith","Gender","Location","vaccinemanufacturer","country","issuedby"]
        info=pd.read_csv('Vaccination.csv',names=col_names).drop_duplicates(keep='last')
        os.system('cls')
        return info[info["Vaccination"]==a].reset_index(drop=True)

# a=Admin("Aswa","Polio","20.10.2020","C024512","01.01.2000","Male",
# "South east Bayern","BioNTech","Germany","Government of Bayern")
# print(a.infoforprofessionals())
# # print(a.writeinfo())