S = input()
N = int(input())
p = list(map(int, input().split()))

T = ""

for i in range(0, N):
    T += "a" * p[i] + " "

print((S) + " " + (T))
