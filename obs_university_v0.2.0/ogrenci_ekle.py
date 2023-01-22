# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication
import sys

import pypyodbc
import pandas as pd
import sqlite3

class Ui_OBS_Project(object):
    def setupUi(self, OBS_Project):
        OBS_Project.setObjectName("OBS_Project")
        OBS_Project.resize(1086, 650)
        OBS_Project.setMinimumSize(QtCore.QSize(1086, 600))
        OBS_Project.setMaximumSize(QtCore.QSize(1086, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OBS_Project.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(OBS_Project)
        self.label.setGeometry(QtCore.QRect(10, 30, 401, 41))
        self.label.setStyleSheet("font: 81 25pt \"Cantarell\";")
        self.label.setObjectName("label")
        self.groupBox_kimlik = QtWidgets.QGroupBox(OBS_Project)
        self.groupBox_kimlik.setGeometry(QtCore.QRect(20, 140, 1061, 201))
        self.groupBox_kimlik.setObjectName("groupBox_kimlik")
        self.isim = QtWidgets.QLabel(self.groupBox_kimlik)
        self.isim.setGeometry(QtCore.QRect(0, 30, 111, 21))
        self.isim.setObjectName("isim")
        self.lineEdit_isim = QtWidgets.QLineEdit(self.groupBox_kimlik)
        self.lineEdit_isim.setGeometry(QtCore.QRect(130, 30, 371, 27))
        self.lineEdit_isim.setObjectName("lineEdit_isim")
        self.lineEdit_soyisim = QtWidgets.QLineEdit(self.groupBox_kimlik)
        self.lineEdit_soyisim.setGeometry(QtCore.QRect(130, 60, 371, 27))
        self.lineEdit_soyisim.setObjectName("lineEdit_soyisim")
        self.lineEdit_kimlik_id = QtWidgets.QLineEdit(self.groupBox_kimlik)
        self.lineEdit_kimlik_id.setGeometry(QtCore.QRect(130, 90, 371, 27))
        self.lineEdit_kimlik_id.setObjectName("lineEdit_kimlik_id")
        self.lineEdit_adres = QtWidgets.QLineEdit(self.groupBox_kimlik)
        self.lineEdit_adres.setGeometry(QtCore.QRect(130, 120, 371, 81))
        self.lineEdit_adres.setText("")
        self.lineEdit_adres.setObjectName("lineEdit_adres")
        self.soyisim = QtWidgets.QLabel(self.groupBox_kimlik)
        self.soyisim.setGeometry(QtCore.QRect(0, 60, 111, 21))
        self.soyisim.setObjectName("soyisim")
        self.kimlil_id = QtWidgets.QLabel(self.groupBox_kimlik)
        self.kimlil_id.setGeometry(QtCore.QRect(0, 90, 111, 21))
        self.kimlil_id.setObjectName("kimlil_id")
        self.adres = QtWidgets.QLabel(self.groupBox_kimlik)
        self.adres.setGeometry(QtCore.QRect(0, 120, 111, 21))
        self.adres.setObjectName("adres")
        self.tel_no = QtWidgets.QLabel(self.groupBox_kimlik)
        self.tel_no.setGeometry(QtCore.QRect(540, 30, 111, 21))
        self.tel_no.setObjectName("tel_no")
        self.lineEdit_tel_no = QtWidgets.QLineEdit(self.groupBox_kimlik)
        self.lineEdit_tel_no.setGeometry(QtCore.QRect(650, 30, 371, 27))
        self.lineEdit_tel_no.setObjectName("lineEdit_tel_no")
        self.label_eposta = QtWidgets.QLabel(self.groupBox_kimlik)
        self.label_eposta.setGeometry(QtCore.QRect(540, 60, 111, 21))
        self.label_eposta.setObjectName("label_eposta")
        self.lineEdit_eposta = QtWidgets.QLineEdit(self.groupBox_kimlik)
        self.lineEdit_eposta.setGeometry(QtCore.QRect(650, 60, 371, 27))
        self.lineEdit_eposta.setObjectName("lineEdit_eposta")
        self.label_cinsiyet = QtWidgets.QLabel(self.groupBox_kimlik)
        self.label_cinsiyet.setGeometry(QtCore.QRect(820, 90, 111, 21))
        self.label_cinsiyet.setObjectName("label_cinsiyet")
        self.comboBox_sehir = QtWidgets.QComboBox(self.groupBox_kimlik)
        self.comboBox_sehir.setGeometry(QtCore.QRect(650, 120, 151, 27))
        self.comboBox_sehir.setObjectName("comboBox_sehir")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.comboBox_sehir.addItem("")
        self.label_sehir = QtWidgets.QLabel(self.groupBox_kimlik)
        self.label_sehir.setGeometry(QtCore.QRect(540, 120, 111, 21))
        self.label_sehir.setObjectName("label_sehir")
        self.label_uyruk = QtWidgets.QLabel(self.groupBox_kimlik)
        self.label_uyruk.setGeometry(QtCore.QRect(540, 90, 111, 21))
        self.label_uyruk.setObjectName("label_uyruk")
        self.comboBox_uyruk = QtWidgets.QComboBox(self.groupBox_kimlik)
        self.comboBox_uyruk.setGeometry(QtCore.QRect(650, 90, 151, 27))
        self.comboBox_uyruk.setObjectName("comboBox_uyruk")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_uyruk.addItem("")
        self.comboBox_cinsiyet = QtWidgets.QComboBox(self.groupBox_kimlik)
        self.comboBox_cinsiyet.setGeometry(QtCore.QRect(890, 90, 131, 27))
        self.comboBox_cinsiyet.setObjectName("comboBox_cinsiyet")
        self.comboBox_cinsiyet.addItem("")
        self.comboBox_cinsiyet.addItem("")
        self.label_dogum_tarih = QtWidgets.QLabel(self.groupBox_kimlik)
        self.label_dogum_tarih.setGeometry(QtCore.QRect(540, 150, 191, 51))
        self.label_dogum_tarih.setObjectName("label_dogum_tarih")
        self.comboBox_d_gun = QtWidgets.QComboBox(self.groupBox_kimlik)
        self.comboBox_d_gun.setGeometry(QtCore.QRect(750, 160, 79, 27))
        self.comboBox_d_gun.setObjectName("comboBox_d_gun")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_gun.addItem("")
        self.comboBox_d_ay = QtWidgets.QComboBox(self.groupBox_kimlik)
        self.comboBox_d_ay.setGeometry(QtCore.QRect(840, 160, 79, 27))
        self.comboBox_d_ay.setObjectName("comboBox_d_ay")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_ay.addItem("")
        self.comboBox_d_yil = QtWidgets.QComboBox(self.groupBox_kimlik)
        self.comboBox_d_yil.setGeometry(QtCore.QRect(930, 160, 79, 27))
        self.comboBox_d_yil.setObjectName("comboBox_d_yil")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.addItem("")
        self.comboBox_d_yil.setItemText(11, "")
        self.groupBox_Kurumsal_kimlik = QtWidgets.QGroupBox(OBS_Project)
        self.groupBox_Kurumsal_kimlik.setGeometry(QtCore.QRect(20, 350, 1061, 171))
        self.groupBox_Kurumsal_kimlik.setObjectName("groupBox_Kurumsal_kimlik")
        self.fakulte = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.fakulte.setGeometry(QtCore.QRect(0, 30, 111, 21))
        self.fakulte.setObjectName("fakulte")
        self.bolum = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.bolum.setGeometry(QtCore.QRect(0, 60, 111, 21))
        self.bolum.setObjectName("bolum")
        self.ogretim_tur = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.ogretim_tur.setGeometry(QtCore.QRect(0, 90, 111, 21))
        self.ogretim_tur.setObjectName("ogretim_tur")
        self.ogrenci_tur = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.ogrenci_tur.setGeometry(QtCore.QRect(0, 120, 111, 21))
        self.ogrenci_tur.setObjectName("ogrenci_tur")
        self.ogrenci_id = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.ogrenci_id.setGeometry(QtCore.QRect(540, 30, 111, 21))
        self.ogrenci_id.setObjectName("ogrenci_id")
        self.ogrenci_id_bilgi = QtWidgets.QLineEdit(self.groupBox_Kurumsal_kimlik)
        self.ogrenci_id_bilgi.setGeometry(QtCore.QRect(650, 30, 371, 27))
        self.ogrenci_id_bilgi.setObjectName("ogrenci_id_bilgi")
        self.okul_eposta = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.okul_eposta.setGeometry(QtCore.QRect(540, 60, 111, 21))
        self.okul_eposta.setObjectName("okul_eposta")
        self.okul_eposta_bilgi = QtWidgets.QLineEdit(self.groupBox_Kurumsal_kimlik)
        self.okul_eposta_bilgi.setGeometry(QtCore.QRect(650, 60, 371, 27))
        self.okul_eposta_bilgi.setObjectName("okul_eposta_bilgi")
        self.yatay = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.yatay.setGeometry(QtCore.QRect(810, 90, 111, 21))
        self.yatay.setObjectName("yatay")
        self.dgs = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.dgs.setGeometry(QtCore.QRect(540, 90, 111, 21))
        self.dgs.setObjectName("dgs")
        self.dgs_bilgi = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.dgs_bilgi.setGeometry(QtCore.QRect(650, 90, 151, 27))
        self.dgs_bilgi.setObjectName("dgs_bilgi")
        self.dgs_bilgi.addItem("")
        self.dgs_bilgi.addItem("")
        self.yata_bilgi = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.yata_bilgi.setGeometry(QtCore.QRect(890, 90, 131, 27))
        self.yata_bilgi.setObjectName("yata_bilgi")
        self.yata_bilgi.addItem("")
        self.yata_bilgi.addItem("")
        self.kayit_tarih = QtWidgets.QLabel(self.groupBox_Kurumsal_kimlik)
        self.kayit_tarih.setGeometry(QtCore.QRect(540, 110, 191, 51))
        self.kayit_tarih.setObjectName("kayit_tarih")
        self.kayit_tarih_gun = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.kayit_tarih_gun.setGeometry(QtCore.QRect(750, 120, 79, 27))
        self.kayit_tarih_gun.setObjectName("kayit_tarih_gun")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_gun.addItem("")
        self.kayit_tarih_ay = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.kayit_tarih_ay.setGeometry(QtCore.QRect(840, 120, 79, 27))
        self.kayit_tarih_ay.setObjectName("kayit_tarih_ay")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_ay.addItem("")
        self.kayit_tarih_yil = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.kayit_tarih_yil.setGeometry(QtCore.QRect(930, 120, 79, 27))
        self.kayit_tarih_yil.setObjectName("kayit_tarih_yil")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.addItem("")
        self.kayit_tarih_yil.setItemText(11, "")
        self.fakulte_bilgi = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.fakulte_bilgi.setGeometry(QtCore.QRect(130, 30, 371, 27))
        self.fakulte_bilgi.setObjectName("fakulte_bilgi")
        self.fakulte_bilgi.addItem("")
        self.fakulte_bilgi.addItem("")
        self.fakulte_bilgi.addItem("")
        self.fakulte_bilgi.addItem("")
        self.fakulte_bilgi.addItem("")
        self.fakulte_bilgi.addItem("")
        self.bolum_bilgi = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.bolum_bilgi.setGeometry(QtCore.QRect(130, 60, 371, 27))
        self.bolum_bilgi.setObjectName("bolum_bilgi")
        self.bolum_bilgi.addItem("")
        self.bolum_bilgi.addItem("")
        self.bolum_bilgi.addItem("")
        self.bolum_bilgi.addItem("")
        self.bolum_bilgi.addItem("")
        self.bolum_bilgi.addItem("")
        self.ogretim_tur_bilgi = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.ogretim_tur_bilgi.setGeometry(QtCore.QRect(130, 90, 371, 27))
        self.ogretim_tur_bilgi.setObjectName("ogretim_tur_bilgi")
        self.ogretim_tur_bilgi.addItem("")
        self.ogretim_tur_bilgi.addItem("")
        self.ogretim_tur_bilgi.addItem("")
        self.ogretim_tur_bilgi.addItem("")
        self.ogretim_tur_bilgi.addItem("")
        self.ogrenci_turu = QtWidgets.QComboBox(self.groupBox_Kurumsal_kimlik)
        self.ogrenci_turu.setGeometry(QtCore.QRect(130, 120, 371, 27))
        self.ogrenci_turu.setObjectName("ogrenci_turu")
        self.ogrenci_turu.addItem("")
        self.ogrenci_turu.addItem("")
        self.ogrenci_turu.addItem("")
        self.ogrenci_turu.addItem("")
        self.pushButton_bitti = QtWidgets.QPushButton(OBS_Project)
        self.pushButton_bitti.setGeometry(QtCore.QRect(950, 550, 121, 31))
        self.pushButton_bitti.setObjectName("pushButton_bitti")
        self.label_2 = QtWidgets.QLabel(OBS_Project)
        self.label_2.setGeometry(QtCore.QRect(400, 600, 301, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(OBS_Project)
        self.label_3.setGeometry(QtCore.QRect(860, 20, 191, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/logo_bozok1.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(OBS_Project)
        QtCore.QMetaObject.connectSlotsByName(OBS_Project)

    def retranslateUi(self, OBS_Project):
        _translate = QtCore.QCoreApplication.translate
        OBS_Project.setWindowTitle(_translate("OBS_Project", "Öğrenci Veri Tabanı Ekleme"))
        self.label.setText(_translate("OBS_Project", "Öğrenci Veri Tabanı Ekleme "))
        self.groupBox_kimlik.setTitle(_translate("OBS_Project", "Öğrenci Kimlik Bilgileri"))
        self.isim.setText(_translate("OBS_Project", "İsim"))
        self.lineEdit_adres.setToolTip(_translate("OBS_Project", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.soyisim.setText(_translate("OBS_Project", "Soyisim"))
        self.kimlil_id.setText(_translate("OBS_Project", "Kimlik ID"))
        self.adres.setText(_translate("OBS_Project", "Adres Bilgisi"))
        self.tel_no.setText(_translate("OBS_Project", "Telefon No"))
        self.label_eposta.setText(_translate("OBS_Project", "E-Posta Adresi"))
        self.label_cinsiyet.setText(_translate("OBS_Project", "Cinsiyet"))
        self.comboBox_sehir.setItemText(0, _translate("OBS_Project", "Yozgat"))
        self.comboBox_sehir.setItemText(1, _translate("OBS_Project", "Ankara"))
        self.comboBox_sehir.setItemText(2, _translate("OBS_Project", "Adana"))
        self.comboBox_sehir.setItemText(3, _translate("OBS_Project", "İstanbul"))
        self.comboBox_sehir.setItemText(4, _translate("OBS_Project", "Kayseri"))
        self.comboBox_sehir.setItemText(5, _translate("OBS_Project", "Kırşehir"))
        self.comboBox_sehir.setItemText(6, _translate("OBS_Project", "Sivas"))
        self.comboBox_sehir.setItemText(7, _translate("OBS_Project", "Nevşehir"))
        self.comboBox_sehir.setItemText(8, _translate("OBS_Project", "Niğde"))
        self.comboBox_sehir.setItemText(9, _translate("OBS_Project", "Tokat"))
        self.comboBox_sehir.setItemText(10, _translate("OBS_Project", "Çankırı"))
        self.comboBox_sehir.setItemText(11, _translate("OBS_Project", "Samsun"))
        self.comboBox_sehir.setItemText(12, _translate("OBS_Project", "Trabzon"))
        self.comboBox_sehir.setItemText(13, _translate("OBS_Project", "Kahramanmaraş"))
        self.comboBox_sehir.setItemText(14, _translate("OBS_Project", "Gaziantep"))
        self.label_sehir.setText(_translate("OBS_Project", "Şehir"))
        self.label_uyruk.setText(_translate("OBS_Project", "Uyruk/Ülke"))
        self.comboBox_uyruk.setItemText(0, _translate("OBS_Project", "Türkiye"))
        self.comboBox_uyruk.setItemText(1, _translate("OBS_Project", "Arabistan"))
        self.comboBox_uyruk.setItemText(2, _translate("OBS_Project", "Katar"))
        self.comboBox_uyruk.setItemText(3, _translate("OBS_Project", "Irak"))
        self.comboBox_uyruk.setItemText(4, _translate("OBS_Project", "İran"))
        self.comboBox_uyruk.setItemText(5, _translate("OBS_Project", "Suriye"))
        self.comboBox_uyruk.setItemText(6, _translate("OBS_Project", "Lübnan"))
        self.comboBox_uyruk.setItemText(7, _translate("OBS_Project", "Azerbaycan"))
        self.comboBox_uyruk.setItemText(8, _translate("OBS_Project", "Kıbrıs"))
        self.comboBox_uyruk.setItemText(9, _translate("OBS_Project", "Türkmenistan"))
        self.comboBox_uyruk.setItemText(10, _translate("OBS_Project", "Rusya"))
        self.comboBox_uyruk.setItemText(11, _translate("OBS_Project", "Ukrayna"))
        self.comboBox_uyruk.setItemText(12, _translate("OBS_Project", "Yunanistan"))
        self.comboBox_cinsiyet.setItemText(0, _translate("OBS_Project", "Kadın"))
        self.comboBox_cinsiyet.setItemText(1, _translate("OBS_Project", "Erkek"))
        self.label_dogum_tarih.setText(_translate("OBS_Project", "<html><head/><body><p>Doğum Tarihi :GG/AA/YYYY</p></body></html>"))
        self.comboBox_d_gun.setItemText(0, _translate("OBS_Project", "1"))
        self.comboBox_d_gun.setItemText(1, _translate("OBS_Project", "2"))
        self.comboBox_d_gun.setItemText(2, _translate("OBS_Project", "3"))
        self.comboBox_d_gun.setItemText(3, _translate("OBS_Project", "4"))
        self.comboBox_d_gun.setItemText(4, _translate("OBS_Project", "5"))
        self.comboBox_d_gun.setItemText(5, _translate("OBS_Project", "6"))
        self.comboBox_d_gun.setItemText(6, _translate("OBS_Project", "7"))
        self.comboBox_d_gun.setItemText(7, _translate("OBS_Project", "8"))
        self.comboBox_d_gun.setItemText(8, _translate("OBS_Project", "9"))
        self.comboBox_d_gun.setItemText(9, _translate("OBS_Project", "10"))
        self.comboBox_d_gun.setItemText(10, _translate("OBS_Project", "11"))
        self.comboBox_d_gun.setItemText(11, _translate("OBS_Project", "12"))
        self.comboBox_d_gun.setItemText(12, _translate("OBS_Project", "13"))
        self.comboBox_d_gun.setItemText(13, _translate("OBS_Project", "14"))
        self.comboBox_d_gun.setItemText(14, _translate("OBS_Project", "15"))
        self.comboBox_d_gun.setItemText(15, _translate("OBS_Project", "16"))
        self.comboBox_d_gun.setItemText(16, _translate("OBS_Project", "17"))
        self.comboBox_d_gun.setItemText(17, _translate("OBS_Project", "18"))
        self.comboBox_d_gun.setItemText(18, _translate("OBS_Project", "19"))
        self.comboBox_d_gun.setItemText(19, _translate("OBS_Project", "20"))
        self.comboBox_d_gun.setItemText(20, _translate("OBS_Project", "21"))
        self.comboBox_d_gun.setItemText(21, _translate("OBS_Project", "22"))
        self.comboBox_d_gun.setItemText(22, _translate("OBS_Project", "23"))
        self.comboBox_d_gun.setItemText(23, _translate("OBS_Project", "24"))
        self.comboBox_d_gun.setItemText(24, _translate("OBS_Project", "25"))
        self.comboBox_d_gun.setItemText(25, _translate("OBS_Project", "26"))
        self.comboBox_d_gun.setItemText(26, _translate("OBS_Project", "27"))
        self.comboBox_d_gun.setItemText(27, _translate("OBS_Project", "28"))
        self.comboBox_d_gun.setItemText(28, _translate("OBS_Project", "29"))
        self.comboBox_d_gun.setItemText(29, _translate("OBS_Project", "30"))
        self.comboBox_d_gun.setItemText(30, _translate("OBS_Project", "31"))
        self.comboBox_d_ay.setItemText(0, _translate("OBS_Project", "1"))
        self.comboBox_d_ay.setItemText(1, _translate("OBS_Project", "2"))
        self.comboBox_d_ay.setItemText(2, _translate("OBS_Project", "3"))
        self.comboBox_d_ay.setItemText(3, _translate("OBS_Project", "4"))
        self.comboBox_d_ay.setItemText(4, _translate("OBS_Project", "5"))
        self.comboBox_d_ay.setItemText(5, _translate("OBS_Project", "6"))
        self.comboBox_d_ay.setItemText(6, _translate("OBS_Project", "7"))
        self.comboBox_d_ay.setItemText(7, _translate("OBS_Project", "8"))
        self.comboBox_d_ay.setItemText(8, _translate("OBS_Project", "9"))
        self.comboBox_d_ay.setItemText(9, _translate("OBS_Project", "10"))
        self.comboBox_d_ay.setItemText(10, _translate("OBS_Project", "11"))
        self.comboBox_d_ay.setItemText(11, _translate("OBS_Project", "12"))
        self.comboBox_d_yil.setItemText(0, _translate("OBS_Project", "2000"))
        self.comboBox_d_yil.setItemText(1, _translate("OBS_Project", "2001"))
        self.comboBox_d_yil.setItemText(2, _translate("OBS_Project", "2002"))
        self.comboBox_d_yil.setItemText(3, _translate("OBS_Project", "2003"))
        self.comboBox_d_yil.setItemText(4, _translate("OBS_Project", "2004"))
        self.comboBox_d_yil.setItemText(5, _translate("OBS_Project", "2005"))
        self.comboBox_d_yil.setItemText(6, _translate("OBS_Project", "2006"))
        self.comboBox_d_yil.setItemText(7, _translate("OBS_Project", "2007"))
        self.comboBox_d_yil.setItemText(8, _translate("OBS_Project", "2008"))
        self.comboBox_d_yil.setItemText(9, _translate("OBS_Project", "2009"))
        self.comboBox_d_yil.setItemText(10, _translate("OBS_Project", "2010"))
        self.groupBox_Kurumsal_kimlik.setTitle(_translate("OBS_Project", "Öğrenci Kurumsal  Kimlik Bilgileri"))
        self.fakulte.setText(_translate("OBS_Project", "Fakülte"))
        self.bolum.setText(_translate("OBS_Project", "Bölüm"))
        self.ogretim_tur.setText(_translate("OBS_Project", "Öğretim Türü"))
        self.ogrenci_tur.setText(_translate("OBS_Project", "Öğrenci Türü"))
        self.ogrenci_id.setText(_translate("OBS_Project", "Öğrenci ID"))
        self.okul_eposta.setText(_translate("OBS_Project", "Okul E-Posta"))
        self.yatay.setText(_translate("OBS_Project", "Yatay Geçiş"))
        self.dgs.setText(_translate("OBS_Project", "DGS"))
        self.dgs_bilgi.setItemText(0, _translate("OBS_Project", "Evet"))
        self.dgs_bilgi.setItemText(1, _translate("OBS_Project", "Hayır"))
        self.yata_bilgi.setItemText(0, _translate("OBS_Project", "Evet"))
        self.yata_bilgi.setItemText(1, _translate("OBS_Project", "Hayır"))
        self.kayit_tarih.setText(_translate("OBS_Project", "<html><head/><body><p>Kayıt Tarihi :GG/AA/YYYY</p></body></html>"))
        self.kayit_tarih_gun.setItemText(0, _translate("OBS_Project", "1"))
        self.kayit_tarih_gun.setItemText(1, _translate("OBS_Project", "2"))
        self.kayit_tarih_gun.setItemText(2, _translate("OBS_Project", "3"))
        self.kayit_tarih_gun.setItemText(3, _translate("OBS_Project", "4"))
        self.kayit_tarih_gun.setItemText(4, _translate("OBS_Project", "5"))
        self.kayit_tarih_gun.setItemText(5, _translate("OBS_Project", "6"))
        self.kayit_tarih_gun.setItemText(6, _translate("OBS_Project", "7"))
        self.kayit_tarih_gun.setItemText(7, _translate("OBS_Project", "8"))
        self.kayit_tarih_gun.setItemText(8, _translate("OBS_Project", "9"))
        self.kayit_tarih_gun.setItemText(9, _translate("OBS_Project", "10"))
        self.kayit_tarih_gun.setItemText(10, _translate("OBS_Project", "11"))
        self.kayit_tarih_gun.setItemText(11, _translate("OBS_Project", "12"))
        self.kayit_tarih_gun.setItemText(12, _translate("OBS_Project", "13"))
        self.kayit_tarih_gun.setItemText(13, _translate("OBS_Project", "14"))
        self.kayit_tarih_gun.setItemText(14, _translate("OBS_Project", "15"))
        self.kayit_tarih_gun.setItemText(15, _translate("OBS_Project", "16"))
        self.kayit_tarih_gun.setItemText(16, _translate("OBS_Project", "17"))
        self.kayit_tarih_gun.setItemText(17, _translate("OBS_Project", "18"))
        self.kayit_tarih_gun.setItemText(18, _translate("OBS_Project", "19"))
        self.kayit_tarih_gun.setItemText(19, _translate("OBS_Project", "20"))
        self.kayit_tarih_gun.setItemText(20, _translate("OBS_Project", "21"))
        self.kayit_tarih_gun.setItemText(21, _translate("OBS_Project", "22"))
        self.kayit_tarih_gun.setItemText(22, _translate("OBS_Project", "23"))
        self.kayit_tarih_gun.setItemText(23, _translate("OBS_Project", "24"))
        self.kayit_tarih_gun.setItemText(24, _translate("OBS_Project", "25"))
        self.kayit_tarih_gun.setItemText(25, _translate("OBS_Project", "26"))
        self.kayit_tarih_gun.setItemText(26, _translate("OBS_Project", "27"))
        self.kayit_tarih_gun.setItemText(27, _translate("OBS_Project", "28"))
        self.kayit_tarih_gun.setItemText(28, _translate("OBS_Project", "29"))
        self.kayit_tarih_gun.setItemText(29, _translate("OBS_Project", "30"))
        self.kayit_tarih_gun.setItemText(30, _translate("OBS_Project", "31"))
        self.kayit_tarih_ay.setItemText(0, _translate("OBS_Project", "1"))
        self.kayit_tarih_ay.setItemText(1, _translate("OBS_Project", "2"))
        self.kayit_tarih_ay.setItemText(2, _translate("OBS_Project", "3"))
        self.kayit_tarih_ay.setItemText(3, _translate("OBS_Project", "4"))
        self.kayit_tarih_ay.setItemText(4, _translate("OBS_Project", "5"))
        self.kayit_tarih_ay.setItemText(5, _translate("OBS_Project", "6"))
        self.kayit_tarih_ay.setItemText(6, _translate("OBS_Project", "7"))
        self.kayit_tarih_ay.setItemText(7, _translate("OBS_Project", "8"))
        self.kayit_tarih_ay.setItemText(8, _translate("OBS_Project", "9"))
        self.kayit_tarih_ay.setItemText(9, _translate("OBS_Project", "10"))
        self.kayit_tarih_ay.setItemText(10, _translate("OBS_Project", "11"))
        self.kayit_tarih_ay.setItemText(11, _translate("OBS_Project", "12"))
        self.kayit_tarih_yil.setItemText(0, _translate("OBS_Project", "2000"))
        self.kayit_tarih_yil.setItemText(1, _translate("OBS_Project", "2001"))
        self.kayit_tarih_yil.setItemText(2, _translate("OBS_Project", "2002"))
        self.kayit_tarih_yil.setItemText(3, _translate("OBS_Project", "2003"))
        self.kayit_tarih_yil.setItemText(4, _translate("OBS_Project", "2004"))
        self.kayit_tarih_yil.setItemText(5, _translate("OBS_Project", "2005"))
        self.kayit_tarih_yil.setItemText(6, _translate("OBS_Project", "2006"))
        self.kayit_tarih_yil.setItemText(7, _translate("OBS_Project", "2007"))
        self.kayit_tarih_yil.setItemText(8, _translate("OBS_Project", "2008"))
        self.kayit_tarih_yil.setItemText(9, _translate("OBS_Project", "2009"))
        self.kayit_tarih_yil.setItemText(10, _translate("OBS_Project", "2010"))
        self.fakulte_bilgi.setItemText(0, _translate("OBS_Project", "Mimarlık - Mühendislik Fakültesi"))
        self.fakulte_bilgi.setItemText(1, _translate("OBS_Project", "Sağlık Bilimleri Fakültesi"))
        self.fakulte_bilgi.setItemText(2, _translate("OBS_Project", "Hukuk Fakültesi"))
        self.fakulte_bilgi.setItemText(3, _translate("OBS_Project", "Tıp Fakültesi"))
        self.fakulte_bilgi.setItemText(4, _translate("OBS_Project", "İletişim Fakültesi"))
        self.fakulte_bilgi.setItemText(5, _translate("OBS_Project", "İlahiyat"))
        self.bolum_bilgi.setItemText(0, _translate("OBS_Project", "Bilgiayar Mühendisliği"))
        self.bolum_bilgi.setItemText(1, _translate("OBS_Project", "Elektrik - Elektronik Mühendisliği"))
        self.bolum_bilgi.setItemText(2, _translate("OBS_Project", "Makine Mühendisliği"))
        self.bolum_bilgi.setItemText(3, _translate("OBS_Project", "Mimarlık"))
        self.bolum_bilgi.setItemText(4, _translate("OBS_Project", "Şehir Bölge Planlama"))
        self.bolum_bilgi.setItemText(5, _translate("OBS_Project", "Gazetecilik"))
        self.ogretim_tur_bilgi.setItemText(0, _translate("OBS_Project", "Birinci Öğretim"))
        self.ogretim_tur_bilgi.setItemText(1, _translate("OBS_Project", "İkinci Öğretim"))
        self.ogretim_tur_bilgi.setItemText(2, _translate("OBS_Project", "Uzaktan Öğretim"))
        self.ogretim_tur_bilgi.setItemText(3, _translate("OBS_Project", "Yüksek Lisans"))
        self.ogretim_tur_bilgi.setItemText(4, _translate("OBS_Project", "Doktora"))
        self.ogrenci_turu.setItemText(0, _translate("OBS_Project", "Lisans"))
        self.ogrenci_turu.setItemText(1, _translate("OBS_Project", "Ön Lisans"))
        self.ogrenci_turu.setItemText(2, _translate("OBS_Project", "Yükesek Lisans"))
        self.ogrenci_turu.setItemText(3, _translate("OBS_Project", "Doktora"))

        self.pushButton_bitti.setText(_translate("OBS_Project", "İşlem Tamamla"))
        self.pushButton_bitti.clicked.connect(self.kaydet)


        self.label_2.setText(_translate("OBS_Project", "<html><head/><body><p>Denizhan Şahin   -  <a href=\"www.denizhansahin.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.denizhansahin.com</span></a></p></body></html>"))

    def kaydet(self):
        print("merhaba")
        #ODBC - MS SQL SERVER
        connection = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=OgrenciVeriTabani;UID=sa;PWD=12345Deniz')
        cursor = connection.cursor()

        #SQL LITE 3
        vt = sqlite3.connect("universite.sqlite3")
        im = vt.cursor()
        
        a = int(self.ogrenci_id_bilgi.text())
        print(a)
        print(type(a))

        b = int(self.lineEdit_kimlik_id.text())
        print(b)
        print(type(b))

        c = str(self.lineEdit_isim.text())
        print(c)
        print(type(c))

        d = str(self.lineEdit_soyisim.text())
        print(d)
        print(type(d))

        e = str(self.lineEdit_adres.text())
        print(e)
        print(type(e))

        f = int(self.lineEdit_tel_no.text())
        print(f)
        print(type(f))

        g = str(self.lineEdit_eposta.text())
        print(g)
        print(type(g))
        
        h = (self.comboBox_uyruk.currentText())
        print(h)
        print(type(h))       

        i = (self.comboBox_cinsiyet.currentText())
        print(i)
        print(type(i))

        k = (self.comboBox_sehir.currentText())
        print(k)
        print(type(k))
        
        j = int(self.comboBox_d_gun.currentText())
        print(j)
        print(type(j))

        m = int(self.comboBox_d_ay.currentText())
        print(m)
        print(type(m))

        n = int(self.comboBox_d_yil.currentText())
        print(n)
        print(type(n))

        o = (self.fakulte_bilgi.currentText())
        print(o)
        print(type(o))

        p = (self.bolum_bilgi.currentText())
        print(p)
        print(type(p))

        r = (self.ogretim_tur_bilgi.currentText())
        print(r)
        print(type(r))

        s = (self.ogrenci_turu.currentText())
        print(s)
        print(type(s))

        t = str(self.okul_eposta_bilgi.text())
        print(t)
        print(type(t))

        u = (self.dgs_bilgi.currentText())
        print(u)
        print(type(u))

        v = (self.yata_bilgi.currentText())
        print(v)
        print(type(v))

        y = int(self.kayit_tarih_gun.currentText())
        print(y)
        print(type(y))

        yy = int(self.kayit_tarih_ay.currentText())
        print(yy)
        print(type(yy))

        z = int(self.kayit_tarih_yil.currentText())
        print(z)
        print(type(z))

        veriler = (a,b,c,d,e,f,g,h,i,k,j,m,n,o,p,r,s,t,u,v,y,yy,z)
        print(veriler)
        print(len(veriler))

        #SQL LITE3
        try:
            tablo_sql = """CREATE TABLE ogrenci_bilgileri (OgrenciID INTEGER PRIMARY KEY AUTOINCREMENT,KimlikID INTEGER, Isim VARCHAR, Soyisim VARCHAR,Addres VARCHAR,TelNo INTEGER,EPosta VARCHAR,Uyruk VARCHAR,Cinsiyet VARCHAR, Sehir VARCHAR,DogumGun INTEGER,DogumAy INTEGER,DogumYil INTEGER,Fakulte INTEGER,Bolum INTEGER,OgretimTuru VARCHAR,OgrenciTuru VARCHAR,OkulEposta VARCHAR, DGS VARCHAR, YatayGecis VARCHAR, KayitGun INTEGER,KayitAy INTEGER,KayitYil INTEGER)"""
            im.execute(tablo_sql)
        except:
            print("islem")
        #SQL LITE3
        veriler_db = [(a,b,c,d,e,f,g,h,i,k,j,m,n,o,p,r,s,t,u,v,y,yy,z)]
        try:

           #tablo göster
            tablo_sql_goster = 'SELECT * FROM ogrenci_bilgileri'
            im.execute(tablo_sql_goster)
            deger=im.fetchall()
            print(deger,"\n")
            vt.commit()

            for veri in veriler_db:
                im.execute("""INSERT INTO ogrenci_bilgileri VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", veri)
                vt.commit()
        except:
            print("islem2")

        #MS-SQL SEERVER
        komut = 'INSERT INTO [OgrenciVeriTabani].[dbo].[OgrenciTablosu](OgrenciID,KimlikID,Isim,Soyisim,Addres,TelNo,EPosta,Uyruk,Cinsiyet,Sehir,DogumGun,DogumAy,DogumYil,Fakulte,Bolum,OgretimTuru,OgrenciTuru,OkulEposta,DGS,YatayGecis,KayitGun,KayitAy,KayitYil) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        try:
            cursor.execute(komut,veriler)
            connection.commit()
        except:
            cursor.execute(komut,veriler)
            connection.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OBS_Project = QtWidgets.QWidget()
    ui = Ui_OBS_Project()
    ui.setupUi(OBS_Project)
    OBS_Project.show()
    sys.exit(app.exec_())
