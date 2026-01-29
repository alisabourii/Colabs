import random

piyango = []
for i in range(1,5+1):
    rnd = random.randint(1,9)
    piyango.append(rnd)

bilet = []
for i in range(1,5+1):
    rnd = random.randint(1,9)
    bilet.append(rnd)

eslesmeSayisi = 0
for i in bilet:
    if i in piyango:
        eslesmeSayisi += 1

if eslesmeSayisi == 3:
    print("Ödül: 100TL")
elif eslesmeSayisi == 4:
    print("Ödül: 1000TL")
elif eslesmeSayisi == 5:
    print("Ödül: 10000TL")
else:
    print(eslesmeSayisi," doğru sayınız var ulan!!!!!!")