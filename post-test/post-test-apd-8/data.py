
from prettytable import PrettyTable
from hitung import hitung_pinjaman

data_peminjam = {}

def tambah_data():
    print("\nMasukkan data peminjam:")
    nama = input("Nama lengkap: ")

    if nama in data_peminjam:
        print("Nama sudah ada. Gunakan nama lain atau update data yang lama.")
        return

    ktp = input("Nomor KTP: ")
    alamat = input("Alamat: ")

    try:
        jumlah = int(input("Masukkan jumlah pinjaman (Rp): "))
        lama = int(input("Masukkan lama cicilan (bulan): "))
    except ValueError:
        print("Input harus berupa angka. Data dibatalkan.")
        return

    data_peminjam[nama] = {
        "ktp": ktp,
        "alamat": alamat,
        "jumlah": jumlah,
        "lama": lama
    }

    print("\nData peminjam berhasil disimpan!")

def tampilkan_data():
    if not data_peminjam:
        print("\nBelum ada data yang dimasukkan.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["Nama", "KTP", "Alamat", "Jumlah (Rp)", "Bunga", "Total", "Lama (Bulan)", "Cicilan/Bulan"]

    for nama, data in data_peminjam.items():
        bunga, total, cicilan = hitung_pinjaman(data["jumlah"], data["lama"])
        tabel.add_row([nama, data["ktp"], data["alamat"], data["jumlah"], bunga, total, data["lama"], cicilan])

    print("\n=== DAFTAR DATA PEMINJAM ===")
    print(tabel)

def update_data():
    if not data_peminjam:
        print("\nTidak ada data untuk di-update.")
        return

    nama_update = input("Masukkan nama peminjam yang ingin di-update: ")

    if nama_update not in data_peminjam:
        print("Data tidak ditemukan.")
        return

    data = data_peminjam[nama_update]
    print("\nPilih data yang ingin di-update:")
    print("1. Nomor KTP")
    print("2. Alamat")
    print("3. Jumlah Pinjaman")
    print("4. Lama Cicilan")
    pilih = input("Masukkan pilihan (1-4): ")

    if pilih == "1":
        data["ktp"] = input("Nomor KTP baru: ")
    elif pilih == "2":
        data["alamat"] = input("Alamat baru: ")
    elif pilih == "3":
        try:
            data["jumlah"] = int(input("Masukkan jumlah pinjaman baru: "))
        except ValueError:
            print("Input tidak valid.")
    elif pilih == "4":
        try:
            data["lama"] = int(input("Masukkan lama cicilan baru: "))
        except ValueError:
            print("Input tidak valid.")
    else:
        print("Pilihan tidak valid.")
        return

    print("\nData berhasil diperbarui.")

def hapus_data():
    if not data_peminjam:
        print("Belum ada data peminjam yang tersimpan.")
        return

    nama_hapus = input("Masukkan nama peminjam yang ingin dihapus: ")

    if nama_hapus in data_peminjam:
        del data_peminjam[nama_hapus]
        print(f"Data peminjam '{nama_hapus}' berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

if __name__ == "__main__":
    while True:
        print("\n=== MENU PROGRAM PINJAMAN ===")
        print("1. Tambah Data Peminjam")
        print("2. Tampilkan Data Peminjam")
        print("3. Update Data Peminjam")
        print("4. Hapus Data Peminjam")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
