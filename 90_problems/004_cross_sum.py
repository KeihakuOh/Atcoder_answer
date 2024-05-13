N, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * K for _ in range(N)]
sum_row = [[0] for _ in range(N)]
sum_line = [[0] for _ in range(K)]

for i in range(N):
    sum_row[i][0] = sum(array[i])
for i in range(K):
    for j in range(N):
        sum_line[i][0] += array[j][i]
for i in range(N):
    for j in range(K):
        ans[i][j] = sum_row[i][0] + sum_line[j][0] - array[i][j]
        if j == K - 1:
            print(' '.join(map(str, ans[i])))
