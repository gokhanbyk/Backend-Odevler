# import random
# secenek = random.choice(('tas', 'kagit', 'makas'))
# print(secenek)

# input tas kagit makas
# input tas, secenek tas is print berabere
# input makas, secenek kagit print kazandınız

""" 1.ÖDEV 1
    ilk if ödeviniz: taş kağıt makas oyunu
    import ile random çekip .choice ile yukardaki yapıyla rastgele seçim yapabilirsiniz
    sonra input ile kendiniz bi değer girip pythonla tas kagit makas oynamanızı istiyorum
 """


""" 1. ÖDEV 2
    bir beden kitle indeksi hesaplama istiyorum hesabını aşağıda belirttim
    google a beden kitle indeksi hesapla yazarak hangi aralıklarda ne yazılması gerektiğini görebilirsiniz
    çektiğiniz inputlarda biri int biri float olacak
"""
# beden kitle indeksi
# beden kitle indeksi nasıl hesaplanır: kilo / (boy * boy)

#vücüt kitle endeksi
import math



boy = float(input('lütfen boyunuzu giriniz'))
kilo = int(input('lütfen kilonuzu giriniz'))
endeks = float(kilo / (boy * boy))
print(endeks)
if (endeks < 18):
    print('vücut kitle endeksiniz zayıf')
elif (endeks > 18 and  endeks < 25 ):
    print('vücut itle endeksiniz normal')
elif (endeks > 26 and endeks < 29 ):
    print('kilolusunuz') 
elif (endeks > 30 and endeks < 35):
    print('1. deree obezite') 
elif (endeks > 36 and endeks < 39):
    print('2. derece obezite')
else:
    print('acilen doktora müracat ediniz')


