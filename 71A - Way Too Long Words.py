#71A - Way Too Long Words


n = input()
for i in range(100):
    x = input()
    
    if len(x)>10:
        l1= str(x[0])
        l2 = str(x[len(x)-1])
        l3= str(len(x)-2)
        print(l1+l3+l2)
    else:
        print(x)   
    