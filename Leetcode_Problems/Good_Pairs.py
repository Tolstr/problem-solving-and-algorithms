#level1: Print amount of 1-ones from the list
# def func(nums):
#     pairs=[]
#     cntr=0
#     for i in nums:
#         if i ==1:
#             cntr=cntr+i
#     return cntr
#
# print(func(nums=[1,2,3,1,1,3])) #3

#level2: Print indexes that belongs to 1-ones
# def func(nums):
#     output=[]
#     for i in range(len(nums)):
#         # print (i,nums[i])
#         if nums[i]==1:
#             output.append(i)
#     return output
# print(func(nums=[1,2,3,1,1,3])) #(0,3,4)

##level3: Print first good pair from the list (0,3)
# def func(nums):
#     output=[]
#     ind=0
#     for i in range(len(nums)):
#         #print (i,nums[i])
#         if nums[i]==1:
#             output.append(i)
#         if len(output)==2:
#             break
#     return output
# print(func(nums=[1,2,3,1,1,3])) #(0,3)

# Level 4 (The Hardest)
# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
def func(l):
    output=[]
    for i in range(len(l)-1):
        for k in range(1,len(l)):
            if k > i:
                a=l[i]
                b=l[k]
                #print(l[i],l[k])
                if l[i]==l[k]:
                    output.append((i,k))
    return len(output)
print('4',func([1,2,3,1,1,3]))
# print('6',func([1,1,1,1]))
# print('0',func([1,2,3]))
#https://leetcode.com/problems/number-of-good-pairs/