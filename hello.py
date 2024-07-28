def menu():
    print("Kitabxana\n")
    print("1. Bosluq qoyaraq musteri elave etme")
    print("2. Normal musteri elave etme")
    print("3. Musteri listine baxma")
    print("4. Kitab elave etme")
    print("5. Kitablari goster")
    print("6. Kitab goturme")
    print("7. Cixis")

class Musteriler:
    musteriler = []
    
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad 
        while True:
            if yas.isdigit():
                self.yas = int(yas)
                break
            else:
                yas = input("Xahis olunur say daxil edin: ")
        self.gmail = ad.lower() + soyad.lower() + "@gmail.com"
        Musteriler.musteriler.append(self)

    @staticmethod
    def stringile_musteri_elave():
        str__ = input("Her hissenin arasinda bosluq qoymaqla ad, soyad, yasi yazin: ")
        if str__.count(" ") == 2:
            ad, soyad, yas = str__.split(" ")
            return Musteriler(ad.capitalize(), soyad.capitalize(), yas)
        else:
            print("Zehmet olmazsa yazi formatini duzeldin, her melumatdan (Ad, soyad, yas) sonra bosluq qoyulmalidir.")
        
    @staticmethod
    def normal_elave():
        x = input("Ad: ")
        y = input("Soyad: ")
        z = input("Yas: ")
        return Musteriler(x, y, z)
    
    @classmethod
    def musteri_goster(cls):
        if cls.musteriler:
            for musteri in cls.musteriler:
                print(f'Ad: {musteri.ad}, Soyad: {musteri.soyad}, Yas: {musteri.yas}, Email: {musteri.gmail}')
        else:
            print("Hal hazirda musteri yoxdur.")

class Kitablar:
    kitaplar = []
    kitap_adlari = []
    
    def __init__(self, kitap_adi, yazar, nov):
        self.adi = kitap_adi
        self.yazar = yazar
        self.nov = nov
        self.veziyyet = "Movcuddur"
        Kitablar.kitaplar.append(self)
        Kitablar.kitap_adlari.append(self.adi)
    
    @staticmethod
    def kitap_elave():
        a = input("Kitabin adi: ")
        b = input("Kitabin yazari: ")
        c = input("Kitabin novu: ")
        Kitablar(a, b, c)

    @classmethod
    def kitablari_goster(cls):
        if cls.kitaplar:
            for idx, kitap in enumerate(cls.kitaplar, start=1):
                print(f"{idx}. adi: {kitap.adi}, Yazar: {kitap.yazar}, Nov: {kitap.nov}, Veziyyet: {kitap.veziyyet}")
        else:
            print('List hele ki bosdur, yeni kitablar elave et.')
    
    @staticmethod
    def kitap_goturme():
        Kitablar.kitablari_goster()
        kitabsirasi = input("Kitabin sirasini daxil edin: ")
        if kitabsirasi.isdigit():
            kitabsirasi = int(kitabsirasi)
            if 0 < kitabsirasi <= len(Kitablar.kitap_adlari):
                Kitablar.kitaplar[kitabsirasi-1].veziyyet = "Movcud deyil"
                print("Kitabi goturdunuz!")
            else:
                print("Secdiyiniz sirada kitab yoxdur")
        else:
            print("Xahis olunur say daxil edin.")

def main():
    while True:
        menu()
        secim = input("Seciminizi edin: ")
        if secim.isdigit():
            secim = int(secim)
            if 0 < secim < 8:
                if secim == 1:
                    Musteriler.stringile_musteri_elave()
                elif secim == 2:
                    Musteriler.normal_elave()
                elif secim == 3:
                    Musteriler.musteri_goster()
                elif secim == 4:
                    Kitablar.kitap_elave()
                elif secim == 5:
                    Kitablar.kitablari_goster()
                elif secim == 6:
                    Kitablar.kitap_goturme()
                elif secim == 7:
                    print("Cixis edilir...")
                    break
            else:
                print("Yanlis secim. Tekrar yoxlayin.")
        else:
            print("Yanlis secim. Tekrar yoxlayin.")

if __name__ == "__main__":
    main()
