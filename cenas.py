cenas = [2000, 5000, 2500, 9000, 10000, 23900, 70000, 1900]
nobraukumi = [300000, 280000, 290000, 200000, 170000, 120000, 5000, 406000]

a = 0

avgCena = sum(cenas)/len(cenas)
avgNobr = sum(nobraukumi)/len(nobraukumi)
avgKoef = avgNobr/avgCena
print("If any coefficient is higher than the average one, then we shall call it a good deal \nAvg cena:", avgCena, "\nAvg mileage: ", avgNobr, "\nAvg koef: ", avgKoef)

while a < len(cenas):
    x = (nobraukumi[a]/cenas[a])
    print("Coef", a+1,": ", x)
    a = a + 1
