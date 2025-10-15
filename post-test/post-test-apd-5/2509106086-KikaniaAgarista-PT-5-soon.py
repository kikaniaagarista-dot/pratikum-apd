
username_benar = "Kikania"
password_benar = "086"

percobaan = 1
login_berhasil = False

print("=== SISTEM PINJAMAN DANA ===")
print("Silahkan login terlebih dahulu")
print("-------------------------------")

while percobaan <= 3 and not login_berhasil:
    username = input("Masukan Nama (Username): ")
    password = input("Masukan NIM (Password): ")

    if username == username_benar and password == password_benar:
        print("/nLogin berhasil! Selamat datang,", username)
        login_berhasil = True
    else:
        print("Login gagal. Silahkan coba lagi")
        percobaan + 1
        if percobaan > 3:
            print("\nKesempatan login habis. Progam di hentikan.")
            exit()

data_ada = False 
nama_peminjam = ""
nomor_ktp = ""
alamat = ""
jenis_pinjaman = ""
jumlah_pinjaman = 0
lama_cicilan = 0
metode_pembayaran = ""
bunga = 0
total_pinjaman = 0
cicilan_per_bulan = 0


while True:
    print("\n=== MENU UTAMA ===")
    print("1. Input Data Pinjaman")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")
    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        print("\nMasukan data peminjam:")
        nama_peminjam = input("Nama lengkap: ")
        nomor_ktp = input("Nomor KTP: ")
        alamat = input("Alamat: ")


        print("\nPilih jenis pinjaman:")
        print("1. Pinjaman Pendidikan")
        print("2. Pinjaman Usaha")
        print("3. Pinjaman Pribadi")
        jenis_input = input("Masukan pilihan (1/2/3): ")

        if jenis_input == "1":
            jenis_pinjaman = "Pendidikan"
        elif jenis_input == "2":
            jenis_pinjaman = "Usaha"
        elif jenis_input == "3":
            jenis_pinjaman = "Pribadi"
        else:
            print("Pilihan tidak valid, data di batalkan.")
            jenis_pinjaman = ""


        if jenis_pinjaman != "":
            jumlah_pinjaman = int(input("Masukan jumlah pinjaman (dalam rupiah): "))
            lama_cicilan = int(input("Masukan lama cicilan (dalam bulan): "))


            print("\nPilih metode pembayaran:")  
            print("1. Transsfer Bank")
            print("2. Dompet Digital")
            print("3. Tunai")             
            metode_input = input("Maukaan pilihan (1/2/3): ")

            if metode_input == "1":
                metode_pembayaran = "Transfer Bank"
            elif metode_input == "2": 
                metode_pembayaran = "Dompet Digital"
            elif metode_input == "3":
                metode_pembayaran = "Tunai"
            else:
                metode_pembayaran = ""
                print("Pilihan tidak valid, data dibatalkan.")
                        

            if metode_pembayaran != "":
                bunga = 0.1 * jumlah_pinjaman
                total_pinjaman = jumlah_pinjaman + bunga 
                cicilan_per_bulan = total_pinjaman / lama_cicilan
                data_ada = True
                print("\nData peminjam berhasil disimpan!")



    elif menu == "2":
        if data_ada:
            print("\n=== RINCIAN PINJAMAN ===")
            print("Nama Peminjam       :", nama_peminjam)
            print("Nomor KTP           :", nomor_ktp)
            print("Alamat              :", alamat)
            print("Jenis Pinjaman      :", jenis_pinjaman)
            print("Jumlah Pinjaman     : Rp", jumlah_pinjaman)
            print("Bunga (10%)         : Rp", int(bunga))
            print("Total Pinjaman      : Rp", int(total_pinjaman))
            print("Lama Cicilan        :", lama_cicilan, "bulan")
            print("Cicilan per Bulan   : Rp", int(cicilan_per_bulan))
            print("Metode Pembayaran   :", metode_pembayaran)
        else:
            print("\nBelum ada data yang dimasukan.")


    elif menu == "3":
        if not data_ada:
            print("\nTidak ada data untuk di-update")
        else:
            print("\nPilih data yang ingin di-update:")
            print("1. Nama Peminjam")
            print("2. Nomor KTP")
            print("3. Alamat")
            print("4. Jenis Pinjaman")
            print("5. Pinjaman")
            print("6. Lama Cicilan")
            print("7. Metode Pembayaran")
            pilih_update = input("Masukkan pilihan (1-7): ")

            if pilih_update == "1" :
                nama_peminjam = input("Nama baru: ")
            elif pilih_update == "2":
                nomor_ktp = input("Nomor KTP baru: ")
            elif pilih_update == "3":
                alamat = input("Alamat baru: ")
            elif pilih_update == "4":
                print("\nPilih jenis pinjaman:")
                print("1. Pendidikan")
                print("2. Usaha")
                print("3. Pribadi")
                jenis_input = input("Masukan pilihan (1/2/3): ")
                if jenis_input == "1":
                    jenis_pinjaman = "Pendidikan"
                elif jenis_input == "2":
                    jenis_pinjaman = "Usaha"
                elif jenis_input == "3":
                    jenis_pinjaman = "Pribadi"
                else:
                    print("Input tidak valid.")

            elif pilih_update == "5":
                jumlah_pinjaman = int(input("Masukan jumlah pinjaman baru: "))
                bunga = 0.1 * jumlah_pinjaman
                total_pinjaman = jumlah_pinjaman + bunga
                cicilan_per_bulan = total_pinjaman / lama_cicilan

            elif pilih_update == "6":
                lama_cicilan = int(input("Masukan lama cicilan baru: "))
                cicilan_per_bulan = total_pinjaman / lama_cicilan

            elif pilih_update == "7":
                print("\nPilih metode pembayaran baru:")
                print("1. Transfer Bank")
                print("2. Dompet Digital")
                print("3. Tunai")
                metode_input = input("Masukan pilihan (1/2/3): ")
                if metode_input == "1":
                    metode_pembayran = "Transfer Bank"
                elif metode_input == "2":
                    metode_pembayaran = "Dompet Digital"
                elif metode_input == "3":
                    metode_pembayaran = "Tunai"
                else:
                    print("Input tidak valid.")

            else:
                print("Pilihan tidak valid.")


            print("\nData berhasil di perbarui")

    elif menu == "4":
        if data_ada:
            konfirmasi = input("Yakin ingin menghapus data? (y/n): ")
            if konfirmasi.lower() == "y":
                data_ada = False
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")

        else:
            print("Tidak ada data untuk di hapus.")


    elif menu == "5":
        print("\nTerimakasih telah menggunakan progam ini!")
        break

    else: 
        print("Pilihan tidak valid, coba lagi.")