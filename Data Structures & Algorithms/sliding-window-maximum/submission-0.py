class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        result = []

        for r in range(len(nums)):
            if q and q[0] <= r - k:
                q.pop(0)
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)
            if r >= k - 1:
                result.append(nums[q[0]])

        return result