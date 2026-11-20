import math
with open('12') as t:
    sp=[[int(i) for i in k.split()]for k in t]
n=0
count=0
for i in sp:
    n+=1
    pov=[x for x in i if i.count(x)>=2]
    nepov=[x for x in i if i.count(x)==1]
    if len(set([int] (pov))==1 and len(nepov)==4:
        if sum(nepov)/len(nepov)<=sum(pov):
            count+=1
print(count)
