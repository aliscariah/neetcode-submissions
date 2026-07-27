class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset=set(nums)

        largest=0
        for num in numset:
            if largest<num:
                largest=num

        for i in range(1,largest):
            if i not in numset:
                return i
        return largest+1
        