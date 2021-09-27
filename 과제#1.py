import time, random


def evaluate_n2(A, x):
	result = 0
	for i in range(len(A)):
		a = A[i]
		num = 1
		for j in range(i):
			num *= x
		result += a * num
	return result


def evaluate_n(A, x):
	result = 0
	num = 1
	for i in A:
		result += i * num
		num *= x
	return result


random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = []
for i in range(n):
	A.append(random.randint(-1000, 1000))

x = random.randint(-1000, 1000)

s = time.process_time()
print(evaluate_n2(A, x))
e = time.process_time()
print(e-s)

s = time.process_time()
print(evaluate_n(A, x))
e = time.process_time()
print(e-s)
