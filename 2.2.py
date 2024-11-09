a_betus_szavak = []
a_szo = None

print('Adj meg egy a-val kezdődő szót, ha nem a-val kezdődik a szó nem tárollom el, ha pedig entert nyomsz vége! ')

while a_szo != '':
    a_szo = input('Adj meg egy szót! ')

    if a_szo == '':
        break
    elif (a_szo[0]) == 'a' or (a_szo[0]) =='A':
        a_betus_szavak.append(a_szo)

print(a_betus_szavak)