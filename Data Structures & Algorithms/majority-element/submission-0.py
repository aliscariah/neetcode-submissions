class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dicts={}
        # for num in nums:
        #     if num in dicts:
        #         dicts[num]+=1
        #     else:
        #         dicts[num]=1
        
        # for num in dicts:
        #     if dicts[num]>(len(nums)//2):
        #         return num

        count=0
        candidate=nums[0]
        for i in range(0,len(nums)):
            if nums[i]==candidate:
                count+=1
            elif nums[i]!=candidate and count!=0:
                count-=1
            else:
                candidate=nums[i]
        return candidate

            
            
            
        