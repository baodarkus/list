
for num in range(1,1001):
    s=0
    for i in range(1,num):
        if num%i==0:
            s+=i
    if num==s:
        print(f"{num} la so hoan thien")
