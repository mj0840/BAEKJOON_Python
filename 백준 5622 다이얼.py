sum = 0
s = list(input())
for i in range(len(s)):
    tmp = ord(s[i])
    if tmp >=65 and tmp <= 67: sum += 3
    elif tmp >= 68 and tmp <= 70: sum += 4
    elif tmp >= 71 and tmp <= 73: sum += 5
    elif tmp >= 74 and tmp <= 76: sum += 6
    elif tmp >= 77 and tmp <= 79: sum += 7
    elif tmp >= 80 and tmp <= 83: sum += 8
    elif tmp >= 84 and tmp <= 86: sum += 9
    elif tmp >= 87 and tmp <= 90: sum += 10
print(sum)