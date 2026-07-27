class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # output=0
        # for i in range(0,len(nums)):
        #     j=i
        #     count=0
        #     while j<len(nums):
        #         count+=nums[j]
        #         if count==k:
        #             output+=1
        #         j+=1
        # return output

        count = {0: 1}
        prefix_sum = 0
        output = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in count:
                output += count[prefix_sum - k]
            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return output