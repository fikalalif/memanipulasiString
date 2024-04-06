string1 = 'hello'
string2 = 'word'
int1 = 6
print (string1 + " " + string2)
print ((string1 + " ") * 10)
print (string1 + " " + str(int1))

# list to str
daftar_kalimat = ['aku', 'seorang', 'kapal laut']
kalimat = " ".join(daftar_kalimat)
print (kalimat)

# str to list
hehehe = 'aku seorang kapal laut'
hahaha = hehehe.split()
print (hahaha)

# sub string/ replace string
daftar_kalimat1 = 'aku seorang rapper kampung, kamu orang kampung'
substring = daftar_kalimat1.replace('kampung','ndeso')
print (substring)

# lowercase & uppercase
nama = 'kapal laut'
nama1 = 'LAUT KAPAL'
print(nama1.lower())
print(nama.upper())
print(nama.capitalize())
print(nama.title())

kota = input('Nama Kota : ').title()
print(kota)