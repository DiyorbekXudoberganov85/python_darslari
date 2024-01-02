class korxona :
    def __init__(self, nomi , firma_raqami, manzili):
        self.nomi = nomi 
        self.firma_raqami = firma_raqami
        self.manzili = manzili
        self.soni = 1   
    def get_info(self):
        full = f"nomi: {self.nomi}"
        full += f"firma_raqami: { self.firma_raqami}"
        full += f"soni:{self.soni}"
        return full
    def update_soni(self,qiymati):
        self.soni = self.soni + qiymati
    def __repr__(self):
        return self.nomi + " " +str(self.soni)
class ishchi:
    def __init__(self ,ismi ,guruh_raqami,staji):
        self.ismi = ismi 
        self.guruh_raqami = guruh_raqami
        self.staji = staji
        self.ishchilar = []
    def __repr__(self):
        return self.ismi
    def add_ishchilar(self, ishchi):
        self.ishchilar.append(ishchi)
    def get_ishchi(self):
        return self.ishchilar
obg1=korxona("to'yxona", "120", "urganch")    
obg2 = korxona("oshxona", "84558596", "urganch")        
ishchi1 = ishchi("diyorbek" , "994626565265" , "41584")
ishchi1.add_ishchilar(obg1)
ishchi1.add_ishchilar(obg2)


