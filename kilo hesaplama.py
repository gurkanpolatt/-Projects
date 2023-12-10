def kilo_hesapla(baslangic_agirlik, degisim):
    son_agirlik = baslangic_agirlik + degisim
    return son_agirlik
#Kullanıcıdan  giriş alalım
baslangic_agirlik = float(input("Başlangıç ağırlığınızı girin (kg): "))
degisim = float(input("Değişen kiloyu girin (eğer kilo verdiyseniz negatif değer gir): "))
#Hesaplamayı yapalım
son_agirlik = kilo_hesapla(baslangic_agirlik, degisim)
#Sonucu kullanıcıya gösterelim
print(f"Sizin  son ağırlığınız: {son_agirlik} kg")
