def upside_down_analiz(enerji):
    toplam = 0
    mini = enerji[0]
    maxi = enerji[0]
    for i in enerji:
        toplam += i
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    ortalama = toplam / len(enerji) #Yine Len element sayısını bulmak için kullanıyoruz.
    print("Toplam: ",toplam)
    print("Min: ",mini)
    print("Max: ",maxi)
    print("Ortalam: ",ortalama)

    if ortalama >= 25:
        print("Upside Down kapısı açılmak üzere!")
    else:
        print("Hawkins bugün güvende.")

enerji = [12, 18, 25, 30, 28, 22, 35, 40, 38, 20, 15, 10, 5,51]
upside_down_analiz(enerji)