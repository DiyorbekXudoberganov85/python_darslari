class Tikuvchi :
    def __init__(self , ism , familiya , lavozim , staji):
        self.ism = ism 
        self.familiya = familiya
        self.lavozim = lavozim 
        self.staji = staji 
    def get_info(self):
        return f"ismi : {self.ism} familiyam : {self.familiya} lavozimi : {self.lavozim} staji: {self.staji} yil"
class Tikuvchiliksexi :
    def __init__(self , nomi ,boshliq , ishchi_soni):
        self.nomi = nomi
        self.boshliq =boshliq 
        self.ishchi_soni =ishchi_soni
        self.ishchilar = []
    def get_iinfo(self):
        return f"nomi : {self.nomi} boshliq: {self.boshliq} ishchi soni {self.ishchi_soni}"
    def add_tikuvchi(self,tikuvchi):
        self.ishchilar.append(tikuvchi)
    def get_remove(self , obj):
        self.ishchilar.remove(obj)
    def get_royxat(self):
        return [k.get_info() for k in self.ishchilar]
        
sex = Tikuvchiliksexi("Barno", "Diyorbek", 100)
tikuvchi1 = Tikuvchi("fotima", "Nurmetova", "tikuvchi", 0.5)
tikuvchi2 = Tikuvchi("Muxlisa", "Rajabboyeva" ,"Dazmolchi", 12)
tikuvchi3 = Tikuvchi("Nigora", "Yusuvjonova", "tikuvchi", 5)
sex.add_tikuvchi(tikuvchi1)
sex.add_tikuvchi(tikuvchi2)
sex.add_tikuvchi(tikuvchi3)

