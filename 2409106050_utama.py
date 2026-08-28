# !/usr/bin/env python3
# Decoder : UTF-8

'''
Nama File : 2409106050_utama.py
Tujuan    : Program ini adalah program utama untuk menjalankan manajemen jaringan kantor cabang virtual
Nama pembuat : Ananda Daffa Harahap 
'''

import importlib

modul = importlib.import_module('2409106050_modul')
buat_id_perangkat = modul.buat_id_perangkat

# BAGIAN A : Identitas Cabang dan Pembuatan ID Perangkat
nim = "2409106050"
nama = "Ananda Daffa Harahap"
kode_cabang = nim[-3:]

# Membuat ID
id_router = buat_id_perangkat('RTR', kode_cabang, 1)
id_switch = buat_id_perangkat('SW', kode_cabang, 1)
id_firewall = buat_id_perangkat('FW', kode_cabang, 1)

# Print ID Perangkat
print(f"ID Router: {id_router}")
print(f"ID Switch: {id_switch}")
print(f"ID Firewall: {id_firewall}")

# BAGIAN B : Pengecekan Status Perangkat
def cek_status(nama_perangkat, status):
    if status == 'up':
        print(f"Status dari perangkat {nama_perangkat} : up")
    else:
        print(f"Status dari perangkat {nama_perangkat} : down")

# Variabel Status Perangkat
status_router = 'up'
status_switch = 'down'
status_firewall = 'up'

cek_status(f"Router {id_router}", status_router)
cek_status(f"Switch {id_switch}", status_switch)
cek_status(f"Firewall {id_firewall}", status_firewall)
print()

# BAGIAN C : Function Klasifikasi Utilisasi Interface
def klasifikasi_utilisasi(nama_interface, in_uti, out_uti):
    rata_rata = (in_uti + out_uti) / 2
    if rata_rata < 50:
        klasifikasi = "NORMAL"
    elif 50 <= rata_rata < 80:
        klasifikasi = "WASPADA"
    else:
        klasifikasi = "KRITIS"

    print(f"Interface: {nama_interface:<12} | Traffic In: {in_uti:>2}% | Traffic Out: {out_uti:>2}% | Rata-rata: {rata_rata:>4.1f}% : [{klasifikasi}]")
    return klasifikasi

# 2409106050
# 1. Level KRITIS (> 80) -> rata-rata: (91 + 91)/2 = 91.0%
klasifikasi_utilisasi("gi0/0 (RTR)", in_uti=91, out_uti=91)

# 2. Level WASPADA (50 - 80) -> rata-rata: (50 + 60)/2 = 55.0%
klasifikasi_utilisasi("fa0/1 (SW)", in_uti=50, out_uti=60)

# 3. Level NORMAL (< 50) -> rata-rata: (24 + 0)/2 = 12.0%
klasifikasi_utilisasi("eth0 (FW)", in_uti=24, out_uti=0)
print()

# BAGIAN D : Misah Modul jadi ke file 2409106050_modul.py

# BAGIAN E : Class Perangkat Jaringan dan Laporan Akhir
class PerangkatJaringan:
    def tampilkan_laporan(self, nama_perangkat, status):
        if status == 'up':
            print(f"Status dari perangkat {nama_perangkat} : up")
        else:
            print(f"Status dari perangkat {nama_perangkat} : down")
        print(f"{nama_perangkat} : {status}")

cabang = PerangkatJaringan()
cabang.tampilkan_laporan(f"Router {id_router}", status_router)
cabang.tampilkan_laporan(f"Switch {id_switch}", status_switch)
cabang.tampilkan_laporan(f"Firewall {id_firewall}", status_firewall)

# Analisis Jawaban:
# 1. Bagian A: Membuat ID Perangkat
# 2. Bagian B: Pengecekan Status Perangkat
# 3. Bagian C: Klasifikasi Utilisasi Interface
# 4. Bagian D: Pemisahan Modul
# 5. Bagian E: Class Perangkat Jaringan dan Laporan Akhir

# Dengan adanya pemisahan modul membuat kita dapat menerapkan prinsip DRY (Don't Repeat Yourself) atau Reusability (Penggunaan ulang kode) 
# dan memudahkan pemeliharaan kode.
# Penerapan class PerangkatJaringan pada Bagian E juga membuat kode lebih terstruktur dan mudah dikembangkan karena menerapkan sistem CLASS