
def two_sum(X, Y, t):
    H = {}
    for val in Y:
        H[val] = 0
    for i in X:
        if -t-i in H:
            return True
    return False


A = input().split()
B = input().split()
C = input().split()

A = list(map(int, A))
B = list(map(int, B))
C = list(map(int, C))

result = "False"

for i in C:
    if two_sum(A, B, i) == True:
        result = "True"
        break
print(result)

# 파이썬의 딕셔너리는 Hash table의 형태를 가지므로 H라는 빈 딕셔너리를 만들어 Y의 원소를 키 값으로 H에 넣어준다.
# 수행시간은 O(n)이다.
# for 루프를 이용해 X의 원소 중 -t에 X의 원소를 뺀 값이 H에 있는지 확인하고 있다면 True를 리턴한다.
# 이의 수행시간 역시 O(n)이다.
# 그러므로 함수 Two_sum의 수행시간은 O(n)이다.
#
# 마지막으로 C의 원소와도 비굘르 해야하므로 for루프를 이용해 for문 안에서 two_sum 함수를 호출해준다.
# 이 과정의 수행시간은 O(n^2)이다.
# 그러므로 세 개의 리스트 A, B, C에 대해 a + b + c = 0이 되는 쌍이 존재하는지 O(n^2)시간 안에 확인할 수 있다.