def temp (C):
    if C < 0 :
        print ('-foksz van tesomsz')
    elif C <= 0 :
        print ('0 foksz van most')
    elif  C >= 100:
        print('nagy foksz van tesomsz')
    else: 
        print('jó foksz van') 

for C in range (-20,121,20):
    print (C,"C " , end="")
    temp(C)