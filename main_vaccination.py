import os
import pandas as pd
import csv



class vaccinations: 

    def __init__(self,Name):
        self.__Name=Name

    
    def readinfo(self):       #reads the csv file and outputs the vaccination details of a particular user.
        os.system('cls')
        col_names=["Name","Vaccination","Date","QR code","dateofbith","Gender","Location","vaccinemanufacturer","country","issuedby"]
        info=pd.read_csv('Vaccination.csv',names=col_names)
        return(info[info['Name']==self.__Name].drop_duplicates(subset=['QR code'],keep='last').reset_index(drop=True))


    def __gencertificate__(self,info_certificate):
        file=open("Certificate.txt","w")
        header="\t\t\t\t\tVACCIFICATE \n\t\t Digital Vaccination Certificate\n"
        line="\t\t----------------------------------"
        Vaccinedetails=f'\n\nName: {info_certificate[0]}\nGender: {info_certificate[5]}\nDate of birth: {info_certificate[4]} \nVaccination: {info_certificate[1]}\nDate of vaccination: {info_certificate[2]}'
        Qrcodedetails=f'\nManufacturer: {info_certificate[7]}\nLocation: {info_certificate[6]}\nCountry: {info_certificate[8]}\nQRcode: {info_certificate[3]}\nIssued by: {info_certificate[9]}'
        file.writelines(header)
        file.writelines(line)
        file.writelines(Vaccinedetails)
        file.writelines(Qrcodedetails)
        for i in range(1, 4):
            file.writelines('\n')
            if i == 3:
                file.writelines("\n\t\t\t(This document is valid without the signature)")
        file.close()


    def getcertificate(self,Certificate):  
        os.system('cls')
        with open('Vaccination.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for details in reader:    
                if self.__Name == details[0]and  Certificate==details[1]:
                    self.__gencertificate__(details)
                    print("\t\t\t VACCIFICATE")
                    print("\t\t\n\n\n\n****************Certificate Downloaded Successfully***********************")
                    break    
            else:
                print("Your details haven't been uploaded yet")
      


            
                