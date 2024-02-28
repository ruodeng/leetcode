import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)[:k]]
print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
