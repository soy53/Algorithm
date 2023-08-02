# 모험가길드 - 모험을 떠나는 그룹 수의 최대값 구하기
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0     # count 초기화

print(result)