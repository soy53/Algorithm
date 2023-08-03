# 상하좌우
n = int(input())
plans = list(input().split())

x, y = 1, 1

dx = [-1, 1, 0, 0] # 위, 아래, 왼, 오
dy = [0, 0, -1, 1] # 위, 아래, 왼, 오
move_types = ['U', 'D', 'L', 'R']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      
  if nx < 1 or ny < 1 or nx > n or ny > n:
      continue          # 공간을 벗어나면 적용 x     
  
  x, y = nx, ny

print(x, y)