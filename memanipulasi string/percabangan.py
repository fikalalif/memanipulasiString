nilai = int(input('masukan nilai : '))
if nilai < 0 or nilai > 100:
    print('Eror : range 0 - 100')
    exit() # break dalam python
else:
    if nilai <= 100 and nilai > 80:
        print('anda mendapatkan nilai A')
    elif nilai <= 80 and nilai > 60:
        print('anda mendapatkan nilai B')
    elif nilai <= 60 and nilai > 40:
        print('anda mendapatkan nilai C')
    elif nilai <= 40 and nilai > 20:
        print('anda mendapatkan nilai D')
    elif nilai <= 20:
        print('anda mendapatkan nilai E')

                        
