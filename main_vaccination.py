import pandas as pd
from Userlogin import userlogin

class vaccination: 

    def __init__(self,Name,Vaccination,dateofvaccination,QRcode):
        self.__Name=Name
        self.__vaccination=Vaccination
        self.__vaccinationdate=dateofvaccination
        self.__code=QRcode
    
    def writeinfo(self):
        info=pd.DataFrame([[self.__Name,self.__vaccination,self.__vaccinationdate,self.__code]])
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"],usecols=["QR code"]).drop_duplicates(keep='first').reset_index()
        # info=info.drop_duplicates(subset=None,keep='first',inplace=False,ignore_index=False)
        info.to_csv("Vaccination.csv",mode="a",index=False,header=False)
    
    def readinfo(self):
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
        print(info[info['Name']==self.__Name])

    def updateinfo(self,Oldinfo,newinfo):
        self.__oldinfo=Oldinfo
        self.__newinfo=newinfo
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
        info=info.replace(Oldinfo,newinfo)
        return info


    def infoforprofessionals(self,vaccination="Polio"):
        userlogin.login()
        userlogin.clear()
        self.vaccination=vaccination
        info=pd.read_csv('Vaccination.csv',names=["Name","Vaccination","Date","QR code"])
        info=info.drop_duplicates(subset="QR code",keep='last',inplace=False,ignore_index=False)
        return (info[info["Vaccination"]==vaccination])


    


a=vaccination("Gokul","Polio","18.04.2020","A1732105")
b=vaccination("Aswath","Polio","18.04.2020","A1732115")
c=vaccination("Dhin","Polio","18.04.2020","A1732101")
d=vaccination("Dhin","Covid","18.04.2020","A1732401")
d.writeinfo()
a.writeinfo()
b.writeinfo()
c.writeinfo()
print(a.readinfo())
# print(a.updateinfo("Gokul","Asw"))
# print(a.infoforprofessionals("Covid")
