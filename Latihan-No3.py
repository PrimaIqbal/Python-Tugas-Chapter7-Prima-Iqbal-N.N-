print('------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('------------------------------')
data = []
jawab = 'y'
while (jawab =='y'):
    try:
        print('Masukkan bilangan bulat : ')
        builbul = int(input ())
        print('Lagi (y/n) ? : ')
        jawab = input ()
        data.append(bilbul)

        if jawab == 'n' :
            jumlah = sum(data)
            banyak = len(data)
            rrerata = jumlah/banyak
            print('rata - ratanya adalah : ', rerata)
            break

    except ValueError:
            print('Bukan bilangan bulat')
