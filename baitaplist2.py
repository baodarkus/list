lst=[]
n=int(input("nhap so phan tu cua list:"))
dem=0
while dem<n:
    dem+=1
    a=int(input("nhap vao phan tu:"))
    lst.append(a)
print("list vua nhap la:",lst)

lst2=[]
for i in lst:
    lst2.append(i**2)
    print("mang moi la:",lst2)

dem2=0
for i in lst2:
    if i>50:
        dem2+=1
print(f"list moi co {dem2} so lon hon 50")