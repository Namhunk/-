import sys

N, k = map(int, sys.stdin.readline().strip().split())
x = list(map(int, sys.stdin.readline().strip().split()))
x = sorted(x)
print(x[-k])