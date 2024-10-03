# Rod Cutting / Connect 'n' ropes with minimal cost
def rodCutting(rodLen, rodPrices):
    # dp[i] will store the maximum profit for rod length i
    dp = [0] * (rodLen + 1)
    
    # Build the dp array in a bottom-up manner
    for i in range(1, rodLen + 1):
        max_val = float('-inf')
        # Check all possible cuts
        for j in range(i):
            max_val = max(max_val, rodPrices[j] + dp[i - j - 1])
        dp[i] = max_val
    
    return dp[rodLen]

n = 8
arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(rodCutting(n, arr))
