# for문 사용(나의 풀이)
N = int(input())
n = list(map(int, input().split()))
v = int(input())

count = 0
for i in n:
  if i == v:
    count += 1
print(count)


-------------------------------------------
# count() 사용(메모리 적은 풀이)
N = int(input())
n = list(map(int,input().split()))
v = int(input())
print(n.count(v))
