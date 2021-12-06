def homerseklet (C):
    if C < 0 :
        print ('-foksz van tesomsz')
    elif C <= 0 :
        print ('0 foksz van most')
    elif  C >= 100:
        print('nagy foksz van tesomsz')

for x in range (-20,121,20):
    print (x,"c",)
    homerseklet (x)