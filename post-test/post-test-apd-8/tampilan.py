from prettytable import PrettyTable

tabel1 = PrettyTable()

tabel1.field_names = ["===== MENU UTAMA ====="]
tabel1.add_row(["1. Input Data Peminjam"])
tabel1.add_row(["2. Tampilkan Data"])
tabel1.add_row(["3. Update Data"])
tabel1.add_row(["4. Hapus Data"])
tabel1.add_row(["5. Keluar"])
tabel1.align = "l"

def tampilkan_menu():
    print(tabel1)
