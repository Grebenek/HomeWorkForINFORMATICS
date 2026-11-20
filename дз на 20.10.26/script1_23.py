import math
with open('23.txt') as t:
    sp=[[int(i) for i in k.split()]for k in t]
n=0
count=0
for i in sp:
    n+=1
    if sum(i)==180 and i[0]>90 or i[1]>90 or i[2]>90:
        count+=1
print(count)
