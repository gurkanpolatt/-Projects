print("Türkiye'deki siyasi partiler:")
print("1. Adalet ve Kalkınma Partisi (AK Parti)")
print("2. Cumhuriyet Halk Partisi (CHP)")
print("3. Milliyetçi Hareket Partisi (MHP)")
print("4. Yeşil Sol Parti (HDP)")
#kullanıcıdan giriş al
secim = input("Oy kullanmak istediğin parti için bir numara seçin (1-4): ")
#kullanıcının girdisine göre kontrol et
if secim == "1":
    print("Oyunuz Adalet ve Kalkınma Partisi (AK Parti) kullandınız:")
elif secim == "2":
    print("Oyunuz 2. Cumhuriyet Halk Partisi (CHP) kullandınız:")
elif secim == "3":
    print("Oyunuz 3. Milliyetçi Hareket Partisi (MHP) kullandınız:")
elif secim == "4":
    print("Oyunuz 4. Yeşil Sol Parti (HDP) kullandınız:") 
else:
    print("Geçersiz bir seçenek girdiniz. Lütfen 1 ile 4 arasında bir sayı girin.")