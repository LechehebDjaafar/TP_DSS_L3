##ks table fun rec 1 table
table = ['a','b','c','d',"e","f","g","h","i","j"]

def mimer(table,n):
    x=len(table)
    if (x)%2 == 0:
        if x//2 == n :
            return table
        z=table[x-n]
        table[x-n]=table[n-1]
        table[n-1]=z
        return mimer(table,n-1)
    else:
        if x//2 == n+1 :
            return table
        z=table[x-n]
        table[x-n]=table[n-1]
        table[n-1]=z
        return mimer(table,n-1)
        


print(mimer(table,len(table)))