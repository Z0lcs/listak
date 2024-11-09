gyumolcsok = []

while True:
    gyumolcs = input('Adj meg egy gyümölcsöt! ')

    if gyumolcs == "vége":
        break
    elif gyumolcsok.count(gyumolcs) < 1:
        gyumolcsok.append(gyumolcs)
    else:
        print('Van már ilyen gyümölcs tárolva!')

for gyumolcs in reversed(gyumolcsok):
    print(gyumolcs, end=", ")

