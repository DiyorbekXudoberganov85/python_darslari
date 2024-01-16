class ishchi :
    def __init__(self, ismi , firma_raqami , staji):
        self.ismi=ismi
        self.firma_raqami=firma_raqami
        self.staji=staji
    def get_info(self):
        return f"ism:{self.ismi} firma raqami :{self.firma_raqami} staji: {self.staji}"
    def update(self , staji):
        self.staji=staji
ishchii = ishchi("Diyorbek" , "75" , "45 yil")     
ishchii.update("48yil")       
print(ishchii.get_info())