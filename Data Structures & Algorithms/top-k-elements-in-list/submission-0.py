from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        result = []
        for x, freq in s.most_common(k):
            result.append(x)
        return result