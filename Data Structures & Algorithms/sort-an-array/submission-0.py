class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp=[0]*len(nums)

        def mergesort(left,right):
            if left>=right:
                return
            mid=(left+right)//2
            mergesort(left,mid)
            mergesort(mid+1,right)
            merge(left,mid,right)
    
        def merge(left,mid,right):
            for x in range(left,right+1):
                temp[x]=nums[x]
            
            i=left
            j=mid+1
            k=left

            while i<=mid and j<=right:
                if temp[i]<=temp[j]:
                    nums[k]=temp[i]
                    k+=1
                    i+=1
                else:
                    nums[k]=temp[j]
                    k+=1
                    j+=1
            
            while i<=mid:
                nums[k]=temp[i]
                k+=1
                i+=1
            
            while j<=right:
                nums[k]=temp[j]
                j+=1
                k+=1

        mergesort(0,len(nums)-1)
        return nums

        

        