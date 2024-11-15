peminjaman_list = []

def tambah_peminjaman(peminjaman_list):
    print("\n=== Tambah Peminjaman ===")
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")

    # Menyimpan data peminjaman dalam bentuk tuple
    peminjaman = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

def tampilkan_peminjaman(peminjaman_list):
    print("\n=== Data Peminjaman Buku ===")
    if not peminjaman_list:
        print("Tidak ada data peminjaman.")
    else:
        for peminjaman in peminjaman_list:
            print(f"ID Peminjaman: {peminjaman[0]}, Nama Peminjam: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal Peminjaman: {peminjaman[3]}")

def update_peminjaman(peminjaman_list):
    print("\n=== Update Peminjaman ===")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diupdate: ")
    
    # Mencari peminjaman berdasarkan ID
    for i in range(len(peminjaman_list)):
        if peminjaman_list[i][0] == id_peminjaman:
            print("Data peminjaman ditemukan.")
            nama_peminjam = input("Masukkan Nama Peminjam baru: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman baru (YYYY-MM-DD): ")

            # Memperbarui data peminjaman
            peminjaman_list[i] = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            print("Data peminjaman berhasil diupdate.")
            return  # Keluar dari fungsi setelah update
    print("Data peminjaman tidak ditemukan.")

def hapus_peminjaman(peminjaman_list):
    print("\n=== Hapus Peminjaman ===")
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    
    # Mencari peminjaman berdasarkan ID
    for i in range(len(peminjaman_list)):
        if peminjaman_list[i][0] == id_peminjaman:
            del peminjaman_list[i]
            print("Data peminjaman berhasil dihapus.")
            return  # Keluar dari fungsi setelah hapus
    print("Data peminjaman tidak ditemukan.")

# Loop utama untuk menjalankan program
while True:
    print("\n=== Sistem Peminjaman Buku Perpustakaan ===")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilihan = input("Pilih opsi (1-5): ")

    if pilihan == '1':
        tambah_peminjaman(peminjaman_list)

    elif pilihan == '2':
        tampilkan_peminjaman(peminjaman_list)

    elif pilihan == '3':
        update_peminjaman(peminjaman_list)

    elif pilihan == '4':
        hapus_peminjaman(peminjaman_list)

    elif pilihan == '5':
        print("Keluar dari program.")
        break

    else:
        print("Opsi tidak valid. Silakan coba lagi.")