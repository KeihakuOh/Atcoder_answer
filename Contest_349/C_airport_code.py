S = str(input())
T = str(input())
index = 0
if T[-1] == 'X':
    target = T[:-1].lower()
else:
    target = T.lower()
count = 0
index = 0
for i in range(len(target)):
    for j in range(len(S)):
        if target[i] == S[j] and j >= index:
            count += 1
            index = j + 1
            break
if len(target) == count:
    print("Yes")
else:
    print("No")