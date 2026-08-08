class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        # v=0
        # pro=0

        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if heights[i]<heights[j]:
        #             pro=heights[i]*(j-i)
        #         else:
        #             pro=heights[j]*(j-i)
        #         v=max(v,pro)
        # return v 

        left=0
        right=n-1
        v=0
        prod=0
        

        while left<right:
            v=min(heights[left],heights[right])
            width=right-left
            prod=max(prod,width*v)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1

        return prod
            

        