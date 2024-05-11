N = int(input())
build = list(map(int, input().split()))
max = build[0]
for i in range(1, len(build)):
    if build[i] > max:
        print(i+1)
        max = build[i]    
        break
if max == build[0]:
    print("-1")