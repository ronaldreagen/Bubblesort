def bubbleSort(array):
    n = len(array)
    for i in range(n):
        tukar = False
        print(f"Langkah {i + 1}:")
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Tukar elemen jika tidak dalam urutan yang benar
                array[j], array[j + 1] = array[j + 1], array[j]
                tukar = True
            print(f"  Membandingkan indeks {j} dan {j + 1}: {array}")
        
        if not tukar:
            print("  Tidak ada pertukaran pada langkah ini. Array sudah terurut.")
            break
        print(f"  Hasil setelah Langkah {i + 1}: {array}\n")

# Request input brainware
input_data = input("Masukkan angka-angka yang ingin diurutkan (pisahkan dengan spasi): ")

# Ubah input string menjadi list of integer
data = list(map(int, input_data.split()))

bubbleSort(data)

print('Array yang telah diurutkan dalam urutan menaik:')
print(data)
