from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxHeap = []
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if followee in self.tweets:
                idx = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush_max(maxHeap, [time, tweetId, followee, idx-1])
        while maxHeap and len(result) < 10:
            time, tweetId, followee, idx = heapq.heappop_max(maxHeap)
            result.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweets[followee][idx]
                heapq.heappush_max(maxHeap, [time, tweetId, followee, idx-1])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
