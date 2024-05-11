N, K = map(int, input().split())
groups = list(map(int, input().split()))
starts = 0
seats_available = K
for people in groups:
    if people > seats_available:
        starts += 1
        seats_available = K - people  
    else:
        seats_available -= people
starts += 1

print(starts)