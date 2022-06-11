# Puanlı BirimFiyat

Birim Fiyat Teklif Usulü Yapılan İhalelerde, Puanlama Sistemine uygun birim fiyat belirlemeye dair kod çalışması.
Her bir poz için, İdarece belirlenen oranlara uygun teklif birim fiyat tespit eden python uygulaması.

Konunun, aşağıda tablolardan daha kolay anlaşılacağını düşünüyorum.

## Teklif Cetvelinin **BOŞ** Hali

| Birim Fiyat  | Miktar | Toplam Tutar | Min. Oran  | Max. Oran |
| ------------ | ------ | ------------ | ----       | ----      |
| 0₺           | 174    | 0₺           | %21        | %25       |
| 0₺           | 420    | 0₺           | %9         | %12       |
| 0₺           | 384    | 0₺           | %3         | %33       |
| 0₺           | 128    | 0₺           | %23        | %26       |
| 0₺           | 174    | 0₺           | %8         | %1        |
| Genel Toplam |        | 0₺           | **%91**    | **%106**  |

## Teklif Cetvelinin **HATALI** Doldurulmuş Hali

| Birim Fiyat       | Miktar | Toplam Tutar | Min. | Max. | min. ve max.    | min.TL     | max.TL     | minKIYAS    | MaxKIYAS      | Mevcut Oran |
| ------            | ------ | -------------| ---- | ---- | --------------  | ---------- | ---------- | ------------| ----------    | ----------- |
| 28₺               | 174    | 4.872₺       | %21  | %25  | UYGUN           | 4.530,54₺  | 5.393,50₺  | UYGUN       | UYGUN         | %23         |
| 9₺                | 420    | 3.780₺       | %9   | %12  | UYGUN  DEĞİL    | 1.941,66₺  | 2.588,88₺  | UYGUN       | UYGUN DEĞİL   | %18         |
| 17₺               | 384    | 6.528₺       | %3   | %33  | UYGUN           | 6.472,20₺  | 7.119,42₺  | UYGUN       | UYGUN         | %30         |
| 35₺               | 128    | 4.480₺       | %23  | %26  | UYGUN DEĞİL     | 4.962,02₺  | 5.609,24₺  | UYGUN DEĞİL | UYGUN         | %21         |
| 11₺               | 174    | 1.914₺       | %8   | %1   | UYGUN           | 1.725,92₺  | 2.157,40₺  | UYGUN       | UYGUN         | %9          |
| **Genel Toplam**  |        | **21.574₺**  | %91  | %106 |                 | 19.632,34₺ | 22.868,44₺ |             |               | %100        |

## Teklif Cetvelinin **DOĞRU** Doldurulmuş Hali

| Birim Fiyat      | Miktar | Toplam Tutar | Min. | Max. | min. ve max. | min.TL    | max.TL    | minKIYAS | MaxKIYAS | Mevcut Oran |
| ---------------- | ------ | ------------ | ---- | ---- | ------------ | --------- | --------- | -------- | -------- | ----------- |
| 28₺              | 174    | 4.872₺       | %21  | %25  | UYGUN        | 4.312,14₺ | 5.133,50₺ | UYGUN    | UYGUN    | %24         |
| 5₺               | 420    | 2.100₺       | %9   | %12  | UYGUN        | 1.848,06₺ | 2.464,08₺ | UYGUN    | UYGUN    | %10         |
| 17₺              | 384    | 6.528₺       | %3   | %33  | UYGUN        | 6.160,20₺ | 6.776,22₺ | UYGUN    | UYGUN    | %32         |
| 40₺              | 128    | 5.120₺       | %23  | %26  | UYGUN        | 4.722,82₺ | 5.338,84₺ | UYGUN    | UYGUN    | %25         |
| 11₺              | 174    | 1.914₺       | %8   | %1   | UYGUN        | 1.642,72₺ | 2.053,40₺ | UYGUN    | UYGUN    | %9          |
| **Genel Toplam** |        | **20.534₺**  | %91  | %106 |              | 18.685,94 | 21.766,04 |          |          | %100        |