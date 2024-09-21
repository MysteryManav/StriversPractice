# Max Consecutive Ones III
def maxConsecutiveOnesIII(A, K):
    i = 0
    for j in range(len(A)):
        if A[j] == 0:
            K -= 1
        if K < 0:
            if A[i] == 0:
                K += 1
            i += 1
    return j - i + 1
print(maxConsecutiveOnesIII([1,1,1,0,0,0,1,1,1,1,0], 2))
print(maxConsecutiveOnesIII([1,0,1,1,0], 1))
print(maxConsecutiveOnesIII([0,0,0,1], 4))
print(maxConsecutiveOnesIII([0,0,0,1], 3))
