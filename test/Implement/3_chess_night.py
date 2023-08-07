n = input()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if 1 <= next_row <=8 and 1 <= next_column <=8:
    count += 1

print(count)