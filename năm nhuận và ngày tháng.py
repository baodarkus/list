def nam_nhuan(nam):
    if (nam%4==0 and nam%100!=0) or (nam%400==0):
        return True
    else:
        return False
nam=int(input("Nhap vao nam:"))
if nam_nhuan(nam):
    print(f"Nam {nam} la nam nhuan")
else:
    print(f"Nam {nam} la nam khong nhuan")

def ngay_cua_thang(thang):
    if thang in (1,3,5,7,8,10,12):
        return "a"
    elif thang ==2:
        if nam_nhuan(nam):
            return "b"
        else:
            return "c"
    else:
        return "d"

thang=int(input("nhap vao thang muon kiem tra:"))
ketqua=ngay_cua_thang(thang)
if ketqua == "a":
    print(f"thang {thang} co 31 ngay")
elif ketqua == "b":
    print(f"thang 2 nam {nam} la nam nhuan co 29 ngay")
elif ketqua == "c":
    print(f"thang 2 nam {nam} la nam khong nhuan co 28 ngay")
else:
    print(f"thang {thang} co 30 ngay")


