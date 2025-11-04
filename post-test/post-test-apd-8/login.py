
login_berhasil = False

def login(percobaan):
    """Login rekursif maksimal 3 kali"""
    global login_berhasil

    if percobaan > 3:
        print("\nKesempatan login habis. Program dihentikan.")
        exit()

    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    akun = {
        "Kikania": "086",
    }

    if username in akun and akun[username] == password:
        login_berhasil = True
        print(f"\nLogin berhasil! Selamat datang, {username}!")
    else:
        print("Login gagal. Silakan coba lagi.\n")
        login(percobaan + 1)
