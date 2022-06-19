# Birim Fiyat Teklif Usulü Yapılan İhalelerde, Puanlama Sistemine uygun birim fiyat belirlemeye dair kod çalışması. Her bir poz için, İdarece belirlenen oranlara uygun teklif birim fiyat tespit eden python uygulaması.

bf = [1, 1, 1, 1, 1]        # Birim fiyatlar. Bu değer değişecek 28, 5, 17, 40, 11 - 1, 1, 1, 1, 1
mkt = [174, 420, 384, 128, 174] # Miktarlar. Bu değer sabit kalacak

toplam_tutarlar = []            # Birim fiyat ile miktar çarpımından oluşan TOPLAM TUTARLARI barıdıran liste

alt_yuzde = [0.21, 0.09, 0.30, 0.23, 0.08] # min. yüzdelik dilim
ust_yuzde = [0.25, 0.12, 0.33, 0.26, 0.10] # max. yüzdelik dilim

min_tutarlar = []                  # İş kalemlerinin en düşük (MİN) toplam tutarlarını barındıran liste
max_tutarlar = []                  # İş kalemlerinin en yüksek (MAX) toplam tutarlarını barındıran liste

def tutar():                    # Teklif Birim fiyatlar ile Miktarların çarpımını barındıran liste.
    toplam_tutarlar.clear()
    for i in range(len(bf)):
        toplam_tutarlar.append(round(bf[i] * mkt[i],2))
    return toplam_tutarlar

print("toplam_tutarlar: ", tutar())

def genel_toplam ():            # GENEL TOPLAMI ( Teklif Tutarı ) Hesaplayan fonksiyonu
    return sum(toplam_tutarlar)

genel_toplam()

def min_tutar():                # İş kalemlerinin en düşük (MİN) toplam tutarlarını hesaplayan fonksiyon
    min_tutarlar.clear()
    for i in range(len(alt_yuzde)):
        min_tutarlar.append(round(alt_yuzde[i] * genel_toplam(),2))
    return min_tutarlar

print("min_tutarlar:", min_tutar())

def max_tutar():                # İş kalemlerinin en yüksek (MAX) toplam tutarlarını  hesaplayan fonksiyon
    max_tutarlar.clear()
    for i in range(len(ust_yuzde)):
        max_tutarlar.append(round(ust_yuzde[i] * genel_toplam(),2))
    return max_tutarlar

print("max_tutarlar:", max_tutar())

# def kontrol():
#     for _ in range(100):
#         for i in range(len(bf)):
#             if (((bf[i] * mkt[i]) >= min_tutarlar[i]) and ((bf[i] * mkt[i]) <= max_tutarlar[i])):
#                 print("işlem sonlandı", bf)
#                 break

#             elif ((bf[i] * mkt[i]) < min_tutarlar[i]):
#                 bf[i] += 1
#                 print("değer artırılıyor", bf[i])
            
#             elif ((bf[i] * mkt[i]) > max_tutarlar[i]):
#                 bf[i] -= 1
#                 print("değer azaltılıyor", bf[i])

# def basla():
#     tutar()
#     genel_toplam()
#     min_tutar()
#     max_tutar()
#     kontrol()

# basla()