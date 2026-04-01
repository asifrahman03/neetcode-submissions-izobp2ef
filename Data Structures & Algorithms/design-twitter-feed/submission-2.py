class Twitter:

    def __init__(self):
        self.followM = defaultdict(set)
        self.tweetM = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweetM[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # 1. First merge into big list
        final_tweets = self.tweetM[userId][:]

        # Getting following's tweets
        for following in self.followM[userId]:
            following_tweets = self.tweetM[following]
            final_tweets.extend(following_tweets)
        
        # 2. Heapify it and return the feed
        final_heap = [(-cnt, t_id) for cnt, t_id in final_tweets]

        heapq.heapify(final_heap)
        res = []
        c = 0
        while final_heap and c != 10:
            _, t_id = heapq.heappop(final_heap)
            res.append(t_id)
            c += 1
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followM[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.followM[followerId]:
            return
        self.followM[followerId].remove(followeeId)
