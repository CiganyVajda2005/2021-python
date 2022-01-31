def kerulet (a,b):
    return (2*(a+b))
def terulet (a,b):
    return (a*b)
a= float (input("A oldal :"))
b= float (input("B oldal :"))
K=kerulet(a,b)
T=terulet (a,b)
print("a téglalap területe:{0} egyseg".format(terulet(a,b)))
print("a téglalap kerülete {0} egység. ".format(kerulet(a,b)))
