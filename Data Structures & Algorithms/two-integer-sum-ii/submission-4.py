class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        k=0
        while i<len(nums):
            for k in range(1,len(nums)):
                if target==nums[i]+nums[k]and i!=k:
                    return [i+1,k+1]
            i+=1
        

        