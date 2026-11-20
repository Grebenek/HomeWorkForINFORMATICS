mn=9999
for i in range(1,2000):
    b=bin(i)[2:]
    b=str(b)[::-1]
    r=int(b,2)
    if i>100 and i<mn and r==7:
        mn=i
print(mn)
