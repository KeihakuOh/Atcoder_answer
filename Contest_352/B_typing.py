S = str(input())
T = str(input())
s = 0
count=[]
for i in range(len(T)):
    if T[i] == S[s]:
        count.append(i+1)
        s += 1
print(' '.join(map(str, count)))
