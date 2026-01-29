import random
#Her günün ortalama değerine tutmak için.
ortalamaDegerler = []
for gun in range(1,5+1):
    gunDegerleri = []
    for volts in range(1,6+1):
        sensor = random.randint(3,5)
        gunDegerleri.append(sensor)
    print(gun,".Gün Değerleri: ", gunDegerleri)
    #Her günün ortalama değerini hesaplıyoruz.
    ortalam = sum(gunDegerleri)/len(gunDegerleri)
    #Değeri ilk lisetemize ekleyip sonrada ekrana yazıyoruz.
    ortalamaDegerler.append(ortalam)
    print(gun,".Günün Ortalaması", sum(gunDegerleri))

print("Ortalama Değerler: ",ortalamaDegerler)
# Sum->bir listenin tum değerlerini topluyor.   len-> bir listenin element sayısını buluyor. (toplam/elemenSayısı = Ortalam)
ortalam = sum(ortalamaDegerler) / len(ortalamaDegerler)
print("Toplam Ortalama Değeri: ",ortalam)