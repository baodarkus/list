from math import sqrt
quest=["2+5+7=","5*10=","sqrt(16)=","12%2=","5//2="]
for i in quest:
    k=i.strip("=")
    ans=eval(k)
    traloi=float(input(i))
    if traloi==ans:
        print("correct")
    else:
        print(f"wrong,the answer is {ans}")
