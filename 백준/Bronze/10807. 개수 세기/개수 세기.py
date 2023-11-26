N = int(input())

n = list(map(int, input().split()))

v = int(input())

count = 0
for i in n:
  if i == v:
    count += 1
print(count)