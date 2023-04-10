h,m=(map(int,input().split()))
sum=h*60+m
sum-=45
if sum>1440:
    sum-=1440
if sum<0:
    sum+=1440
h=int(sum/60)
m=sum%60
print(h,m)