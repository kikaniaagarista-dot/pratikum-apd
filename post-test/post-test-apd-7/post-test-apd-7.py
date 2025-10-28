data_peminjam = {}
login_berhasil = False
percobaan = 1


def login(percobaan):
    """Login rekursif maksimal 3 kali"""
    global login_berhasil

    if percobaan > 3:
        print("\nKesempatan login habis. Program dihentikan.")
        exit()

    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    akun = {
        "Kikania": "086",
    }

    if username in akun and akun[username] == password:
        login_berhasil = True
        print(f"\nLogin berhasil! Selamat datang, {username}!")
    else:
        print("Login gagal. Silakan coba lagi.\n")
        login(percobaan + 1)


def hitung_pinjaman(jumlah, lama):
    """Hitung bunga, total, dan cicilan"""
    bunga = int(jumlah * 0.1)
    total = jumlah + bunga
    cicilan = int(total / lama)
    return bunga, total, cicilan


def tampilkan_data():
    """Menampilkan data peminjam"""
    if not data_peminjam:
        print("\nBelum ada data yang dimasukkan.")
    else:
        print("\n=== DAFTAR DATA PEMINJAM ===")
        for nama, data in data_peminjam.items():
            bunga, total, cicilan = hitung_pinjaman(data["jumlah"], data["lama"])
            print(f"""
Nama Peminjam     : {nama}
Nomor KTP         : {data['ktp']}
Alamat            : {data['alamat']}
Jumlah Pinjaman   : Rp {data['jumlah']}
Bunga (10%)       : Rp {bunga}
Total Pinjaman    : Rp {total}
Lama Cicilan      : {data['lama']} bulan
Cicilan per Bulan : Rp {cicilan}
""")


def hapus_data(nama_hapus):
    """Hapus data peminjam"""
    if nama_hapus in data_peminjam:
        del data_peminjam[nama_hapus]
        print(f"Data peminjam '{nama_hapus}' berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")


def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\n=== MENU UTAMA ===")
    print("1. Input Data Peminjam")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")


print("=== SISTEM PINJAMAN DANA ===")
print("Silakan login terlebih dahulu")
print("--------------------------------")

login(percobaan)

while login_berhasil:
    tampilkan_menu()
    menu = input("Pilih menu (1-5): ")

    try:
        if menu == "1":
            print("\nMasukkan data peminjam:")
            nama = input("Nama lengkap: ")

            if nama in data_peminjam:
                print("Nama sudah ada. Gunakan nama lain atau update data yang lama.")
                continue

            ktp = input("Nomor KTP: ")
            alamat = input("Alamat: ")

            try:
                jumlah = int(input("Masukkan jumlah pinjaman (Rp): "))
                lama = int(input("Masukkan lama cicilan (bulan): "))
            except ValueError:
                print("Input harus berupa angka. Data dibatalkan.")
                continue

            data_peminjam[nama] = {
                "ktp": ktp,
                "alamat": alamat,
                "jumlah": jumlah,
                "lama": lama
            }

            print("\nData peminjam berhasil disimpan!")

        elif menu == "2":
            tampilkan_data()

        elif menu == "3":
            if not data_peminjam:
                print("\nTidak ada data untuk di-update.")
            else:
                nama_update = input("Masukkan nama peminjam yang ingin di-update: ")
                if nama_update not in data_peminjam:
                    print("Data tidak ditemukan.")
                    continue

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
                print("\nData berhasil diperbarui.")

        elif menu == "4":
            if not data_peminjam:
                print("Belum ada data peminjam yang tersimpan.")
            else:
                nama_hapus = input("Masukkan nama peminjam yang ingin dihapus: ")
                hapus_data(nama_hapus)

        elif menu == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

    except:
        print("Terjadi kesalahan, coba lagi.")