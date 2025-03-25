import numpy as np
import pandas as pd

# struktur data
data_siswa = {
    "Nama": ["Andi", "Budi", "Cici", "Dedi"],
    "Matematika": [80, 75, 90, 65],
    "Fisika": [70, 85, 80, 75],
    "Kimia": [85, 70, 75, 80]
}

df = pd.DataFrame(data_siswa)

# untuk menampilkan data
def tampilkan_data():
    print("\n=== DATA NILAI SISWA ===")
    print(df)

# fungsi untuk statistik dasar (pake numpy)
def hitung_statistik():
    print("\n=== STATISTIK NILAI ===")
    for pelajaran in ["Matematika", "Fisika", "Kimia"]:
        nilai = df[pelajaran].values
        print(
            f"{pelajaran}: Rata-rata = {np.mean(nilai):.1f}, "
            f"Max = {np.max(nilai)}, Min = {np.min(nilai)}"
        )

# untuk menambahkan siswa baru
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    matematika = int(input("Nilai Matematika: "))
    fisika = int(input("Nilai Fisika: "))
    kimia = int(input("Nilai Kimia: "))
    
    # tambah data baru ke dataframe
    global df
    df.loc[len(df)] = [nama, matematika, fisika, kimia]
    print(f"\nSiswa {nama} berhasil ditambahkan!")

# untuk mencari siswa (struktur kontrol)
def cari_siswa():
    nama_cari = input("\nCari nama siswa: ")
    hasil = df[df["Nama"].str.contains(nama_cari, case=False)]
    
    if not hasil.empty:
        print("\nHasil Pencarian:")
        print(hasil)
    else:
        print("Siswa tidak ditemukan!")

while True:
    print("\n=== MENU ANALISIS DATA ===")
    print("1. Tampilkan Data Siswa")
    print("2. Tambah Siswa Baru")
    print("3. Cari Siswa")
    print("4. Lihat Statistik Nilai")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_siswa()
    elif pilihan == "3":
        cari_siswa()
    elif pilihan == "4":
        hitung_statistik()
    elif pilihan == "5":
        print("Program selesai, bye!")
        break
    else:
        print("Pilihan tidak valid!")