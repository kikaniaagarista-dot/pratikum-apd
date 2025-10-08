# for i in range (1, 10, 2):
#     print(f'Perulangan ke {i}')

# for i in range (10, 1, -1):
#     print(f'Perulangan ke {i}')

# mahasiswa = [ "ahnap", "dapupu", 10, 102,"True"]

# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)


# mahasiswa = []
# for i in "mahasiswa":
#     print(i)

    
# for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
#    for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
#        print(f'{i} x {j} = {i * j}')
#    print('') #biar ada jarak tiap iterasi


# for i in range(10): 
#     for j in range(10):
#         print(i, end="")
#     print("")

# for i in range(1, 10): 
#     for j in range(1, i+1):
#         print("@", end="")
#     print("")

# for i in range(1, 10): 
#     for j in range(1, i+1):
#         print("ini j", end="")
#     print("ini i")


# for i in range(1, 10): 
#     for j in range(1, i+1):
#         print("#", end="  ")
#     print("")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
# print(f"Total perulangan: {hitung}")



# while True:
#     print("MENU")
#     print("1. fitur 1")
#     print("2. fitur 2")
#     print("3. fitur 3")
#     opsi = int(input("Masukan opsi: "))
#     if opsi == 1:
#         print("1. fitur 1")
#     elif opsi == 2:
#         print("2. fitur 2")
#     else:
#         break 

while True:
    print("MENU")
    print("1. fitur 1")
    print("2. fitur 2")
    print("3. fitur 3")
    opsi = int(input("Masukan opsi: "))
    if opsi == 1:
        print("1. fitur 1")
    elif opsi == 2:
        print("2. fitur 2")
    elif opsi == 3:
        break 
    else: 
        print("pilihan invalid")

