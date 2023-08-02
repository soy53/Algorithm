# 곱하기 혹은 더하기
# 풀이 방법 1(by me)
# n = input()

# result = 0

# for i in range(len(n)):
#   if result == 0 or result == 1:
#     result += int(n[i])
#   else:
#     result *= int(n[i])

# print(result)

# 풀이 방법2(by 이코테)
data = input()

result = int(data[0])

for i in range(1, len(data)):
  num = int(data[i])
  if num < 1 or result < 1:
    result += num
  else:
    result *= num

print(result)