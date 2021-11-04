def solve(A):
    DP = [0] * len(A) # DP는 특정 정수 j가 포함된 인덱스 쌍에 대해 m(i, j)의 합을 계산해 append하는 리스트다.
    DP[0] = A[0]
    list = [A[0]]

    for i in range(1, len(A)):
        list.append(A[i])
        if A[i] >= A[i-1]: # 직전 인덱스의 정수 값보다 클때
            DP[i] = DP[i-1] + A[i] # 직전 index의 DP값에 A[i]를 더한 값과 같다.
        else:
            min_num = min(list)
            if min_num == A[i]: # A[i]가 현재까지의 인덱스 중 최소값일때
                DP[i] = A[i] * (i+1) # A[i]를 길이만큼 곱한 값과 같다.
            else: # 직전 인덱스의 정수값보다 작되 최소값이 아닐때
                k = i
                while A[k] >= A[i]: # A[i]부터 반대로 리스트를 돌며 정수값이 처음으로 감소하는 인덱스를 찾는다
                    k -= 1
                n = i - k
                DP[i] = DP[i - n] + A[i] * n # 정수가 처음으로 감소하는 인덱스의 DP값에 그 인덱스와 i의 차 만큼 A[i]를 곱해서 더한다.
    return sum(DP)


A = [int(x) for x in input().split()]
print(solve(A))

# n만큼 for 루프를 돌며 연산을 하기 때문에 평균 수행시간은 O(n)이지만
# 최악의 경우 수행시간은 O(n^2)이다.
