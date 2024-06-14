import numpy as np

def main():
    x=get_input()
    while len(x)>1:
        x=series(x)
        x=parallel(x)

    print(x[0])

def get_input():
    x=int(input("Enter the number of resistors "))
    n=0
    out=[]
    while n <x :
        r=input("Enter the resistor info ").split()
        de=check_in(r)
        if de==True:
            out.append([int(i) for i in r])
            n+=1

    return out

def parallel(x):
    for i in x[::-1] :
        for j in x[x.index(i)+1:] :
            if i[0:2]==j[0:2]:
                res=1/i[2]+1/j[2]
                res=round(1/res,1)
                x.remove(i)
                x.remove(j)
                x.append([i[0],i[1],res])
                return parallel (x)
    return x

def series(x) :
    arr=np.array(x)
    y=list (arr[:,0])
    z=list (arr[:,1])

    for i in x[::-1]:
        for j in x:
            if i[1]==j[0] and y.count(j[0]) ==1 and z.count(j[0])==1:
                n=[i[0],j[1],i[2]+j[2]]
                x.append(n)
                x.remove(i)
                x.remove(j)
                return series(x)
    return x

def check_in(x):
    if len(x)!=3:
        return False
    for i in x:
        if i.isnumeric()==False:
            return False
        elif int(i)<0:
            return False
    return True

if __name__=="__main__" :
    main()
