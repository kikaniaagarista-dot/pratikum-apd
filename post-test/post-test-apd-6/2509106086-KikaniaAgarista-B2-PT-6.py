percobaan = 1
login_berhasil = False


data_peminjam = {} 

print("=== SISTEM PINJAMAN DANA ===")
print("Silahkan login terlebih dahulu")
print("-------------------------------")

while percobaan <= 3:  
    username = input("Masukan Nama (Username): ")
    password = input("Masukan NIM (Password): ")


    if username == "Kikania" and password == "086":
        print("\nLogin berhasil! Selamat datang,", username)

        while True:
            print("\n=== MENU UTAMA ===")
            print("1. Input Data Pinjaman")
            print("2. Tampilkan Data")
            print("3. Update Data")
            print("4. Hapus Data Berdasarkan Nama")
            print("5. Keluar")
            menu = input("Pilih menu (1-5): ") 

            if menu == "1":
                print("\nMasukan data peminjam:")
                nama = input("Nama lengkap: ")
                

                if nama in data_peminjam: 
                    print("Nama sudah ada. Gunakan nama lain atau update data yang lama.")
                    continue

                ktp = input("Nomor KTP: ")
                alamat = input("Alamat: ")

                jumlah_input = input("Masukan jumlah pinjaman (Rp): ")

                if not jumlah_input.isdigit(): 
                    print("Input harus angka. Data dibatalkan.")
                    continue
                jumlah = int(jumlah_input)

                lama_input = input("Masukan lama cicilan (bulan): ")
                if not lama_input.isdigit():
                    print("Input harus angka. Data dibatalkan.")
                    continue
                lama = int(lama_input)

                data_peminjam[nama] = {
                    "ktp": ktp,
                    "alamat": alamat,
                    "jumlah": jumlah,
                    "lama": lama
                }

                print("\nData peminjam berhasil disimpan!")

            elif menu == "2":
                if not data_peminjam:
                    print("\nBelum ada data yang dimasukkan.")
                else:
                    print("\n=== DAFTAR DATA PEMINJAM ===")
                    
                    for nama, data in data_peminjam.items():
                        bunga = int(data["jumlah"] * 0.1)
                        total = data["jumlah"] + bunga
                        cicilan = int(total / data["lama"])

                        print("\nNama Peminjam     :", nama)
                        print("Nomor KTP           :", data["ktp"])
                        print("Alamat              :", data["alamat"])
                        print("Jumlah Pinjaman     : Rp", data["jumlah"])
                        print("Bunga (10%)         : Rp", bunga)
                        print("Total Pinjaman      : Rp", total)
                        print("Lama Cicilan        :", data["lama"], "bulan")
                        print("Cicilan per Bulan   : Rp", cicilan)

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
                        jumlah_input = input("Masukkan jumlah pinjaman baru: ")
                        if jumlah_input.isdigit():
                            data["jumlah"] = int(jumlah_input)
                        else:
                            print("Input tidak valid.")
                    elif pilih == "4":
                        cicilan_input = input("Masukan lama cicilan baru: ")
                        if cicilan_input.isdigit():
                            data["lama"] = int(cicilan_input)
                        else:
                            print("Input tidak valid.")
                    else:
                        print("Pilihan tidak valid.")
                    print("\nData berhasil diperbarui.")

            elif menu == "4":
                if not data_peminjam:
                        print("Belum ada data peminjam yangntersimpan.")
                else:
                    nama_hapus = input("Masukan nama peminjam yang ingin di hapus: ")


                    if nama_hapus in data_peminjam:
                        del data_peminjam[nama_hapus]
                        print(f"data peminjam '{nama_hapus}' berhasil di hapus. ")
                    else:
                        print("Data tidak ditemukan.")

            elif menu == "5":
                print("Terimakasih telah menggunakan progam ini.")
                exit()
            else:
                print("Pilihan tidak valid, coba lagi.")

    else:
        print("Login gagal. Silahkan coba lagi.")
        percobaan += 1
        if percobaan > 3:
            print("\nKesempatan login habis. Program dihentikan.")
            exit()