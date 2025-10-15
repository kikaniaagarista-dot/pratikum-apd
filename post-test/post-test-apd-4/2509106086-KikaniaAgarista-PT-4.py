

print("=== LOGIN BIOSKOP XX0 ===")

percobaan = 1
login_berhasil = False

while percobaan <= 3:
    nama = input("Masukkan Nama: ").lower()
    nim = input("Masukkan NIM: ")

    if nama == "kikania" and nim == "086":
        print("Login")
        login_berhasil = True
        break
    else:
        print("Login gagal")
        percobaan = percobaan + 1


if not login_berhasil:
    print("Terlalu banyak percobaan. Program berhenti.")
    exit()


total_bayar = 0

while True:
    print("=== MENU PEMBELIAN TIKET BIOSKOP XX0 ===")
    print("1. Tiket Reguler  = Rp50.000")
    print("2. Tiket VIP      = Rp100.000")
    print("3. Tiket VVIP     = Rp150.000")
    print("4. Keluar")

    pilihan = input("Pilih jenis tiket (1-4): ")

    if pilihan == "4":
        break
    elif pilihan == "1" or pilihan == "2" or pilihan == "3":
        jumlah_input = input("Masukkan jumlah tiket: ")

        
        if jumlah_input.isdigit():
            jumlah = int(jumlah_input)
        else:
            print("Input harus berupa angka!")
            continue

        if jumlah <= 0:
            print("Jumlah tiket harus lebih dari 0!")
            continue

        
        if pilihan == "1":
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
        print(f"Anda membeli {jumlah} tiket {jenis} dengan total Rp{subtotal:,}")

    else:
        print("Pilihan tidak valid!")

print("\n=== STRUK PEMBELIAN ===")
print(f"Total Sebelum Diskon: Rp{total_bayar:,}")

# Menentukan potongan atau bonus
if total_bayar >= 300000:
    potongan = total_bayar * 0.12
    total_bayar = total_bayar - potongan
    print("Anda mendapat potongan 12%!")
elif total_bayar >= 200000:
    potongan = total_bayar * 0.08
    total_bayar = total_bayar - potongan
    print("Anda mendapat potongan 8%!")
elif total_bayar >= 150000:
    print("Anda mendapat Poster Film Eksklusif!")

print(f"Total Bayar Akhir: Rp{total_bayar:,.0f}")
print("Terima kasih telah membeli tiket di Bioskop XX0!")
