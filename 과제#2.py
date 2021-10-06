import heapq


def solve(A, k): # return k-th smallest key, 1 <= k <= n
    for i in range(k):
        result = heapq.heappop(A)
    return result

k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A) # A is now a min-heap
print(solve(A, k))