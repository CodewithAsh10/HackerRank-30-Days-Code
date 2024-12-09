# Question - Slicing s string
n = int(input())
for i in range(n):
    s=input()
    print(s[0:len(s):2],end=" ")
    print(s[1:len(s):2])
