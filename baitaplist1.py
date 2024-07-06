import random
n=int(input("nhap vao so phan tu:"))
lst=[0]*n
for i in range(n):
    lst[i]=random.randrange(1,101)
print(lst)