class Maxsulot :
    def __init__(self , nomi ,narxi , mamlakat):
        self.nomi = nomi 
        self.narxi = narxi
        self.mamlakat = mamlakat 
    def get_info(self):
        return f"nomi : {self.nomi} narxi: {self.narxi} ishlab chiqarilgan mamlakat :{self.mamlakat}"
    def __repr__(self):
        return self.nomi +" "+ self.narxi
class Dukon :
    def __init__(self,nomi , manzil , turi):
        self.nomi = nomi 
        self.manzil = manzil 
        self.turi = turi 
        self.maxsulotlar = []
    def get_iinfo(self):
        return f"nomi :{self.nomi}   manzili: {self.manzil} turi:{self.turi}"
    def add_dokon(self, maxsulot):
        self.maxsulotlar.append(maxsulot)
    def get_soni(self):
        k = 0 
        for i in self.maxsulotlar:
            k += 1 
        return f"do'konimizda {k} ta maxsulot mavjud"
    def remove_maxsulotlar(self , obj):
        if obj in self.maxsulotlar:
            self.maxsulotlar.remove(obj)
    def get_royxat(self):
        return [k.get_info() for k in self.maxsulotlar]
dokon = Dukon("Pepsi", "Fargona viloyati", "ozoiq ovqat")
maxsulot1 = Maxsulot("shakar", 5000, "O'zbekiston")
maxsulot2 = Maxsulot("shokalad", 50000, "Rassiya")
maxsuloy3 = Maxsulot("Banan", 15000, "Hindiston")
dokon.add_dokon(maxsulot1)
dokon.add_dokon(maxsulot2)
dokon.add_dokon(maxsuloy3)
