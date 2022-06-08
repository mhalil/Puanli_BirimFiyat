# Birim Fiyat Teklif Usulü Yapılan İhalelerde, Puanlama Sistemine uygun birim fiyat belirlemeye dair kod çalışması. Her bir poz için, İdarece belirlenen oranlara uygun teklif birim fiyat tespit eden python uygulaması.

bf = [28, 5, 17, 40, 11] # birim fiyatlar. Bu değer değişecek
mkt = [174, 420, 384, 128, 174] # miktarlar. Bu değer sabit kalacak

tutarlar = [] # birim fiyat ile miktar çarpımından oluşan değerlerin tutulduğu liste

alt_yzd = [0.21, 0.09, 0.30, 0.23, 0.08] # min. yüzdelik dilim
ust_yzd = [0.25, 0.12, 0.33, 0.26, 0.10] # max. yüzdelik dilim

def tutar(bf_:list, mkt_:list):     # Teklif Birim fiyatlar ile Miktarların çarpımını barındıran liste.
    tutarlar.clear()
    for i in range(len(bf_)):
        tutarlar.append(bf_[i] * mkt_[i])
    return tutarlar

# print(tutar(bf, mkt))

tutar(bf, mkt)

def toplam ():                      # Toplam Teklif Tutarı
    return sum(tutarlar)

# print(toplam(bf, mkt))

