K = int(input())
n = int(input())
list1 = [[int(x)] for x in input().split()]
list2 = [int(x) for x in input().split()]

for i in range(n):
    list1[i].append(list2[i])
list1.sort(key=lambda x: (x[1]), reverse=True)

size = []
profit = []
for i in list1:
    size.append(i[0])
    profit.append(i[1])

x = [0 for _ in range(n)]
MaxProfit = 0


def fractional_knapsack(n, size, profit, K):
    if K <= 0:
        return 0
    s = 0
    p = 0
    for i in range(n):
        if s + size[i] <= K:
            p += profit[i]
            s += size[i]
        else:
            # p += (K-s) * (profit[i]/size[i])
            # s = K
            break
    return p


def knapsack(i, T): # 남은 공간 : T
    global MaxProfit
    if i >= n or T <= 0:
        # print(x)
        return MaxProfit

    p = sum(profit[j] for j in range(n) if x[j] == 1)
    s = sum(size[j] for j in range(n) if x[j] == 1)

    x[i] = 1
    if s + size[i] <= K:
        B = fractional_knapsack(n-(i+1), size[i+1:], profit[i+1:], T-size[i])
        if B + p + profit[i] >= MaxProfit:
            MaxProfit = p + profit[i]
            knapsack(i+1, T-size[i])

    x[i] = 0
    B = fractional_knapsack(n-(i+1), size[i+1:], profit[i+1:], T)
    # if (p + B) >= MaxProfit:
    knapsack(i+1, T)

    return MaxProfit


# print(profit)
# print(size)
print(knapsack(0, K))