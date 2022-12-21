# obs_university
Üniversitelerde kullanılan Öğrenci Bilgi Sistemleri ve kurumsal olarak personel yönetimi sistemlerine benzer olarak geliştirilmekte olan bir projedir. Açık kaynak kodlu olarak deneysel çalışmalar için geliştirilmektedir. Bu projenin geliştirilmesinde SQL Server 17 Linux, Azure Data Studio, Visual Studio Code, Qt Creator ve Pyhton3 programlama dili kullanılmaktadır. Uygulamada Pyhton kütüphanesi olan pypyodbc kullanılmıştır. Grafik arayüz için ise Pyhton kütüphanesi olan PyQt5 kullanılmıştır.

PIP ile Pypyodbc ve PyQt5 kurmak için:

         pip install pypyodbc
         pip install PyQt5

SQL-SERVER Linux Kurulumu için resmi Micrsoft kaynağını inceleyiniz : https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver16

SQL-SERVER Linux Kurulumu:

         
         wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add - 
         sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2022.list)" 
         sudo apt-get update 
         sudo apt-get install -y mssql-server


Version-0.0.1 Sürüm Notları:
  1. OgrenciVeriTabani isimli veritabanı oluşturulması
  2. OgrenciVeriTabani üzerinde OgrenciTablosu isimli tablo oluşturulması.
  3. OgrenciVeriTabani üzerinde AkademisyenKurumsalVeriTablosu tablosu oluşturulması.
  4. OgrenciVeriTabani üzerinde AkademisyenEgitimVeriTablosu tablosu oluşturulması.
  5. OgrenciVeriTabani üzerinde AkademisyenYuksekLisansVeriTablosu tablosu oluşturulması.
  6. OgrenciVeriTabani üzerinde AkademisyenDoktoraVeriTablosu tablosu oluşturulması.
  7. Öğrenci ekleme
  8. Akademisyen ekleme



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
                          
Akademisyen Eğitim Tablosu Oluşturma:

                          USE OgrenciVeriTabani
                          CREATE TABLE AkademisyenEgitimVeriTablosu
                          (
                          AkademisyenID bigint PRIMARY KEY NOT NULL,
                          Universite varchar(50) NULL,
                          Bolum varchar(50) NULL,
                          OgretimTuru varchar(500) NULL,
                          LisansTuru varchar(50) NULL,
                          Fakulte varchar(50) NULL,
                          Sehir varchar(50) NULL,
                          BaslangicGun INT NULL,
                          BaslangicAy INT NULL,
                          BaslangicYil INT NULL,
                          BitisGun INT NULL,
                          BitisAy INT NULL,
                          BitisYil INT NULL,

                          );
Akademisyen Yüksek Lisans Tablosu Oluşturma:

                          USE OgrenciVeriTabani
                          CREATE TABLE AkademisyenYuksekLisansVeriTablosu
                          (
                          AkademisyenID bigint PRIMARY KEY NOT NULL,
                          Universite varchar(50) NULL,
                          Bolum varchar(50) NULL,
                          Fakulte varchar(50) NULL,
                          Sehir varchar(50) NULL,
                          BaslangicGun INT NULL,
                          BaslangicAy INT NULL,
                          BaslangicYil INT NULL,
                          BitisGun INT NULL,
                          BitisAy INT NULL,
                          BitisYil INT NULL,

                          );
                          
Akademisyen Doktora Tablosu Oluşturma:

                          USE OgrenciVeriTabani
                          CREATE TABLE AkademisyenDoktoraVeriTablosu
                          (
                          AkademisyenID bigint PRIMARY KEY NOT NULL,
                          Universite varchar(50) NULL,
                          Bolum varchar(50) NULL,
                          Fakulte varchar(50) NULL,
                          Sehir varchar(50) NULL,
                          BaslangicGun INT NULL,
                          BaslangicAy INT NULL,
                          BaslangicYil INT NULL,
                          BitisGun INT NULL,
                          BitisAy INT NULL,
                          BitisYil INT NULL,
                          );
