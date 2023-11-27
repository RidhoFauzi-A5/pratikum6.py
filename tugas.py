# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)
    return nilai_akhir

# Dictionary kosong untuk menyimpan data siswa
data_siswa = {}

# Fungsi untuk menambahkan data siswa
def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_siswa[nama] = {
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    }
    print(f"Data untuk {nama} berhasil ditambahkan!")

# Fungsi untuk menampilkan data siswa
def tampilkan_data():
    for nama, data in data_siswa.items():
        print(f"Nama: {nama}")
        for key, value in data.items():
            print(f"{key}: {value}")
        print()  # Memberikan baris kosong antara setiap data siswa

# Fungsi untuk mencari data siswa berdasarkan nama
def cari_data():
    nama = input("Masukkan nama mahasiswa yang ingin dicari: ")
    if nama in data_siswa:
        print(f"Data siswa {nama}:")
        data = data_siswa[nama]
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

# Fungsi untuk mengubah data siswa
def ubah_data():
    nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
    if nama in data_siswa:
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_siswa[nama] = {
            'Tugas': tugas,
            'UTS': uts,
            'UAS': uas,
            'Nilai Akhir': nilai_akhir
        }
        print(f"Data untuk {nama} berhasil diubah!")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

# Fungsi untuk menghapus data siswa
def hapus_data():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    if nama in data_siswa:
        del data_siswa[nama]
        print(f"Data untuk {nama} berhasil dihapus!")
    else:
        print(f"Data untuk {nama} tidak ditemukan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '6':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
