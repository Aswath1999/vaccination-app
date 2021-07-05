from Userlogin import userlogin
class vaccination():

    def __init__(self,Name,Vaccination,date):
        self.Name=Name
        self.vaccination=Vaccination
        self.date=date

    def info(self):
        userlogin.main()
        userlogin.clear()
        data=dict(zip(self.vaccination,self.date))
        return self.Name+" is vaccinated with \n"+ ("\n".join("{}\t{}".format(k,v)for k,v in data.items()))

a=vaccination("asw",["Covid","Polio","TB"],["19-05-2020","20.05.1999","19-08-2016"])
print(a.info())

        