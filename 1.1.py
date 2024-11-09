iras_jel=input('Adj meg egy mondatot, írásjellel a végén! ')

if (iras_jel[-1])=='.':
    print('Kijelentő mondat')
elif (iras_jel[-1])=='?':
    print('Kérdő mondat')
elif (iras_jel[-1])=='!':
    print('Felkiáltó / felszólító / óhatjtó mondat')