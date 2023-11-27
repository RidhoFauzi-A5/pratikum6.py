# Dictionary
kontak = {"Ari": "081267888", "Dina": "087677776"}

# Menampilkan Kontak Ari
pairs = list(kontak.items())
print(pairs[0], "\n")

# Menambahkan Kontak Riko dan Merubah Kontak Dina
kontak["Riko"] = "087654544"
kontak["Dina"] = "088999776"

# Menampilkan Semua Nama dan Nomor
print(kontak.keys())
print(kontak.values(), "\n")

# Menampilkan semua daftar Nama dan Nomor
pairs = list(kontak.items())
print(pairs[0:3], "\n")

# Menghapus Kontak Dina
del kontak["Dina"]
pairs = list(kontak.items())
print(pairs[0:3], "\n")