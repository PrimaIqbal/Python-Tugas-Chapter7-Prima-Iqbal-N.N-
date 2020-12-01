print('Masukan nama file : ')
namafile = input()
file = open(namafile, "a")

jawab = 'y'
while (jawab == 'y'):
    print('Data yang mau ditambah : ')
    datatambah = input ()
    file.write(datatambah + "\n" )
    print('Mau lagi (y/n) : ')
    jawab = input()
    if (jawab == 'n' ):
        file.close()
        break
