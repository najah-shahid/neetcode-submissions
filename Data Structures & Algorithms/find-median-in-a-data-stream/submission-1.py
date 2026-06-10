import heapq
class MedianFinder:

    def __init__(self):
        self.right = [] # min heap
        self.left = [] # max heap
    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush_max(self.left, num)
            return
        max_of_left = self.left[0]
        if num < max_of_left:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) > len(self.right) + 1:
            max_left = heapq.heappop_max(self.left)
            heapq.heappush(self.right, max_left)
        elif len(self.right) > len(self.left) + 1:
            min_right = heapq.heappop(self.right)
            heapq.heappush_max(self.left, min_right)
        
    def findMedian(self) -> float:
        nLeft = len(self.left)
        nRight = len(self.right)
        if nLeft > nRight:
            return self.left[0]
        elif nRight > nLeft:
            return self.right[0]
        else:
            return (self.left[0] + self.right[0])/2
        
        
        