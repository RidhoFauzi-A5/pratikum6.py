# latihan 

# Menambahkan Kontak Riko dan Merubah Kontak Dina
kontak["Riko"] = "087654544"
kontak["Dina"] = "088999776"

# Menampilkan Semua Nama dan Nomor
print(kontak.keys())
print(kontak.values())

# Menampilkan semua daftar Nama dan Nomor
pairs = list(kontak.items())
print(pairs[0:3])

# Menghapus Kontak Dina
del kontak["Dina"]
pairs = list(kontak.items())
print(pairs[0:3])

![Gambar](Screenshot (38).jpg) 

