class Shaxar:
    def __init__(self , tuman_nomi , xuquqiy_xolati):
        self.tuman_nomi = tuman_nomi 
        self.xuquqiy_xolati = xuquqiy_xolati 
    def get_info(self):
        return f"(tuman nomi: {self.tuman_nomi} Xuquqiy xolati: {self.xuquqiy_xolati})"
    def __call__(self):
        return self.tuman_nomi 
    def __repr__(self):
        full = self.tuman_nomi 
        return full
class Viloyat:
    def __init__(self , nomi ,yer_maydoni , axolisi_soni , respublikasi):
        self.nomi = nomi 
        self.yer_maydoni = yer_maydoni
        self.axolisi_soni = axolisi_soni
        self.respublikasi = respublikasi 
        self.Shaxarlar = []
    def get_info(self):
        return f"(Nomi : {self.nomi} axoli soni: {self.axolisi_soni})"
    def add_shaxar(self , shaxar):
        self.Shaxarlar.append(shaxar)
    def get_shaxarlar(self):
        return self.Shaxarlar
shaxar1 = Shaxar("Bagdod", "yaxshi")
shaxar2 = Shaxar("Uchko'prik", "Yomon")
viloyat = Viloyat("Fargona","150km",60000, "O'zbekiston")
viloyat.add_shaxar(shaxar1)
viloyat.add_shaxar(shaxar2)
print(viloyat.get_info())
print(viloyat.get_shaxarlar())