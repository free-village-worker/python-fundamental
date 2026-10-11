"""
Program perulangan membaca buku dengan while sampai paham
"""
jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_dipahami = 0
jumlah_baca = 0
print(f'Jumlah buku yang sudah dibaca dan dpahami {jumlah_buku_dipahami}')

print("Dengan while")
while jumlah_baca < jumlah_buku + 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_buku_dipahami == 9:
        print(f"Buku ke {jumlah_buku_dipahami + 1 } belum paham")
    else:
        jumlah_buku_dipahami = jumlah_buku_dipahami + 1
        print(f"Buku ke {jumlah_buku_dipahami} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_dipahami}')

if jumlah_buku_dipahami == jumlah_buku:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {jumlah_buku_dipahami} buku"')
