n = int(input())
for i in range(n):
    cnt, s = input().split()
    cnt = int(cnt)
    for j in range(len(s)):
        print(s[j] * cnt, end="")
    print("")