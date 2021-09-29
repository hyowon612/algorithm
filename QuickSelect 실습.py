def QuickSelect(L, k):
    A, B, M = [], [], []
    p = L[0]
    for i in L:
        if i < p:
            A.append(i)
        elif i > p:
            B.append(i)
        else:
            M.append(i)
    if len(A) >= k:
        return QuickSelect(A, k)
    elif len(A) + len(M) < k:
        return QuickSelect(B, k - len(A) - len(M))
    else:
        return p


a = input().split()
k = int(a[1])
L = input().split()
L = list(map(int, L))

result = QuickSelect(L, k)
print(result)