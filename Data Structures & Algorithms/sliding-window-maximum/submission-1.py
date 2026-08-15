class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [0] * len(nums)
        front = 0
        back = 0

        result = []

        for r in range(len(nums)):

            # Remove expired index
            if front < back and q[front] <= r - k:
                front += 1

            # Remove smaller elements from back
            while front < back and nums[q[back - 1]] <= nums[r]:
                back -= 1

            q[back] = r
            back += 1

            # Window is ready
            if r >= k - 1:
                result.append(nums[q[front]])

        return result