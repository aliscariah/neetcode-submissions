class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        n=len(nums)

        for i in range(n):

            if nums[i]>0:
                break
            left=i+1
            right=n-1
            target=-nums[i]
            while left<right:
                curr=nums[left]+nums[right]
                if curr==target:
                    result.add((nums[i],nums[left],nums[right]))   
                    left+=1
                    right-=1
                elif curr>target:
                    right-=1
                else:
                    left+=1

        return [list(t) for t in result]    
                 

        