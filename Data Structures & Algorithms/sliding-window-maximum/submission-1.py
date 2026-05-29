import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        result = []
        heap = [(num, idx) for idx, num in enumerate(nums[0:k-1])]
        heapq.heapify_max(heap)
        for end in range(k - 1, len(nums)):
            heapq.heappush_max(heap, (nums[end], end))
            win_max, pos = heapq.heappop_max(heap)
            while pos < start:
                win_max, pos = heapq.heappop_max(heap)
            heapq.heappush_max(heap, (win_max, pos))
            result.append(win_max)
            start += 1
        return result
            

