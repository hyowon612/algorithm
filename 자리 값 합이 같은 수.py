def solve(L, S):
    k = S
    result = 0
    if L == 1 or S == 1:
        return 1

    while k > 0:
        result += solve(L-1, k)
        k -= 1

    return result


L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)