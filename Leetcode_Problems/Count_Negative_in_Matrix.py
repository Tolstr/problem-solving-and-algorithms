# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
def func(m):
    cntr=0
    for i in m:
        for j in i:
            if j<0:
                cntr+=1
    return cntr
print(func(m=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))