N = int(input())
giants = []

for _ in range(N):
    a, b = map(int, input().split())
    giants.append((b - a, a, b))

giants.sort()

max_height = 0
current_height = 0

for diff, shoulder, head in giants:
    current_height += shoulder  
    max_height = max(max_height, current_height + head - shoulder) 
print(max_height)