# N이 1이 되는데 1번, 2번 연산을 수행하는데 걸리는 최소 횟수를 구하시오.
# 1번 연산 : N에서 1을 빼기 / 2번 연산 : N에서 K 나누기
n, k = map(int, input().split())

result = 0

# 반복문을 사용하면 시간복잡도가 줄어든다.
while True:
  target = (n // k) * k # n이 k로 나누어 떨어지는 가장 가까운 수 찾기
  result += (n - target) # n - target = 1로 빼야하는 횟수
  n = target 
  # n이 k보다 작으면(더이상 나눌 수 없으면) 반복문 탈출
  if n < k:
    break
  # 그렇지 않다면 n을 k로 나누기
  result += 1 # 나눈거 연산 1회 추가
  n //= k

result += (n - 1) # n이 1보다 크다면 n이 1이 될 수 있도록 하기 위해서 마지막으로 남은 수에 대해 1씩 빼기
print(result)

# n % k == 0이면 다시 나눠주고 n % k != 0이면 1을 빼주는 방식도 존재. but n과 k가 커졌을 때 시간복잡도가 무수히 늘어나게 된다.