# Hand of Straights
from collections import Counter
import heapq

def handOfStraights(hand, groupSize):
    hand_size = len(hand)
    if hand_size % groupSize != 0:
        return False
    cardCount = Counter(hand)
    min_heap = list(cardCount.keys())
    heapq.heapify(min_heap)
    while min_heap:
        currentCard = min_heap[0]
        for i in range(groupSize):
            if cardCount[currentCard + i] == 0:
                return False
            cardCount[currentCard + i] -= 1
            if cardCount[currentCard + i] == 0:
                if currentCard + i != heapq.heappop(min_heap):
                    return False
    return True

print(handOfStraights([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(handOfStraights([1, 2, 3, 4, 5], 4))
print(handOfStraights([8, 10, 12], 3))
print(handOfStraights([2, 3, 1], 3))
