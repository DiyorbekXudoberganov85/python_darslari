# class bo'yicha yechish
class Text:
    def __init__(self, nomi):
        self.nomi = nomi
        with open(f"{self.nomi}", "w") as fayl:
            pass
    def uqish(self):
        with open(f"{self.nomi}", "r") as fayl:
            return fayl.read()
    
    def yozish(self, matn):
        with open(f"{self.nomi}", "w") as fayl:
            fayl.write(matn)
    def frist_row(self):
        with open(f"{self.nomi}", "r") as fayl:
            return fayl.readline()
    def massiv(self):
        with open(f"{self.nomi}", "r") as fayl:
            lines = fayl.readlines()
            lines = [i.strip() for i in lines]
            return lines
    def del_abzas(self):
        with open(f"{self.nomi}" , "r") as fayl :
            d = fayl.readlines()[n]
            for i in d:
               return  i.rstrip() 
    def belgi_soni(self):
        with open(f"{self.nomi}" , "r") as fayl :
            d = fayl.read()
            s = len(d)
            return s 
    def __getitem__(self , n  ):
        with open(f"{self.nomi}" , "r") as fayl :
            return fayl.readlines(n) 
    def del_row(self , n):
        with open(f"{self.nomi}" , "r") as fayl :
            lines = fayl.readlines()
            lines = [i.strip() for i in lines]
            s = lines[::n] + lines[n+1::]
            return s
    def del_rows(self , n  ,m):
        with open(f"{self.nomi}" , "r") as fayl :
            lines = fayl.readlines()
            lines = [i.strip() for i in lines]
            s = lines[:n] + lines[m:]
            return s
    def get_row(self,n):
        with open(f"{self.nomi}" , "r") as fayl:
            d = fayl.readlines()
            d = [i.strip() for i in d]
            s = d[n-1]
            return s
file = Text("Salom.txt")
file.yozish("kecha kelgundir debon\nul sarvi gulro kelmadi\nko'zlarimga kecha tong\n otguncha uyqu kelmadi")