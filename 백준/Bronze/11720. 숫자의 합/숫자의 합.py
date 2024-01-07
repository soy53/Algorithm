# 나의 풀이
n = int(input())
number = input()
sum = 0

for i in number:
  sum += int(i)

print(sum)

# sum() 함수 사용
n = input()
print(sum(map(int,input())))
