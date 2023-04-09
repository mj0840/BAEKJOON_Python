sum=0
index=0
for i in range(9):
    num=int(input())
    if sum<num:
        sum=num
        index=i+1
print(sum, index)