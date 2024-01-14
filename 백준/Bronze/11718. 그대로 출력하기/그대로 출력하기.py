# 나의 풀이
while True:
  try:
    print(input())
  except EOFError:
    break

# for문 이용
for line in input():
    print(line, end="")
