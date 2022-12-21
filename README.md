# obs_university
Üniversitelerde kullanılan Öğrenci Bilgi Sistemleri ve kurumsal olarak personel yönetimi sistemlerine benzer olarak geliştirilmekte olan bir projedir. Açık kaynak kodlu olarak deneysel çalışmalar için geliştirilmektedir.

V 0.0.1 Sürüm Notları:
  1. OgrenciVeriTabani isimli veritabanı oluşturulması
  2. OgrenciVeriTabani üzerinde OgrenciTablosu isimli tablo oluşturulması.
  3. OgrenciVeriTabani üzerinde AkademisyenKurumsalVeriTablosu tablosu oluşturulması.
  4. OgrenciVeriTabani üzerinde AkademisyenEgitimVeriTablosu tablosu oluşturulması.
  5. OgrenciVeriTabani üzerinde AkademisyenYuksekLisansVeriTablosu tablosu oluşturulması.
  6. OgrenciVeriTabani üzerinde AkademisyenDoktoraVeriTablosu tablosu oluşturulması.
  7. Öğrenci ekleme(Öğrenci ID, Kimlik ID, İsim, Soyisim, Adres, Telefon Numarası, E-Posta,Uyruk,Cinsiyet, Şehir, Doğum Tarihi, Bölüm, Fakülte, Öğretim Türü,Öğrenci Türü,Kayıt Tarihi)
  8. Akademisyen ekleme
  9. AkademisyenKurumsalVeriTablosu için akademisyen bilgileri ekleme (Akademisyen ID, Kimlik ID, İsim, Adres, Telefon Numarası, Uyruk, Cinsiyet, Şehir, Doğum Tarihi, Görev Bilgileri, Okul E-Postası, Görev Başlana Tarihi)
  10. AkademisyenEgitimVeriTablosu için akademisyen eğitim bilgileri ekleme(Akademisyen ID, Üniversite, Bölüm, Öğretim Türü, Lisans Türü, Fakülte, Şehir, Başlama Tarihi, Bitirme Tarihi)
  11. AkademisyenYuksekLisansVeriTablosu için akademisyen yüksek lisans bilgileri ekleme(Akademisyen ID, Üniversite, Bölüm, Fakülte, Şehir, Başlangıç Tarihi, Bitirme Tarihi)
  12. AkademisyenDoktoraVeriTablosu için akademisyen doktora bilgileri ekleme(Akademisyen ID, Üniversite, Bölüm, Fakülte, Şehir, Başlama Tarihi, Bitirme Tarihi)

Öğrenci Tablosu Olıuşturma:

                          USE OgrenciVeriTabani
                          CREATE TABLE OgrenciTablosu
                          (
                          OgrenciID bigint PRIMARY KEY NOT NULL,
                          KimlikID bigint NULL,
                          Isim varchar(50) NULL,
                          Soyisim varchar(50) NULL,
                          Addres varchar(500) NULL,
                          TelNo bigint NULL,
                          EPosta varchar(50) NULL,
                          Uyruk varchar(50) NULL,
                          Cinsiyet varchar(50) NULL,
                          Sehir varchar(50) NULL,
                          DogumGun INT NULL,
                          DogumAy INT NULL,
                          DogumYil INT NULL,
                          Fakulte varchar(50) NULL,
                          Bolum varchar(50) NULL,
                          OgretimTuru varchar(50) NULL,
                          OgrenciTuru varchar(50) NULL,
                          OkulEposta varchar(50) NULL,
                          DGS varchar(50) NULL,
                          YatayGecis varchar(50) NULL,
                          KayitGun INT NULL,
                          KayitAy INT NULL,
                          KayitYil INT NULL,

                          );
Akademisyen Tablosu Olıuşturma:
                          USE OgrenciVeriTabani
                          CREATE TABLE AkademisyenKurumsalVeriTablosu
                          (
                          AkademisyenID bigint PRIMARY KEY NOT NULL,
                          KimlikID bigint NULL,
                          Isim varchar(50) NULL,
                          Soyisim varchar(50) NULL,
                          Adres varchar(500) NULL,
                          TelNo bigint NULL,
                          EPosta varchar(50) NULL,
                          Uyruk varchar(50) NULL,
                          Cinsiyet varchar(50) NULL,
                          Sehir varchar(50) NULL,
                          DogumGun INT NULL,
                          DogumAy INT NULL,
                          DogumYil INT NULL,
                          GorevFakulte varchar(50) NULL,
                          GorevBolum varchar(50) NULL,
                          GorevOgretimTuru varchar(50) NULL,
                          GorevLisansTuru varchar(50) NULL,
                          GorevTuru varchar(50) NULL,
                          OkulEposta varchar(50) NULL,
                          GorevKayitGun INT NULL,
                          GorevKayitAy INT NULL,
                          GorevKayitYil INT NULL,

                          );
