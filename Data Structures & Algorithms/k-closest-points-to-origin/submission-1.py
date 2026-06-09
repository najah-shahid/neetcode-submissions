import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDist(x,y):
            return math.sqrt(x*x + y*y)
        heap = []
        for x, y in points:
            dist = findDist(x,y)
            if len(heap) < k:
                heapq.heappush_max(heap, [dist, x, y])
            else:
                if dist < heap[0][0]:
                    heapq.heappop_max(heap)
                    heapq.heappush_max(heap, [dist, x, y])
        heap = list(heap)
        heap = [[x,y] for dist, x, y in heap]
        return heap
