def A(n):
    result = [0]*30
    for i in range(n):
        for j in range(list[i][0], list[i][1]+1):
            result[j] += 1
    return max(result)


n = int(input())
list = []

for i in range(n):
    list.append([int(x) for x in input().split()])
list.sort(key=lambda x: (x[-1], -x[0]))


print(A(n))