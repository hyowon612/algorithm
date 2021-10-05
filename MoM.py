def find_median_five(A):
    num = len(A)
    if A == 0:
        return None
    M = []
    for i in range(num):
        M.append(min(A))
        A.remove(min(A))
    median = int(num/2)
    if num % 2 == 1:
        return M[median]
    else:
        return (M[median-1]+M[median])/2


def MoM(A, k):
    if len(A) == 1: # no more recursion
        return A[0]
    i = 0
    S, M, L, medians = [], [], [], []
    while i+4 < len(A):
        medians.append(find_median_five(A[i: i+5]))
        i += 5
    if i < len(A) and i+4 >= len(A):
        medians.append(find_median_five(A[i:]))

    mom = MoM(medians, len(medians)//2)
    for v in A:
        if v < mom: S.append(v)
        elif v > mom: L.append(v)
        else: M.append(v)

    if len(S) >= k: return MoM(S,k)
    elif len(S)+len(M): return MoM(L,k-len(S)-len(M))
    else: return mom


n, k = (int(x)for x in input().split())
A = [int(x) for x in input().split()]
print(MoM(A, k))