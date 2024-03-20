def konversi_biner(angka):
    return bin(angka)
def konversi_oktal(angka):
    return oct(angka)

def konversi_desimal(angka):
    return str(angka)

def konversi_heksadesimal(angka):
    return hex(angka)

def main():
    while True:
        try:
            pilihan = int(input("Pilih jenis konversi:\n1. Biner\n2. Oktal\n3. Desimal\n4. Heksadesimal\n5. Keluar\nPilihan Anda: "))
            
            angka = int(input("Masukkan angka: "))
            if pilihan == 1:
                hasil = konversi_biner(angka)
                print("Angka", angka, "dalam bentuk biner adalah:", hasil)
            elif pilihan == 2:
                hasil = konversi_oktal(angka)
                print("Angka", angka, "dalam bentuk oktal adalah:", hasil)
            elif pilihan == 3:
                hasil = konversi_desimal(angka)
                print("Angka", angka, "dalam bentuk desimal adalah:", hasil)
            elif pilihan == 4:
                hasil = konversi_heksadesimal(angka)
                print("Angka", angka, "dalam bentuk heksadesimal adalah:", hasil)
          
            else:
                print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, 4, atau 5.")
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")

if __name__ == "__main__":
    main()