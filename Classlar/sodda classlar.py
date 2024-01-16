class Ishchi:
    def __init__(self, ism, firma_raqami, staji):
        self.ism = ism
        self.firma_raqami = firma_raqami
        self.staji = staji

    def get_info(self):
        return f"Ism: {self.ism}, Firma raqami: {self.firma_raqami}, Staji: {self.staji}"

    def update_staji(self):
        self.staji += 1
ishchi = Ishchi("Diyorbek", "ABC123", 5)
print(ishchi.get_info())  
ishchi.update_staji()
print(ishchi.get_info())  

class Jurnal:
    def __init__(self, nomi, davriylik, korinishi, nashriyoti):
        self.nomi = nomi
        self.davriylik = davriylik
        self.korinishi = korinishi
        self.nashriyoti = nashriyoti

    def get_info(self):
        return f"Nomi: {self.nomi}, Davriylik: {self.davriylik}, Ko'rinishi: {self.korinishi}, Nashriyoti: {self.nashriyoti}"

    def set_nomi(self, x):
        self.nomi = x
jurnal = Jurnal("Tarix jurnali", "Haftalik", "Elektron", "O'zbekiston tarixi")
print(jurnal.get_info())  
jurnal.set_nomi("Madaniyat jurnali")
print(jurnal.get_info()) 

class Maxsulot:
    def __init__(self, nomi, soni, narxi, mamlakat):
        self.nomi = nomi
        self.soni = soni
        self.narxi = narxi
        self.mamlakat = mamlakat

    def get_info(self):
        return f"Nomi: {self.nomi}, Soni: {self.soni}, Narxi: {self.narxi}, Mamlakat: {self.mamlakat}"

    def set_narxi(self, x):
        self.narxi *= (1 + x / 100)
maxsulot = Maxsulot("Telefon", 1000, 500, "O'zbekiston")
print(maxsulot.get_info())
maxsulot.set_narxi(10)
print(maxsulot.get_info())  

class Kvitansiya:
    def __init__(self, raqami, sana, pul_miqdori, manzili):
        self.raqami = raqami
        self.sana = sana
        self.pul_miqdori = pul_miqdori
        self.manzili = manzili

    def get_info(self):
        return f"Raqami: {self.raqami}, Sana: {self.sana}, Pul miqdori: {self.pul_miqdori}, Manzili: {self.manzili}"

    def set_manzili(self, x):
        self.manzili = x
kvitansiya_1 = Kvitansiya("12345", "2023-12-25", 150.0, "Toshkent, O'zbekiston")
print(kvitansiya_1.get_info())
kvitansiya_1.set_manzili("Samarqand, O'zbekiston")
print(kvitansiya_1.get_info())  


class Tikuvchilik:
    def __init__(self, ismi, boshliq, ishchi_soni, zavod):
        self.ismi = ismi
        self.boshliq = boshliq
        self.ishchi_soni = ishchi_soni
        self.zavod = zavod

    def get_info(self):
        return f"Tikuvchilik: {self.ismi}, Boshliq: {self.boshliq}, Ishchi soni: {self.ishchi_soni}, Zavod: {self.zavod}"

    def set_ishchi_soni(self, yangi_son):
        self.ishchi_soni = yangi_son

tikuvchilik_1 = Tikuvchilik("Kompaniya ABC", "John Doe", 50, "Zavod A")
print(tikuvchilik_1.get_info())  
tikuvchilik_1.set_ishchi_soni(60)
print(tikuvchilik_1.get_info())

class Shaxs:
    def __init__(self, ism, yoshi, jinsi, millati):
        self.ism = ism
        self.yoshi = yoshi
        self.jinsi = jinsi
        self.millati = millati

    def get_info(self):
        return f"Ism: {self.ism}, Yoshi: {self.yoshi}, Jinsi: {self.jinsi}, Millati: {self.millati}"

    def set_millati(self, x):
        self.millati = x
shaxs_1 = Shaxs("John Doe", 30, "Erkak", "O'zbek")
print(shaxs_1.get_info())  
shaxs_1.set_millati("Amerikalik")
print(shaxs_1.get_info())  

class Korabl:
    def __init__(self, ism, suv_siljishi, turi, yoshi):
        self.ism = ism
        self.suv_siljishi = suv_siljishi
        self.turi = turi
        self.yoshi = yoshi

    def get_info(self):
        return f"Ism: {self.ism}, Suv siljishi: {self.suv_siljishi}, Turi: {self.turi}, Yoshi: {self.yoshi}"

    def set_turi(self, x):
        self.turi = x

korabl_1 = Korabl("Sea Queen", "Petrol", "Yuk", 5)
print(korabl_1.get_info())  
korabl_1.set_turi("Sayohat")
print(korabl_1.get_info())  
class Shahar:
    def __init__(self, nomi, respublikasi, tumani, xuquqiy_xolati):
        self.nomi = nomi
        self.respublikasi = respublikasi
        self.tumani = tumani
        self.xuquqiy_xolati = xuquqiy_xolati

    def get_info(self):
        return f"Nomi: {self.nomi}, Respublikasi: {self.respublikasi}, Tumani: {self.tumani}, Xuquqiy xolati: {self.xuquqiy_xolati}"

    def set_nomi(self, x):
        self.nomi = x

shahar_1 = Shahar("Tashkent", "O'zbekiston", "Yunusobod", "Aholi")
print(shahar_1.get_info())  
shahar_1.set_nomi("Andijon")
print(shahar_1.get_info())  

class Tasvir:
    def __init__(self, nomi, tasvirchi, yili, galereya):
        self.nomi = nomi
        self.tasvirchi = tasvirchi
        self.yili = yili
        self.galereya = galereya

    def get_info(self):
        return f"Nomi: {self.nomi}, Tasvirchi: {self.tasvirchi}, Yili: {self.yili}, Galereya: {self.galereya}"

    def set_yili(self, x):
        self.yili = x

tasvir_1 = Tasvir("Qishloq o'rtasida ko'cha", "Anvar Yusupov", 2023, "Toshkent galereya")
print(tasvir_1.get_info())  
tasvir_1.set_yili(2024)
print(tasvir_1.get_info())  
class Ijarachi:
    def __init__(self, ismi, mamlakat, yoshi, sayohat_maqsadi):
        self.ismi = ismi
        self.mamlakat = mamlakat
        self.yoshi = yoshi
        self.sayohat_maqsadi = sayohat_maqsadi

    def get_info(self):
        return f"Ismi: {self.ismi}, Mamlakat: {self.mamlakat}, Yoshi: {self.yoshi}, Sayohat maqsadi: {self.sayohat_maqsadi}"

    def update_yoshi(self, yangi_yosh):
        self.yoshi = yangi_yosh
ijarachi_1 = Ijarachi("Ali", "O'zbekiston", 35, "Ta'lim")
print(ijarachi_1.get_info())  
ijarachi_1.update_yoshi(40)
print(ijarachi_1.get_info())  

