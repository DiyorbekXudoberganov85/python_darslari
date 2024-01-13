class Ustoz:
    def __init__(self ,ismi ,yoshi , maktab , sinf):
        self.ismi = ismi 
        self.yoshi = yoshi 
        self.maktab = maktab 
        self.sinf = sinf 
    def get_info(self):
        return self.ismi 
    def __repr__(self ):
        return self.ismi 
class Maktab:
    def __init__(self , nomi ,raqami , manzili , urni):
        self.nomi = nomi
        self.raqami = raqami 
        self.manzuli = manzili 
        self.urni = urni 
        self.ustozlar = []
    def add_ustoz(self , ad):
        self.ustozlar.append(ad)
    def get_info(self):
        return self.ustozlar
maktab = Maktab("ixtisoslashgan", 1, "xitoy qishlogi", "12-uy")
ustoz1 = Ustoz("Diyorbek", 20, 42, "10-sinf")
ustoz2 = Ustoz("Fotima", 26, 4, "8-sinf")