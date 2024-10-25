# Program Kalkulator Sederhana
print("=== Program Kalkulator Sederhana ===")

# Input dua angka
angka1 = float(input("\nMasukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Input operator
print("\nOperator yang tersedia: ")
print("+ : Penjumlahan")
print("- : Pengurangan")
print("* : Perkalian")
print("/ : Pembagian")
operator = input("\nMasukkan operator: ")

# Proses perhitungan menggunakan if elif else
if operator == '+':
    hasil = angka1 + angka2
    operasi = "Penjumlahan"
elif operator == '-':
    hasil = angka1 - angka2
    operasi = "Pengurangan"
elif operator == '*':
    hasil = angka1 * angka2
    operasi = "Perkalian"
elif operator == '/':
    if angka2 != 0:  # Cek pembagian dengan nol
        hasil = angka1 / angka2
        operasi = "Pembagian"
    else:
        print("\nError: Tidak bisa melakukan pembagian dengan nol!")
        exit()
else:
    print("\nError: Operator tidak valid!")
    exit()

# Output hasil
print("\nDetail Perhitungan:")
print(f"Operasi: {operasi}")
print(f"Angka 1: {angka1}")
print(f"Angka 2: {angka2}")
print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")