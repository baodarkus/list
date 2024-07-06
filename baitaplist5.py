lst=[]
n=int(input("nhap vao so phan tu cua mang:"))
dem=0
while dem<n:
    dem+=1
    a=int(input("nhap vao phan tu cua mang:"))
    lst.append(a)
print("mang ban vua nhap la",lst)
lst_max=[]
lst_min=[]
for i in lst:
    if i==max(lst):
        continue
    else:
        lst_max.append(i)
    if i==min(lst):
        continue
    else:
        lst_min.append(i)
print("gia tri lon thu 2 trong list vua nhap la",max(lst_max))
print("gia tri nho thu 2 trong list vua nhap la",min(lst_min))
lst_index=[]
for j in range(len(lst)):
    if lst[j]==max(lst_max):
        lst_index.append(j)
    if lst[j]==min(lst_min):
        lst_index.append(j)
print(lst_index)



