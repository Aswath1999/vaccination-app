import os

class Appinfo:
    def Aboutus():
        print("Vaccificate is a software app that allows one to access their digital certificates from everywhere")
        print("The app is very easy to access and is interoperable. There is no need to carry your certificates if you have Vaccificate")
        print("Life is easier with vaccificate")


class vaccinationdetails:
    
    def __init__(self,name):
        self.__name=name

    def vacci_description(self):


        if self.__name=="POLIO":
            with open ("Vacci_data.txt","w",encoding="utf-8") as file: 
               file.write("****************************VACCINE DESCRIPTION*******************************")
               file.write("\n************Here you find the complete Description of the vaccines*************")
               file.writelines('\n\n * polio -  Poliovirus vaccine is an active immunizing agent used to prevent poliomyelitis (polio).'\
            '\nIt works by causing your body to produce its own protection (antibodies) against the virus that causes polio.'\
            '\n* WHEN SHOULD A POLIO VACCINE BE GIVEN - recommends a 4 dose schedule at birth, 6, 10 and 14 weeks.'\
            '\nDepending on the hygiene settings, more than 4 doses of OPV are needed to protect children for life.'\
            '\n\n*BENEFITS -produces antibodies in the blood ("humoral" or serum immunity) to all three types of poliovirus')
            file.close()
            with open ("Vacci_data.txt","r",encoding="utf-8") as file: 
                os.system('cls')
                a=file.readlines()
                print(a)
        
        elif self.__name=="COVID19":
            with open ("Vacci_data.txt","w",encoding='utf-8') as file: 
                file.write("****************************VACCINE DESCRIPTION*******************************")
                file.write("\n************Here you find the complete Description of the vaccines*************")
                file.write('\n\n COVID-19  - A COVID‑19 vaccine is a vaccine intended to provide acquired immunity against severe\n'\
                         'acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2), the virus that\ncauses coronavirus disease 2019 (COVID‑19).\n*'\
                         'WHEN SHOULD A COVID-19 VACCINE GIVEN - We continue to recommend COVID-19 vaccination for anyone above 12 years of age and older and older\n'\
                        'you will need 2 shots to get the most protection.')
                file.close()
            with open ("Vacci_data.txt","r",encoding="utf-8") as file: 
                os.system('cls')
                a=file.readlines()
                print(a)
                        
        
        elif self.__name=="INFLUENZA":
            with open ("Vacci_data.txt","w",encoding='utf-8') as file: 
               file.write("****************************VACCINE DESCRIPTION*******************************")
               file.write("\n************Here you find the complete Description of the vaccines*************")
               file.write('\n\n INFLUENZA - Influenza vaccines, also known as flu shots or flu jabs, are vaccines that protect\n\t'\
                'against infection by influenza viruses.\n * WHEN SHOULD VACCINE BE GIVEN - we recommend a flu vaccine by the'\
                'end of October,\n before flu begins spreading in your community.')
               file.close()
            with open ("Vacci_data.txt","r",encoding="utf-8") as file: 
                os.system('cls')
                a=file.readlines()
                print(a)
        elif self.__name=="HEPATITIS_A":
            with open ("Vacci_data.txt","w",encoding='utf-8') as file: 
               file.write("****************************VACCINE DESCRIPTION*******************************")
               file.write("\n************Here you find the complete Description of the vaccines*************")
               file.writelines('\n\n HEPATITIS A -  a person who has not previously received hepatitis A vaccine and who has\n\t'\
                    'direct contact with someone with hepatitis A should get hepatitis A vaccine within 2 weeks after exposure.'\
                    '\n\t WHEN SHOULD A COVID-19 VACCINE GIVEN:\n *Children need 2 doses of hepatitis A vaccine:\n First dose: 12'\
                    'through 23 months of age and\nSecond dose: at least 6 months after the first dose.')  
               file.close()
            with open ("Vacci_data.txt","r",encoding="utf-8") as file: 
                os.system('cls')
                a=file.readlines()
                print(a)      
        else:
            print("The details have not yet been updated yet.")
    
    
 