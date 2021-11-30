def A(n):
    result = 0
    k = 0
    for i in range(1, n):
        if list[i][0] > list[k][1]:
            result += 1
            k = i
            if i == n-1:
                result += 1

    if k != n-1:
        result += 1
    return result


n = int(input())
list = []

for i in range(n):
    list.append([int(x) for x in input().split()])
list.sort(key=lambda x: (x[-1], -x[0]))

print(list)
print(A(n))