# a. Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
klub_basket = {"arik", "Hilmy", "Cindy", "Dina", "Eko"}
klub_renang = {"Hilmy", "Cindy", "Fani", "Gina"}

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:")
print(siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_basket = klub_basket - klub_renang
siswa_hanya_renang = klub_renang - klub_basket
siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)

print("Siswa yang hanya mengikuti satu klub:")
print(siswa_hanya_satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
semua_siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu klub:")
print(semua_siswa_unik)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
jumlah_siswa_unik = len(semua_siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)