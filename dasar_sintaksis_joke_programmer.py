"""
Semua sintaks dasar pemrograman terdiri dari :
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali - kali selama/sampai kondisi terpenuhi
"""
#sekuensial
"""
print('Ibu berkata,"Pergi ke toko"')
print('Budi menjawab,"Apa yang harus saya beli?"')
print('Ibu menjawab,"Beli satu botol susu, dan jika ada telor beli 6"')
print('Kemudian Budi pergi ke toko')
print('Budi mulai berbelanja')
"""
# Percabangan
milkAmount = 100
milkPrice: int = 10000
money: int  = 50000
eggAmount = 100

if milkAmount > 0:
    print("Budi pergi ke toko")
    if money > milkPrice * 1:
        if eggAmount > 0:
            print("Budi membeli 1 botol susu")
            print("Budi membeli 6 butir telur")
            print("Budi pulang ke rumah")
            print("Budi menyerahkan belanjaan ke Ibu")
        else:
            print("Budi membeli 1 botol susu")
            print("Budi pulang ke rumah")
            print("Budi menyerahkan belanjaan ke Ibu")
    else:
        print("Budi pulang")
else:
    print("Budi tidak jadi membeli 1 botol susu")