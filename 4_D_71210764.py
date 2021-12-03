# input Fungsi

def nilaiTerbesar(x) :
    nilaiTertinggi = x[0]

    for nilai in x :
        if nilai >  nilaiTertinggi :
            nilaiTertinggi = nilai
        
    return nilaiTertinggi

def nilaiTerkecil(x) :
    nilaiTerendah = x[0]

    for nilai in x :
        if nilai < nilaiTerendah:
            nilaiTerendah = nilai
    
    return nilaiTerendah

nilaiInput1 = [3, 20, 100, -35, 50]
nilaiInput2 = [3, 20, 90, 35, 75]

#Output
print(nilaiInput1)
print(f"Nilai terbesar : {nilaiTerbesar(nilaiInput1)}")
print(F"Nilai terkecil : {nilaiTerkecil(nilaiInput1)}")
