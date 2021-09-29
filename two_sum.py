
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