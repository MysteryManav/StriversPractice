# Design Twitter
from typing import List

class Twitter:

    def __init__(self):
        self.posts = [] # (user, tweetId)
        self.followers = {} # user: set()


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followers:
            self.followers[userId] = set()
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followers:
            self.followers[userId] = set()
            return []
        feed = []
        while True:
            N = len(self.posts)
            for i in range(N - 1, -1, -1):
                user, tweet = self.posts[i]
                if user == userId or user in self.followers[userId]:
                    feed.append(tweet)
                if len(feed) == 10:
                    break
            return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
