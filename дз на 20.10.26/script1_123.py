with open('123.txt') as t:
    sp=[[int(i) for i in k.split()]for k in t]
count=0
for i in sp:
    pov=[x for x in i if i.count(x)>=2]
    nepov=[x for x in i if i.count(x)==1]
    if len(pov)==0 and len(nepov)==6:
        if max(nepov)>sum(nepov)-max(nepov):
            count+=1
print(count)
