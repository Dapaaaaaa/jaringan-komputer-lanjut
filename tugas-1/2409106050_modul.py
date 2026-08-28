# !/usr/bin/env python3
# Decoder : UTF-8

'''
Nama File : 2409106050_modul.py
Tujuan    : Program ini adalah module untuk network automation pembuatan ID untuk perangkat pada cabang kantor virtual
Nama pembuat : Ananda Daffa Harahap 
'''

def buat_id_perangkat(jenis, kode_cabang, nomor):
    id_perangkat = f"{jenis}-{kode_cabang}-{nomor:02d}"
    return id_perangkat