
# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)



# angka_ganjil = {1, 3, 5, 7, 9}

# for angka in angka_ganjil:
#     print(angka) 
 


# nama = ['dapupu','julpa','asep hedsot']


# angka_ganjil = {1, 3, 5, 7, 9}

# for angka in angka_ganjil:
#     print(angka) 

# print("menambahkan angka 11")
# angka_ganjil.add(11)



# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# # print(Daftar_buku["Buku1"])

# # print(Daftar_buku)

# # print(Daftar_buku.keys())

# for value in Daftar_buku.values():
#     print(value)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True, 
#     "Social Media" : { "Instagram" : "daffahrhap"  
#     }
# }

# print(Biodata["KRS"][1])

# print(Biodata)

# list_mahasiswa = dict(nama="Dapupu", Jurusan="Informatika")
# print(list_mahasiswa)


# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True, 
#     "Social Media" : { "Instagram" : "daffahrhap"  
#     }
# }

# for i,j in Biodata.items():
#     print(f"{i} : {j}")

# print(f"nama saya adalah {Biodata["MAHASIGMA"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# # print(f"nama saya adalah {Biodata.get["Nama"]}")
# print(Biodata.get)

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }

# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah
# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")


Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
      
#Sebelum Ditambah
print(Film)
Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
#Setelah Ditambah
print("")

