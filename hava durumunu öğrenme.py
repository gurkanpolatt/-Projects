import requests
import json

def hava_durumu_api(cidade):
    # OpenWeatherMap API anahtarı
    api_anahtari = "YOUR_API_KEY"

    # API isteği için URL
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_anahtari}"

    # API'ye isteği gönder
    cevap = requests.get(api_url)

    # İsteğin başarılı olup olmadığını kontrol et
    if cevap.status_code == 200:
        # JSON verisini çözümle
        hava_durumu_verisi = json.loads(cevap.text)

        # Hava durumu bilgilerini al
        sicaklik = hava_durumu_verisi['main']['temp']
        durum = hava_durumu_verisi['weather'][0]['description']

        # Bilgileri ekrana yazdır
        print(f"{cidade} şehrinin hava durumu:")
        print(f"Sıcaklık: {sicaklik} K")
        print(f"Durum: {durum}")
    else:
        # İstek başarısız olduysa hata mesajını yazdır
        print(f"Hava durumu bilgisi alınamadı. Hata kodu: {cevap.status_code}")

if __name__ == "__main__":
    sehir = input("Hava durumu bilgisini öğrenmek istediğiniz şehri girin: ")
    hava_durumu_api(sehir)
