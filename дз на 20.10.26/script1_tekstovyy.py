import math
with open('Текстовый документ.txt') as t:
    sp=[[int(i) for i in k.split()]for k in t]
n=0
count=0
for i in sp:
    n+=1
    if i[0]%2!=i[1]%2!=i[2]%2!=i[3]%2!=i[4]%2!=i[5]%2!=i[6]%2:
        pov=[x for x in i if i.count(x)>=2]
        nepov=[x for x in i if i.count(x)==1]
        if 3*sum(nepov)>=math.prod(pov):
            count+=n
print(count)
