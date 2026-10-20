class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cons = nums[0]
        max_cons = nums[0]
        for i in range(1, len(nums)):
            cons = max(nums[i], cons+nums[i])
            max_cons = max(max_cons, cons)
        return max_cons