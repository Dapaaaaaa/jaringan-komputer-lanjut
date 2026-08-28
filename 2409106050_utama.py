# !/usr/bin/env python3
# Decoder : UTF-8

'''
Nama File : 2409106050_utama.py
Tujuan    : Program ini adalah program utama untuk menjalankan manajemen jaringan kantor cabang virtual
Nama pembuat : Ananda Daffa Harahap 
'''
# Membuat modul sesuai perintah soal A
def buat_id_perangkat(jenis, kode_cabang, nomor):
    id_perangkat = f"{jenis}-{kode_cabang}-{nomor:02d}"
    return id_perangkat

# Alasan menggunakan importlib karena modul gabisa di panggil kalau menggunakan nama file awalan angka
import importlib

# Kita buat variabel untuk memanggil modul dari file 2409106050_modul.py
modul = importlib.import_module('2409106050_modul')
# ini adalah contoh pemanggilan fungsi untuk buat_id_perangkat dari modul
buat_id_perangkat = modul.buat_id_perangkat

# BAGIAN A : Identitas Cabang dan Pembuatan ID Perangkat
nim = "2409106050"
nama = "Ananda Daffa Harahap"
kode_cabang = nim[3:]

# Membuat ID
id_router = buat_id_perangkat('RTR', kode_cabang, 1)
id_switch = buat_id_perangkat('SW', kode_cabang, 1)
id_firewall = buat_id_perangkat('FW', kode_cabang, 1)

