class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        k=n//3

        for i in range(0,n):
            if nums[i] not in result:
                j=i+1
                count=1
                while j<n:
                    if nums[i]==nums[j]:
                        count+=1 
                    j+=1 
                if count>k:
                    result.append(nums[i])
        return result    