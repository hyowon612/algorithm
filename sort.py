import random, timeit


def quick_sort(A, first, last):
    if first >= last:
        return
    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    A[first], A[right] = A[right], A[first]
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)


def merge_sort(A, first, last):
    if first >= last:
        return
    merge_sort(A, first, (first+last)//2)
    merge_sort(A, (first+last)//2+1, last)
    merge_two_sorted_list(A, first, last)


def merge_two_sorted_list(A, first, last):
    m = (first + last)//2
    i, j = first, m+1
    B = []
    while i <= m and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    for k in range(i, m+1):
        B.append(A[k])
    for k in range(j, last+1):
        B.append(A[k])
    for i in range(first, last+1):
        A[i] = B[i - first]


def heap_sort(A):
    n = len(A)
    for i in range(n-1, -1, -1):
        heapify_down(A, i, n)

    for i in range(len(A)-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        n -= 1
        heapify_down(A, 0, n)
    
    
def heapify_down(A, k, n):
    while 2*k+1 < n:
        L, R = 2*k+1, 2*k+2
        if L < n and A[L] > A[k]:
            m = L
        else:
            m = k
        if R < n and A[R] > A[m]:
            m = R
        if m != k:
            A[k], A[m] = A[m], A[k]
            k = m
        else:
            break


def check_sorted(A):
    for i in range(n-1):
        if A[i] > A[i+1]:
            return False
    return True


Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
