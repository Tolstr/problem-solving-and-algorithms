# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
def func(n):
    output=[]
    cntr=0
    for i in n:
        cntr=cntr+i
        output.append(cntr)
    return output
print(func(n=[1,2,3,4])) #Output: [1,3,6,10]


















# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as
# runningSum[i] = sum(nums[0]…nums[i])
# # Input: nums = [1,2,3,4]
# # Output: [1,3,6,10]
# # Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# def func(nums):
#     cntr=0
#     sum=[]
#     for i in nums:
#         cntr=cntr+i
#         sum.append(cntr)
#     return sum
# print(func(nums=[1,2,3,4]))
