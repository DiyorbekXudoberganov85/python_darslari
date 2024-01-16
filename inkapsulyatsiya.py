class Talaba :
    __number = 0
    def __init__(self , ism , familya , shartnoma):
        Talaba.__number += 1
        self.__id = Talaba.__number
        self.ism = ism 
        self.familya = familya 
        self.shartnoma = shartnoma 
    def get_id(self):
        return self.__id 
    def change_id(self , x):
        self.__id = x
    def obyektlar_soni(cls):
        return cls.__number
class Shaxs :
    __odamlar_soni = 0
    def __init__(self, ism , familya , ish_joyi  ,jshshir , pasporti="AA1234567"):
        Shaxs.__odamlar_soni +=1
        self.ism = ism 
        self.familya = familya
        self.ish_joyi = ish_joyi 
        self.__jshshir = jshshir 
        self.pasporti =pasporti 
    def get_str(self):
        return self.__jshshir 
    def change_str(self , x ):
        self.__jshshir =x
    def obyektlar_soni(cls):
        return cls.__odamlar_soni 
talaba1 =Talaba("Diyorbek", "Xudoberganov", "kantrakt")
talaba2 = Talaba("Ulugbek" , "Abdulxayev" , "kontrakr")
talaba3 = Talaba("Umidjon" ,"Otajonov" , "grant")
shaxs1 = Shaxs("otabek", "abdukarimov", "maktab"  , 1452630258974586)
