class Shaxs:
    kursi=3
    def __init__(self , ismi , familiyasi, yoshi=20):
        self.ismi = ismi 
        self.familiyasi = familiyasi 
        self.yoshi = yoshi 
    def get_info(self):
        return f"ismi : {self.ismi} familiyasi: {self.familiyasi} yoshi: {self.yoshi } "
    def __repr__(self):
        return self.ismi
    def __call__(self):
        return self.yoshi 
    def yoshi(cls):
        return cls.kursi
class Professor(Shaxs):
    def __init__(self , ismi , familiyasi , yoshi , tel_nomer , millati):
        super().__init__(ismi, familiyasi, yoshi)
        self.tel_nomer = tel_nomer
        self.millati = millati 
    def get_info() :
        full = super().get_info()
        full +=   self.millati+cls.kursi
        return full 
class Admin(Professor):
    def __init__(self, ismi, familiyasi, yoshi, tel_nomer, millati ,manzili):
        super().__init__(ismi, familiyasi, yoshi, tel_nomer, millati)
        self.manzili = manzili
    def ban_user(self):
        return "foydalanuvchi bloklandi"
d = Admin("Diyorbek", "Xudoberganov", 20, +998931430504, "ozbek", "Fargona")  
