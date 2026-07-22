class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums={}
        for num in nums:
            if num in dict_nums:
                dict_nums[num]+=1
            else:
                dict_nums[num]=1
        
        sorted_keys = sorted(dict_nums, key=dict_nums.get, reverse=True)
        return sorted_keys[:k]
