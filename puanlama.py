# Birim Fiyat Teklif Usulü Yapılan İhalelerde, Puanlama Sistemine uygun birim fiyat belirlemeye dair kod çalışması. Her bir poz için, İdarece belirlenen oranlara uygun teklif birim fiyat tespit eden python uygulaması.

bf = [1, 1, 1, 1, 1]            # Birim fiyatlar. Bu değer değişecek
mkt = [174, 420, 384, 128, 174] # Miktarlar. Bu değer sabit kalacak

toplam_tutarlar = []            # Birim fiyat ile miktar çarpımından oluşan değerlerin tutulduğu liste

alt_yuzde = [0.21, 0.09, 0.30, 0.23, 0.08] # min. yüzdelik dilim
ust_yuzde = [0.25, 0.12, 0.33, 0.26, 0.10] # max. yüzdelik dilim

min_tutar = []                  # İş kalemlerinin en düşük (MİN) toplam tutarlarını barındıran liste
max_tutar = []                  # İş kalemlerinin en yüksek (MAX) toplam tutarlarını barındıran liste

def tutar():                    # Teklif Birim fiyatlar ile Miktarların çarpımını barındıran liste.
    toplam_tutarlar.clear()
    for i in range(len(bf)):
        toplam_tutarlar.append(bf[i] * mkt[i])
    return toplam_tutarlar

tutar(bf, mkt)

def genel_toplam ():                  # GENEL TOPLAMI ( Teklif Tutarı ) Hesaplayan fonksiyonu
    return sum(toplam_tutarlar)

genel_toplam()

def min_tutar():             # İş kalemlerinin en düşük (MİN) toplam tutarlarını hesaplayan fonksiyon
    pass


def max_tutar():             # İş kalemlerinin en yüksek (MAX) toplam tutarlarını  hesaplayan fonksiyon
    pass