try:
    file = open("e:/data1.txt","r")
    bil1 = int(file.readline(1))
    bil2 = int(file.readline(2))
    hasil = bil1/bil2
    print(bil1 , "dibagi" , bil2 , "sama dengan" , hasil)
except:
    print('file tidak ditemukan')

try:
    file = open("e:/data1.txt","r")
    bil1 = int(file.readline(1))
    bil2 = int(file.readline(2))
    hasil = bil1/bil2
    print(bil1 , "dibagi" , bil2 , "sama dengan" , hasil)
except:
    print('Tidak boleh pembagian dengan nol')
