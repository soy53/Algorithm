chess_count = [1, 1, 2, 2, 2, 8]
chess_list = list(map(int, input().split()))

for i in range(len(chess_list)):
  print(chess_count[i] - chess_list[i], end=' ')