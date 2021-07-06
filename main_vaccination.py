import pandas as pd
from Userlogin import userlogin

class vaccination(userlogin): 

    def __init__(self,Name,Vaccination,dateofvaccination,QRcode):         
        self.__Name=Name
        self.__vaccination=Vaccination
        self.__vaccinationdate=dateofvaccination
        self.__code=QRcode
    
    def writeinfo(self):       #saves the instance from __init__ constructor in a cvv file 
        info=pd.DataFrame([[self.__Name,self.__vaccination,self.__vaccinationdate,self.__code]])
        info.to_csv("Vaccination.csv",mode="a",header=False)  #Use mode="w" when writing first instance
    
    def readinfo(self):        #reads the csv file and outputs the vaccination details of a particular user.
        userlogin.main_menu()
        userlogin.clear()
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
        return info[info['Name']==self.__Name].drop_duplicates(subset=['QR code'],keep='last').reset_index(drop=True)
        

    def updateinfo(self,Oldinfo,newinfo):  #to change the value.Changes all values in the database
        self.__oldinfo=Oldinfo
        self.__newinfo=newinfo
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
        info=info.replace(Oldinfo,newinfo)
        return info


    def infoforprofessionals(self,vaccination="Polio"):    #displays details of all users for a particular vaccination 
        userlogin.main_menu()
        userlogin.clear()
        self.vaccination=vaccination
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"]).drop_duplicates(keep='last')
        return info[info["Vaccination"]==vaccination].reset_index(drop=True)

    def getcertificate(self):   #not working yet but should display a vaccinationcertificate in sentences
        userlogin.main_menu()
        userlogin.clear()
        print("Vaccination certificate")
        print("------------------------")
        return f'Name: {self.__Name}\nVaccination:{self.__vaccination}\nManufacturer:  \nQR code:{self.__code}'
                
      
    


a=vaccination("Gokul","Polio","18.04.2020","A1732105")
b=vaccination("Aswath","Polio","18.04.2020","A1732115")
c=vaccination("Dhin","Polio","18.04.2020","A1732101")
d=vaccination("Dhin","Covid","18.04.2020","A1732401")
e=vaccination("Aswath","Covid","18.04.2020","A4732401")
# b.writeinfo()
# a.writeinfo()
# d.writeinfo()
# e.writeinfo()
# c.writeinfo()
print(a.getcertificate())
# print(a.updateinfo("Gokul","Asw"))
# print(a.infoforprofessionals("Covid")
