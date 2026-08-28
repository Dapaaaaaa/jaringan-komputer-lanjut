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
        print(f"Status dari perangkat {nama_perangkat} : UP")
    else:
        print(f"Status dari perangkat {nama_perangkat} : DOWN")

# Variabel Status Perangkat
status_router = 'UP'
status_switch = 'DOWN'
status_firewall = 'UP'

cek_status(f"Router {id_router}", status_router)
cek_status(f"Switch {id_switch}", status_switch)
cek_status(f"Firewall {id_firewall}", status_firewall)
print()