class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos=0
        n=len(nums)
        while pos!=n:
            for i in range(pos+1,n):
                if target==nums[pos]+nums[i]:
                    return [pos,i]
            pos+=1
        
                    