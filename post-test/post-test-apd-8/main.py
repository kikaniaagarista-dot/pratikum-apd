import login
from data import tambah_data, tampilkan_data, update_data, hapus_data
from tampilan import tampilkan_menu

print("=== SISTEM PINJAMAN DANA ===")
print("Silakan login terlebih dahulu")
print("--------------------------------")



login.login(1)

while login.login_berhasil:
    tampilkan_menu()
    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        tambah_data()
    elif menu == "2":
        tampilkan_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        hapus_data()
    elif menu == "5":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")