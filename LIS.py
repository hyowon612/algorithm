def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]:
            print(seq[i], end="")
        else:
            print("_", end="")
    print()


# def LIS_DP(seq):
#     x = [0] * len(seq)
#     DP = [0] * len(seq)



# seq = input()
# lis, x = LIS_DP(seq)
# print(lis)

print_IS("abcabc", [1, 0, 0, 0, 0, 0])