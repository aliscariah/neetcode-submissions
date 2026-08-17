class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:

        l=0
        r=len(nums)-1
        while r-l>=k:
            leftval=x-nums[l]
            rightval=nums[r]-x
            if leftval>rightval:
                l+=1
            else:
                r-=1
        print (l,r)
        return nums[l:r+1]


        