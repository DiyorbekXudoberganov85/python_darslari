class Futbolchi:
    def __init__(self , ismi , yoshi , kim_bolib_oynaydi, gollar_soni):
       self.ismi = ismi 
       self.yoshi = yoshi 
       self.kim_bolib_oynaydi = kim_bolib_oynaydi 
       self.gollar_soni = gollar_soni 
    def __repr__(self ):
        return self.ismi 
class Jamoa:
    def __init__(self ,nomi , galabalar_soni , maglubyatlar_soni):
        self.nomi = nomi 
        self.galabalar_soni = galabalar_soni 
        self.maglubyatlar_soni = maglubyatlar_soni 
        self.fudbolchilar = []
    def add_fudbolchi(self , add):
        self.fudbolchilar.append(add)
    def get_info(self):
        return self.fudbolchilar 
add1 = Futbolchi("Diyorbek", 20, "xujumchi", 651)
add2 = Futbolchi("Ulugbek", 19, "darvozabon", 0)
jamoa = Jamoa("Barselon", 8, 2)