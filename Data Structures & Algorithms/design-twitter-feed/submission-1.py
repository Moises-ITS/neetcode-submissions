class Twitter:

    def __init__(self):
        self.count = 0
        self.postDb = defaultdict(list)
        self.followDb = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postDb[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followDb[userId].add(userId)
        for followeeId in self.followDb[userId]:
            if followeeId in self.postDb:
                index = len(self.postDb[followeeId]) - 1
                count, tweetId = self.postDb[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.postDb[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDb[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDb[followerId]:
            self.followDb[followerId].remove(followeeId)

