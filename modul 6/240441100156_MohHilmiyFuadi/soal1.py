karyawan_list = []

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan():
    for i in range(5):
        print(f"Input data karyawan ke-{i + 1}:")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        # Menyimpan data karyawan sebagai tuple
        karyawan = (nip, nama, alamat, departemen, jabatan)
        karyawan_list.append(karyawan)

# Fungsi untuk mencari karyawan berdasarkan atribut
def cari_karyawan(atribut, nilai):
    hasil_cari = []
    for karyawan in karyawan_list:
        if karyawan[atribut].lower() == nilai.lower():
            hasil_cari.append(karyawan)
    return hasil_cari

# Fungsi untuk menampilkan hasil pencarian
def tampilkan_hasil(hasil):
    if hasil:
        print("Data Karyawan yang ditemukan:")
        for karyawan in hasil:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
    else:
        print("Tidak ada karyawan yang ditemukan.")

# Menjalankan program
tambah_karyawan()  # Tambah data karyawan

while True:
    print("\nPencarian Karyawan")
    print("Pilih atribut untuk mencari:")
    print("0: NIP")
    print("1: Nama")
    print("2: Alamat")
    print("3: Departemen")
    print("4: Jabatan")

    atribut = input("Masukkan nomor atribut yang ingin dicari (0-4): ")

    # Validasi atribut
    if atribut not in ['0', '1', '2', '3', '4']:
        print("Atribut tidak valid. Silakan coba lagi.")
        continue

    nilai = input("Masukkan nilai untuk atribut yang dipilih: ")
    hasil = cari_karyawan(int(atribut), nilai)

    # Menampilkan hasil pencarian
    tampilkan_hasil(hasil)

    mencarilagi = input("\nApakah Anda ingin mencari lagi? (y/n): ")
    if mencarilagi.lower() != 'y':
        break