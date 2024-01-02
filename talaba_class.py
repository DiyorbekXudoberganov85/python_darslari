class Talaba:
    """talaba nomli class yaratamiz"""
    def __init__(self,ism , familiyasi , yili):
        self.ism = ism
        self.familiyasi = familiyasi 
        self.yili = yili 
        self.bosqich = 1
    def set_bosqich(self,yangi_bosqich):
        self.bosqich +=1 
    def update_bosqich(self):
        self.bosqich +=1
    def get_info(self):
        return f"ismi {self.ism} familiyasi : {self.familiyasi} yili : {self.yili}"
    def get_fullname(self):
        return f"{self.ism} {self.familiyasi}"
class Fan :
    def __init__(self , nomi):
        self.nomi = nomi 
        self.talabalar_soni = 0 
        self.talabalar = []
    def add_studen(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni +=1 
    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]
    def get_students_num(self):
        return self.talabalar_soni
    def see_methods(klass):
        return [methods for methods in dir(klass) if methods.startswith('__') is False]
matematika = Fan("oliy matematika")
talaba1 = Talaba("Diyorbek", "Xudoberganov", 2004)
talaba2 = Talaba("Umidjon","Abdulxayev", 2004)
talaba3 = Talaba("Ulugbek", "Abdulxayev", 2005)
matematika.add_studen(talaba1)
matematika.add_studen(talaba2)
matematika.add_studen(talaba3)
print(matematika.get_students())