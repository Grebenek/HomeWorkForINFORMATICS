a=16**820-2**761+14
k=0
while a:
    if a%4==0:
        k+=1
    a=a//4
print(k)
