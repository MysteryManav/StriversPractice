# Subsequences with sum K
def subSequences(ss, index, total, sum):
    if sum == total:
        return True
    
    if index == len(ss):
        return
    
    if subSequences(ss, index+1, total, sum+ss[index]):
        return True
    if subSequences(ss, index+1, total, sum):
        return True

    return False

def subSequencesWithSumK(ss, total):
    return subSequences(ss, 0, total, 0)


ss = [1, 2, 3, 4, 5]
total = 5
print(subSequencesWithSumK(ss, total))
