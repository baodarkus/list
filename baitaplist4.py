lst1=[]
n=int(input("nhap vao so phan tu cua list:"))
dem1=0
dem2=0
while dem1<n:
    dem1+=1
    a=int(input("nhap vao phan tu cua list:"))
    lst1.append(a)
print("mang ban vua nhap la:",lst1)
lst1_index=[]
for j in range(len(lst1)):
    if lst1[j]<5:
        dem2+=1
        lst1_index.append(j)
print(f"so phan tu nho hon 5 la {dem2}")
print(f"cac vi tri index cua nhung so do la {lst1_index}")

