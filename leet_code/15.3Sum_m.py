# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# key:The idea is to sort an input array and then run through all indices of a possible first element of a triplet.
#  For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the
# array. Also we want to skip equal elements to avoid duplicates in the answer without making a set or smth
# like that.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        if len(nums)<3:
            return []
        for i in range (len(nums)):
            # if the element is same with the former one, we move to the next one
            # since this situation has already been considered
            # note that it is very import to have i>0, since nums[-1] also exists
            if i >0 and nums[i]==nums[i-1]:
                continue
            else:
                left, right=i+1,len(nums)-1
                while left<right:
                    s=nums[i]+nums[left]+nums[right]
                    if s>0:
                        right-=1
                    elif s<0:
                        left+=1
                    else:
                        result.append([nums[i],nums[left],nums[right]])
                        #next move the cursor if the value of left and right is
                        #same
                        # here should be careful that left should be less than
                        #len(nums)-1 and right should be greater than 1
                        while left< len(nums)-1 and nums[left+1]==nums[left]:
                            left+=1
                        while right >1 and nums[right-1]==nums[right]:
                            right-=1
                        left+=1
                        right-=1
        return result


#
# def main():
#     s="   +123"
#     sln=Solution().myAtoi(s)
#     print(sln)
#
# if __name__=="__main__":
#     main()