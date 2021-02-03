# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# iteration through the main list
# take from the list first element that is another list?
# iterate that nested list and add elements to the summ
# compare two summs
def func(l):
    max=0
    for i in l:#1 iteration in [1,2,3], 2nd Iteration [3,2,1]
        sum=0
        for j in i:#iteration1 in 1,2,3 2nd iteration  3,2,1
            sum+=j
            if sum>max:
                max=sum
    return max
print(func(l=[[1,2,3],[3,2,2]]))