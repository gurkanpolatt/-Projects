import json
import os
from datetime import datetime

class NotDefteri:
    def __init__(self):
        self.notlar = []
        self.kullanici_adi = None
        self.kullanici_girisi()

    def kullanici_girisi(self):
        self.kullanici_adi = input("Kullanıcı adınızı girin: ")

        if os.path.exists(f"{self.kullanici_adi}_notlar.json"):
            self.notlari_yukle()
        else:
            self.notlari_kaydet()

    def notlari_kaydet(self):
        with open(f"{self.kullanici_adi}_notlar.json", "w") as file:
            json.dump(self.notlar, file)

    def notlari_yukle(self):
        with open(f"{self.kullanici_adi}_notlar.json", "r") as file:
            self.notlar = json.load(file)

    def notlari_goster(self):
        if not self.notlar:
            print("Henüz hiç notunuz yok.")
            return

        print("Notlarınız:")
        for i, not_ in enumerate(self.notlar, 1):
            print(f"{i}. Başlık: {not_['baslik']}, Tarih: {not_['tarih']}")

    def not_ekle(self):
        baslik = input("Not başlığını girin: ")
        icerik = input("Not içeriğini girin: ")

        yeni_not = {
            "baslik": baslik,
            "icerik": icerik,
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.notlar.append(yeni_not)
        self.notlari_kaydet()
        print("Not başarıyla eklendi.")

    def not_duzenle(self, not_index):
        if 1 <= not_index <= len(self.notlar):
            yeni_icerik = input("Yeni not içeriğini girin: ")
            self.notlar[not_index - 1]["icerik"] = yeni_icerik
            self.notlari_kaydet()
            print("Not başarıyla güncellendi.")
        else:
            print("Geçersiz not numarası.")

    def not_sil(self, not_index):
        if 1 <= not_index <= len(self.notlar):
            silinecek_not = self.notlar.pop(not_index - 1)
            self.notlari_kaydet()
            print(f'"{silinecek_not["baslik"]}" başlıklı not başarıyla silindi.')
        else:
            print("Geçersiz not numarası.")

if __name__ == "__main__":
    not_defteri = NotDefteri()

    while True:
        print("\n1. Notları Göster")
        print("2. Not Ekle")
        print("3. Not Düzenle")
        print("4. Not Sil")
        print("5. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçin (1-5): ")

        if secim == "1":
            not_defteri.notlari_goster()
        elif secim == "2":
            not_defteri.not_ekle()
        elif secim == "3":
            not_defteri.notlari_goster()
            index = int(input("Düzenlemek istediğiniz notun numarasını girin: "))
            not_defteri.not_duzenle(index)
        elif secim == "4":
            not_defteri.notlari_goster()
            index = int(input("Silmek istediğiniz notun numarasını girin: "))
            not_defteri.not_sil(index)
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")
