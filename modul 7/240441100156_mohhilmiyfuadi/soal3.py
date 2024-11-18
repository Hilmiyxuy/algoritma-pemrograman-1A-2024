data_siswa = {
    1: [],  
    2: [],  
    3: []  
}

# Fungsi untuk menambahkan siswa
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    kelas = input("Masukkan kelas siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")
    plotting = int(input("Masukkan plotting (1/2/3): "))

    if plotting not in data_siswa:
        print("Plotting tidak valid. Pilih antara 1, 2, atau 3.")
        return

    # Cek apakah kelas sudah penuh (maksimal 3 siswa per kelas)
    if len(data_siswa[plotting]) >= 3:
        print("Kelas di plotting ini sudah penuh.")
        return

    # Tambahkan siswa ke plotting yang dipilih
    data_siswa[plotting].append({
        'nama': nama,
        'kelas': kelas,
        'asal_sekolah': asal_sekolah
    })
    print(f"Siswa {nama} berhasil ditambahkan ke plotting {plotting}.")

# Fungsi untuk menampilkan data siswa
def tampilkan_data():
    if not any(data_siswa.values()):
        print("Belum ada data siswa.")
        return
    
    for plotting, siswa_list in data_siswa.items():
        print(f"\nPlotting {plotting}:")
        if not siswa_list:
            print("Belum ada siswa di plotting ini.")
            continue
        for siswa in siswa_list:
            print(f"Nama: {siswa['nama']}, Kelas: {siswa['kelas']}, Asal Sekolah: {siswa['asal_sekolah']}")

# Fungsi untuk mengupdate data siswa
def update_siswa():
    nama_lama = input("Masukkan nama siswa yang ingin diubah: ")
    plotting = int(input("Masukkan plotting (1/2/3): "))

    if plotting not in data_siswa:
        print("Plotting tidak valid.")
        return

    for siswa in data_siswa[plotting]:
        if siswa['nama'] == nama_lama:
            siswa['nama'] = input("Masukkan nama baru: ")
            siswa['kelas'] = input("Masukkan kelas baru: ")
            siswa['asal_sekolah'] = input("Masukkan asal sekolah baru: ")
            print(f"Data siswa {nama_lama} berhasil diperbarui.")
            return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan di plotting {plotting}.")

# Fungsi untuk menghapus siswa
def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    plotting = int(input("Masukkan plotting (1/2/3): "))

    if plotting not in data_siswa:
        print("Plotting tidak valid.")
        return

    for siswa in data_siswa[plotting]:
        if siswa['nama'] == nama:
            data_siswa[plotting].remove(siswa)
            print(f"Siswa {nama} berhasil dihapus dari plotting {plotting}.")
            return
    print(f"Siswa dengan nama {nama} tidak ditemukan di plotting {plotting}.")

# Fungsi untuk menampilkan menu
def menu():
    while True:
        print("\n=== Selamat datang di lembaga bimbingan intensif Gema Ripah ===")
        print("1. Menambahkan nama siswa yang ikut bimbingan")
        print("2. Tampilkan Data Siswa bimbingan")
        print("3. Update Siswa yang ikut bimbingan")
        print("4. Hapus Siswa dari bimbingan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == '1':
            tambah_siswa()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            update_siswa()
        elif pilihan == '4':
            hapus_siswa()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


menu()