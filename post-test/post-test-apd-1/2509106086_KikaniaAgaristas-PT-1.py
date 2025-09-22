#input
nama = input("masukkan nama: ")
NIM = input("masukkan NIM: ")
HM = float(input("Ingin membeli makanan seharga: "))

#Pajak dan Total harga
PP = HM * (5 / 100) #Pajak Pecel lele
HP = HM + PP   # Harga pecel lele

PM = HM * (8 / 100) #Pajak Mie ayam
HMi = HM + PM  # Harga mie ayam

PN = HM * (10 / 100) #Pajak Nasi padang
HN = HM + PN   # Harga nasi padang


#output
print("===Hasil Perhitungan===")
print("Nama:", nama)
print("NIM:", NIM)

print("-------------------------------------------")
print("|    Menu Makanan    |       Harga        |")
print("-------------------------------------------")
print(f"|     Pecel lele     |       Rp{HP:,.0f} |")
print(f"|      Mie ayam      |       Rp{HMi:,.0f} |")
print(f"|    Nasi Padang     |       Rp{HN:,.0f} |")
print("-------------------------------------------")