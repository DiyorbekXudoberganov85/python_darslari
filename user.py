class user :
    def __init__(self , ism ,foydalanufchi_ismi , email):
        self.ism = ism 
        self.foydalanufchi_ismi=foydalanufchi_ismi
        self.email = email
    def get_malumot(self):
        return f"\nism : {self.ism} \nfoydalanufchi : {self.foydalanufchi_ismi} \nemail : {self.email}"
    def set_email(self, gmail):
        self.email =gmail
userr = user("Diyorbek" , "diyorbek1122" , "xudaberganovdiyorbek556@gmail.com")    
userr.set_email("aliali@gmail.com")
print(userr.get_malumot() )
