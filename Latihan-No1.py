print('Masukan nama file : ')
namafile = input()
print('Isi file', namafile, 'adalah: ')
isifile = open(namafile, "r")
print(isifile.read())
