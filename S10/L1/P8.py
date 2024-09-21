# Maximum points you can obtain from cards
def maxPointsObtainFromCards(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints[:k])
    result = total
    for i in range(1, k + 1):
        total += cardPoints[-i] - cardPoints[k - i]
        result = max(result, total)
    return result

print(maxPointsObtainFromCards([1,2,3,4,5,6,1], 3))
print(maxPointsObtainFromCards([2,2,2], 2))
print(maxPointsObtainFromCards([9,7,7,9,7,7,9], 7))
