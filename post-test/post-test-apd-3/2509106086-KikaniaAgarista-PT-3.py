
# Progam Pembayaran Langganan Musik 
nama_asli = "Kikan" 
nim_asli = "086" 

BL = 1500000

nama = input("Masukan Nama").strip()
nim =  input("Masukan NIM").strip()

if nama == nama_asli and nim == nim_asli:
    print("Login")
   

    print("Paket Bronze: Biaya administrasi 1%, akses dasar ke lagu-lagu populer.")
    print("Paket Silver: Biaya administrasi 3%, akses lagu premium dan playlist kustom.")
    print("Paket Gold: Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline.")
    print("Paket Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.")

    print("Ketik nama paket dengan huruf BESAR SEMUA (BRONZE/SILVER/GOLD/PLATINUM)")
    paket = input("Masukan paket: ")

    if paket == "BRONZE": 
        TBB = BL + (BL*0.01)
        print("Total Biaya Paket BRONZE:", TBB)
   

    elif paket == "SILVER":
        TBS = BL + (BL*0.03)
        print("Total Biaya Paket SILVER:", TBS)
    

    elif paket == "GOLD":
        TBG = BL + (BL*0.05)
        print("Total Bayar  Paket GOLD:", TBG)


    elif paket == "PLATINUM": 
        TBP = BL + (BL*0.07)
        print("Total Biaya Paket PLATINUM", TBP)

    else :
        print("Pilihan Tidak Valid")
    
else : 
    print("Gagal login")

