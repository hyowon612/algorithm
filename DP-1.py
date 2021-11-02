def make_ascending(A):
    n = len(A)
    DP = [[-1]*201 for _ in range(n)]   # 201 x n 개수의 이중 배열을 만들어서 -1로 채운다.

    def get_min_try(i, prev):
        if i > 0 and DP[i][prev] >= 0:  # 이전에 이미 계산한 최소 값이 있으면 DP에서 저장된 최소값을 바로 리턴한다.
            return DP[i][prev]

        minv = 99999999999999
        if i == n-1:    # 마지막 노드이면 +1 -1 횟수만 계산한다.
            return abs(A[i] - prev)

        count_inc = 0
        prev_now = 0
        for j in range(prev, 201):
            now = abs(A[i] - j) + get_min_try(i + 1, j) # 현재 노드를 j로 변경했을 때 현재 노드의 +1 -1 횟수 + 다음 노드의 최소 계산 횟수
            if now < minv:  # 지금까지의 최소 횟수와 비교해서 최소값이면 교체
                minv = now
                count_inc = 0
            elif now > prev_now:
                count_inc += 1
            prev_now = now
            if i > 0 and count_inc > 1: # 최소값이 점점 증가하면 더이상 해볼 필요가 없다.
                break

        if i>0: # 0번째 노드는 나중에 사용될 일이 없으므로 DP에 저장할 필요가 없다.
            DP[i][prev] = minv  # 한번 계산한 최솟값은 DP에 저장한다.
        return minv

    result = get_min_try(0, 1)
    return result


# 인덱스 1부터 n까지 2~200번의 연산을 하는데 이는 O(kn)이라고 할 수 있다.
# 그러므로 시간복잡도는 O(n)이다.