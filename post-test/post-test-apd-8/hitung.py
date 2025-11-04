
def hitung_pinjaman(jumlah, lama):
    """Hitung bunga, total, dan cicilan"""
    bunga = int(jumlah * 0.1)
    total = jumlah + bunga
    cicilan = int(total / lama)
    return bunga, total, cicilan