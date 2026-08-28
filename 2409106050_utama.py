# !/usr/bin/env python3
# Decoder : UTF-8

'''
Nama File : 2409106050_utama.py
Tujuan    : Program ini adalah program utama untuk menjalankan manajemen jaringan kantor cabang virtual
Nama pembuat : Ananda Daffa Harahap 
'''
# Alasan menggunakan importlib karena modul gabisa di panggil kalau menggunakan nama file awalan angka
import importlib

# Kita buat variabel untuk memanggil modul dari file 2409106050_modul.py
modul = importlib.import_module('2409106050_modul')
# ini adalah contoh pemanggilan fungsi untuk buat_id_perangkat dari modul
buat_id_perangkat = modul.buat_id_perangkat

