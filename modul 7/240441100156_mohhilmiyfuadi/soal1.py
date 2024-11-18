alat_kesehatan = {
    "alat pengukur tekanan darah": 2,
    "termometer": 3,
    "stetoskop": 4,
    "alat inhaler": 0
}

# Proses pengembalian setelah seminggu
alat_kesehatan["alat pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Proses penukaran
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["alat inhaler"] += 2

# Menampilkan hasil akhir dengan format string yang berbeda
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah}")  