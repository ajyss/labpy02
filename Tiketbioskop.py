# Program Pemesanan Tiket Bioskop
print("=== Program Pemesanan Tiket Bioskop ===")

# Input tipe tiket
print("\nPilihan Tiket:")
print("1. Reguler (Rp50.000)")
print("2. VIP (Rp100.000)")
tipe = input("Masukkan pilihan tiket (1/2): ")

# Menentukan harga dengan if else
if tipe == "1":
    harga = 50000
else:
    harga = 100000

# Input status member
member = input("Apakah anda member? (y/n): ").lower()

# Menghitung diskon dengan operator ternary
diskon = 0.2 if member == "y" else 0

# Menghitung total dengan if else
if member == "y":
    total = harga - (harga * diskon)
else:
    total = harga

# Output hasil dengan operator ternary
print("\nDetail Pembayaran:")
print(f"Tipe Tiket: {'Reguler' if tipe == '1' else 'VIP'}")
print(f"Status Member: {'Ya' if member == 'y' else 'Tidak'}")
print(f"Harga Tiket: Rp{harga}")
print(f"Diskon: {int(diskon * 100)}%")
print(f"Total Bayar: Rp{int(total)}")