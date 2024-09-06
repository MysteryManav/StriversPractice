# Subset Sum - 1
def subsetSum(ss, sum, index):
    if index == len(ss):
        answer.append(sum)
        return
    
    subsetSum(ss, sum+ss[index], index+1)
    subsetSum(ss, sum, index+1)

answer = []
ss = [1, 2, 3]
sum = 0
subsetSum(ss, sum, 0)
print(answer)
