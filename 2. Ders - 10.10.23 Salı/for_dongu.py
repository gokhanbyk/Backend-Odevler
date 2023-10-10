for i in range(0,10):
    print(i)

isim = 'Gökhan'
for i in isim:
    print(i)

sayilar = [1, 2, 3, 4, 5, 6]
for sayi in sayilar:
    print(sayi)

for yazi in sayilar:
    print('merhaba')

isimler = ['Gökhan', 'Ahmet', 'Mehmet', 'Ali']

for isim in isimler:
    print(isim)

for i in range(20,0,-5):
    print(i)
# 20den 0

numbers = [5, 10, 1, 35,22, 57, 72]
print('*' *30)
for sayi in numbers:
    if sayi % 5 == 0:
        print(sayi)
print('*' *30)

toplam = 0
for i in numbers:
    toplam += i
print(toplam)

urunler = ['laptop', 'telefon', 'bilgisayar', 'telefon', 'telefon']
for urun in urunler:
    print(urun[1])
print('*' *30)

count = 0
for urun in urunler:
    if urun == 'telefon':
        count += 1

print(f'Telefon modelinden {count} adet var')


# isalpha -> stringim içinde harflar alfabetik

# metin = 'deneme'
# print(metin.isalpha())


# kullanıcıdan bir metin alalım 
# girdiği metinde kaç tane harf olduğunu öğrenelim
# girdiği metinde harf dışında sayi girdiyse harf saymıyım

metin = input('metin girelim: ')
harf_sayim = 0

for harf in metin:
    if harf.isalpha():
        harf_sayim += 1

print(harf_sayim)