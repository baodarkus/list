import math
def giai_bt_bac_2(a,b,c):
    delta=(b*b)-(4*a*c)
    if a!=0:
        if delta>0:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            return (x1,x2)
        elif delta==0:
            x=(-b)/(2*a)
            return x
        else:
            return "vo nghiem"
    else:
        if b!=0:
            x=(-c)/b
            return x
        else:
            if c!=0:
                return "vo nghiem"
            else:
                return "vo so nghiem"

a=float(input("nhap vao he so a:"))
b=float(input("nhap vao he so b:"))
c=float(input("nhap vao he so c:"))
print(giai_bt_bac_2(a,b,c))

