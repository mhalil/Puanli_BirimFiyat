# Birim Fiyat Teklif Usulü Yapılan İhalelerde, Puanlama Sistemine uygun birim fiyat belirlemeye dair kod çalışması. Her bir poz için, İdarece belirlenen oranlara uygun teklif birim fiyat tespit eden python uygulaması. Hesaplama Toplam Teklif Tutarının belirlenmesi ile, tüm pozlara min. ve max. birim fiyatlarını belirleme esasına dayanır.

birim_fiyatlar = []        # Hesaplanacak olan Birim fiyatlar, liste olarak eklenecek
miktarlar = [174, 420, 384, 128, 174] # Miktarlar. Bu değer sabittir, ihale dokumanında belirtilen değerlerdir.

teklif_tutari = int(input("Toplam Teklif bedeli belirtin: "))            # Kullaıcıdan istenilen tahmini toplam teklif bedeli.

alt_yuzde = [0.21, 0.09, 0.30, 0.23, 0.08] # min. yüzdelik dilim. Bu değer sabittir, ihale dokumanında belirtilen değerlerdir
ust_yuzde = [0.25, 0.12, 0.33, 0.26, 0.10] # max. yüzdelik dilim. Bu değer sabittir, ihale dokumanında belirtilen değerlerdir

for i in range(len(miktarlar)):
    alt = round(teklif_tutari * alt_yuzde[i] / miktarlar[i],2)
    ust = round(teklif_tutari * ust_yuzde[i] / miktarlar[i],2)
    birim_fiyatlar.append([alt, ust])

toplam_min = 0
toplam_max = 0

for i in range(len(miktarlar)):
    toplam_min += birim_fiyatlar[i][0] * miktarlar[i]
    toplam_max += birim_fiyatlar[i][1] * miktarlar[i]

for index, bf in enumerate(birim_fiyatlar):
    print(f"{index+1}. Poza ait min. ve max. fiyat aralığı: {birim_fiyatlar[index]}")

print(f"Min. Birim Fiyatlara Göre Toplam Teklif Tutarı: {round(toplam_min,2)} TL\nMax. Birim Fiyatlara Göre Toplam Teklif Tutarı: {round(toplam_max,2)} TL")