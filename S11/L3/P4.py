# Maximum Sum Combination
import heapq

def maxSum(A, B, C):
    # Sort both arrays in descending order
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    # Max heap to store sums, negative values because heapq is a min-heap by default
    max_heap = []
    
    # Set to keep track of visited indices
    visited = set()
    
    # Push the largest possible sum with the indices (0, 0)
    heapq.heappush(max_heap, (-(A[0] + B[0]), 0, 0))
    visited.add((0, 0))
    
    result = []
    
    # Extract the top C sums
    for _ in range(C):
        current_sum, i, j = heapq.heappop(max_heap)
        result.append(-current_sum)  # Append the actual positive sum
        
        # Push the next combination from the same row (A[i+1], B[j]) if not visited
        if i + 1 < len(A) and (i + 1, j) not in visited:
            heapq.heappush(max_heap, (-(A[i + 1] + B[j]), i + 1, j))
            visited.add((i + 1, j))
        
        # Push the next combination from the same column (A[i], B[j+1]) if not visited
        if j + 1 < len(B) and (i, j + 1) not in visited:
            heapq.heappush(max_heap, (-(A[i] + B[j + 1]), i, j + 1))
            visited.add((i, j + 1))
    
    return result

A = [3, 2]
B = [1, 4]
C = 2
print(maxSum(A, B, C))
print(A)
print(B)

A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C = 4
print(maxSum(A, B, C))
print(A)
print(B)
