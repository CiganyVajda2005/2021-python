nyitva = int(input('hány óra van most? ')) 
if 8 < nyitva <= 16 :
    print (' a bót  nyitva')
    print (16-nyitva ,'ennyi időd van még oda érni')
else:
    print('bót zárva')  
    print( 32 - nyitva  , 'ennyi idő múlva nyit ki a bót')
