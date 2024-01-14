# 나의 풀이
while True:
  try:
    print(input())
  except EOFError:
    break

# for문 이용
import sys
for line in sys.stdin:
    print(line, end="")

# read() 이용
import sys
print(sys.stdin.read())

# open(0) 이용
print(open(0).read()) # open(0).read() == sys.stdin.read()
