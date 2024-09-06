# Subsequences with sum K
def subSequences(ss, index, total, sum, output):
    if sum == total:
        output[0] += 1
        return
    
    if index == len(ss):
        return
    
    subSequences(ss, index+1, total, sum+ss[index], output)
    subSequences(ss, index+1, total, sum, output)

def subSequencesWithSumK(ss, total):
    output = [0]  # Use a list to hold the count
    subSequences(ss, 0, total, 0, output)
    return output[0]

ss = [1, 2, 3, 4, 5]
total = 5
print(subSequencesWithSumK(ss, total))
