def bentukDiamond(n):
    for i in range(n) :
        print(' '*(n-i-1)+ '* '*(i+1))
    for i in range(n-1) :
        print(' '*(i+1)+ '* '*(n-i-1))

n = int(input("Masukkan Angka: "))
print()
bentukDiamond(n)

a = [3, 20, 100, -35, 50]

print(a)
print('Nilai terbesar:', nilai_maksimal(a))
print('Nilai terkecil:', nilai_minimal(a))