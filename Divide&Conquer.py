def max_sum(A, left, right):
    middle = (left + right)//2

    if left == right:
        return A[left]

    result = 0
    a = A[middle]
    for i in range(middle, left-1, -1):
        result += A[i]
        a = max(a, result)

    result = 0
    b = A[middle+1]
    for i in range(middle+1, right+1):
        result += A[i]
        b = max(b, result)

    first = max_sum(A, left, middle)
    second = max_sum(A, middle+1, right)
    third = a + b

    return max(first, second, third)


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)

