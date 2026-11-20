import math
with open('34.txt') as t:
    sp=[[int(i) for i in k.split()]for k in t]
n=0
count=0
for i in sp:
    n+=1
    if max(i)+min(i)<sum(i)-min(i)+max(i):
        count+=1
print(count)
