def tampilkan_menu_prioritas():
    print("Pilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")

def tambah_barang(barang_list):
    # Meminta input dari pengguna
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")

    # Menampilkan menu prioritas dan meminta input
    tampilkan_menu_prioritas()
    pilihan = input("Masukkan pilihan (1/2/3): ")

    # Menentukan prioritas berdasarkan pilihan
    if pilihan == '1':
        prioritas = 'darurat'
    elif pilihan == '2':
        prioritas = 'biasa'
    elif pilihan == '3':
        prioritas = 'non-darurat'
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")
        return

    # Menyimpan barang dalam tuple
    barang = (id_barang, nama_barang, prioritas)

    # Menambahkan barang ke dalam list berdasarkan prioritas
    if prioritas == 'darurat':
        barang_list.insert(0, barang)  # Tambahkan di awal list
    elif prioritas == 'biasa':
        # Tambahkan di tengah-tengah list
        for i in range(len(barang_list)):
            if barang_list[i][2] == 'non-darurat':
                barang_list.insert(i, barang)
                break
        else:
            barang_list.append(barang)  # Jika tidak ada barang Non-Darurat, tambahkan di akhir
    else:  # prioritas 'non-darurat'
        barang_list.append(barang)  # Tambahkan di akhir list

    print("Barang berhasil ditambahkan.")

def tampilkan_barang(barang_list):
    # Menampilkan daftar barang
    if not barang_list:
        print("Tidak ada barang yang terdaftar.")
        return

    print("\nDaftar Barang:")
    for id_barang, nama_barang, prioritas in barang_list:
        print(f"ID Barang: {id_barang}, Nama Barang: {nama_barang}, Prioritas: {prioritas}")

# Daftar barang kosong
barang_list = []

# Loop untuk menambah barang
while True:
    tambah_barang(barang_list)  # Memanggil fungsi untuk menambah barang
    tampilkan_barang(barang_list)  # Menampilkan daftar barang

    lagi = input("Apakah Anda ingin menambah barang lagi? (ya/tidak): ").strip().lower()
    if lagi != 'ya':
        break  # Keluar dari loop jika pengguna tidak ingin menambah barang lagi

print("Terima kasih!")