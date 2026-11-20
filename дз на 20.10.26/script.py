import itertools as t
k=0
s=[]
for i in t.product([tuple[str, ...]] (sorted('АКЛМНЯ'),repeat=5):
    k+=1
    if i[0]=='N' and i[1]=='H':
        s.append(k)
print(s[-1]-s[0]-1)
