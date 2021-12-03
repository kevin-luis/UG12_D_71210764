# Input Variabel
awal = int(input("Masukkan awal deret: "))
akhir = int(input("Masukkan akhir deret:"))

#Perulangan dan Output
for i in range(awal,akhir):
    if (i % 3 != 0) and (i % 7 != 0) and (i % 2 == 0) :
        print(i, end=" ")