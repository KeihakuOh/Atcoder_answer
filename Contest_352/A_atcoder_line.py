N, X, Y, Z = map(int, input().split(" "))
if X < Y:
    if Z >= X and Z <= Y:
        print("Yes")
    else:
        print("No")
else:
    if Z >= Y and Z <= X:
        print("Yes")
    else:
        print("No")