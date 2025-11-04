
print(" ===LOGIN BIOSKOP XX0==== ")

percobaan = 1
login_berhasil = False

while percobaan <= 3:
    nama = input("Masukan Nama : ")
    nim  = input("Masukan Nim: ")

    if nama == "Kikania" and nim == "086":
        print("Login berhasil")
        login_berhasil = True
        break
    else:
        print("Login gagal")
        percobaan = percobaan + 1

if not login_berhasil:
    print("login terlalu banyak percobaan.Progam berhenti")

total_bayar = 0

while True:
    print("===MENU PEMBELIASAN TIKET BIOSKOP XX0===")
    print("1. Tiket Reguler = Rp 50.000")
    print("2. Tiket VIP = Rp.100.000")
    print("3. Tiket VVIP = Rp.150.00 ")
    print("4. Keluar")

    pilihan = input("Pilih jenis tiket (1-4): ")
    if pilihan == "4": 
        break
    elif  pilihan == "1" or pilihan == "2" or pilihan == "3":
        jumlah_input = input("Masukan jumlah tiket : ")

        if jumlah_input.isdigit():
            jumlah = int(jumlah_input)

        else:
            print("Input harus berupa angka")
            continue
        
        if jumlah <= 0:
            print("Jumlah tiket harus lebih dari 0!")
            continue

        if pilihan == "1" :
            harga = 50000
            jenis = "Reguler"

        elif pilihan == "2":
            harga = 100000
            jenis = "VIP"

        else:
            harga = 150000
            jenis = "VVIP"


        subtotal = harga * jumlah
        total_bayar = total_bayar + subtotal
        print(f"Anda membeli {jumlah} tiket {jenis} dengan total Rp. {subtotal:,} ")
 

