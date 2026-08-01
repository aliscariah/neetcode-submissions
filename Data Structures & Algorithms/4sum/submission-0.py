class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(i + 1, n):
                left = j + 1
                right = n - 1
                tar = target - nums[i] - nums[j]
                while left < right:
                    curr = nums[left] + nums[right]
                    if curr == tar:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
                        right-=1
                    elif curr>tar:
                        right-=1
                    else:
                        left+=1
        return [list(t) for t in result]

