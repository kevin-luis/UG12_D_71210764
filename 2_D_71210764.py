
def senin():
    senin = ['1 Algorima Graf', '3 Sistem Operasi', '4 PAK']
    for i in range(len(senin)):
        print(f"kelas ke-{senin[i]}")

def selasa():
    selasa = ['2 Matematika Teknik', '4 Bhs Indonesia', '6 PKN']
    for i in range(len(selasa)):
        print(f"kelas ke-{selasa[i]}")

def rabu():
    rabu = ['2 Sistem Basis Data', '4 Praktikum Basis Data']
    for i in range(len(rabu)):
        print(f"kelas ke-{rabu[i]}")

def kamis():
    kamis = ['1 IMK', '3 LogMat', '4 Praktekkom']
    for i in range(len(kamis)):
        print(f"kelas ke-{kamis[i]}")

def jumat():
    print("Hari Jumat Anda tidak ada kelas")


hari = str(input("Hai Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: "))

if hari == "senin" :
    senin()
elif hari == "selasa" :
    selasa()
elif hari == "rabu" :
    rabu()
elif hari == "kamis" :
    kamis()
elif hari == "jumat" :
    jumat()
    
