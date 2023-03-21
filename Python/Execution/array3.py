A = [1, 2, 3, 4]
B = 7

for i in range(0,4):
    for j in range(0,4):
        if i!=j:
            if A[i] + A[j] == B:
                print("1")

