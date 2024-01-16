class Shaxs :
    def __init__(self , ism , familiya , ish_joyi ):
        self.ism = ism 
        self.familiya =familiya 
        self.ish_joyi = ish_joyi 
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.ish_joyi}"
    def delet(self,yangi):
        self.ish_joyi = yangi 

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, ish_joyi ,manzili):
        super().__init__(ism, familiya, ish_joyi)
        self.manzili = manzili 
    def get_info(self):
        return super().get_info() + self.manzili

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, ish_joyi, manzili , millati):
        super().__init__(ism, familiya, ish_joyi, manzili)
        self.millati = millati 
    def ban_user(self):
        return "Foydalanuvchi bloklandi"
add = Admin("Diyorbek", "Xudoberganov", "maktab", "urganch", "uzbek")
