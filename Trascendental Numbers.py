import numpy as np
p=int(input('Max coefficient (integer): '))
n=float(input('Number to approximate:'))
def frac(x):
    return x - np.floor(x)
n1=np.pi
n2=np.exp(1)
n3=np.sqrt(2)
v1=(np.arange(p))*n1
v2=(np.arange(p))*n2
v3=(np.arange(p))*n3
M=np.add.outer(np.add.outer(v1,v2),v3)
Dif = np.minimum(abs(frac(n)-frac(M)),1-abs(frac(n)-frac(M)))
i,j,k=np.where(Dif == Dif.min())
x=np.asarray(i).item()
y=np.asarray(j).item()
z=np.asarray(k).item()
C= np.round(n-(x*n1+y*n2+z*n3))
n_aprox=x*n1+y*n2+z*n3+C
print('{} is approximately {}pi + {}e + {}sqrt(2) + {} = {}'.format(str(n),str(x),str(y),str(z),str(C),str(n_aprox)))
