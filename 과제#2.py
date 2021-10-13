import heapq


def solve(A, k): # return k-th smallest key, 1 <= k <= n
    for i in range(k):
        result = heapq.heappop(A)
    return result


k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A) # A is now a min-heap
print(solve(A, k))

# for 루프에서 heapq의 내장함수를 이용해 k번만큼 pop을 해주고 리턴값을 result 변수에 저장해준다.
# for문이 끝나고 result 변수를 return 해주면 k번째로 작은 수가 리턴된다.
# heappop함수의 시간복잡도가 O(log n)이고 for문 안에 있으므로 총 O(nlogn)시간이 소요된다.

# 장점: 내장함수로 간단하게 코드 작성 가능
# 단점: O(nlogn)시간 필요