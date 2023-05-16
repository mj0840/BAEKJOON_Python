sum = [-1] * 26
tmp = 0
s = list(input())
for i in range(len(s)):
    tmp = ord(s[i])
    if sum[tmp - 97] == -1:
        sum[tmp - 97] = i
for i in range(26):
    print(sum[i], end=" ")