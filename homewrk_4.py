class Departman:
    def __init__(self, ad):
        self.ad = ad
        self.personeller = []

    def personel_ekle(self, personel):
        self.personeller.append(personel)

    def personel_listele(self):
        return [personel for personel in self.personeller]

class Personel:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def __str__(self):
        return f"{self.ad} {self.soyad}"

def main():
    muhasebe = Departman("Muhasebe")
    personel1 = Personel("Ahmet", "Yılmaz")
    personel2 = Personel("Ayşe", "Kara")
    muhasebe.personel_ekle(personel1)
    muhasebe.personel_ekle(personel2)

    yazilim = Departman("Yazılım")
    personel1 = Personel("Yıldız", "Binici")
    personel2 = Personel("Zeynep", "Çelik")
    yazilim.personel_ekle(personel1)
    yazilim.personel_ekle(personel2)
  

    print("Muhasebe Departmanındaki Personeller:")
    for personel in muhasebe.personel_listele():
        print(personel)

    print("Yazılım Departmanındaki Personeller:")
    for personel in yazilim.personel_listele():
        print(personel)


if __name__ == "__main__":
    main()
