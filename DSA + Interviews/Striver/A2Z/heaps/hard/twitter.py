import heapq
from collections import defaultdict

# Class representing the Twitter system
class Solution:
    def __init__(self):
        # tweets { userId : list((tweetId, timestamp)) }
        self.tweets = defaultdict(list)

        # followers { followerId : set(followeeId) }
        self.follows = defaultdict(set)

        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int):
        feed = [] # max_heap (-timestamp, tweetId, index)

        users = self.follows[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                heapq.heappush(feed, (-self.tweets[user][-1][0], self.tweets[user][-1][1], len(self.tweets[user]) - 1, user))

        most_recent = []
        while len(most_recent) < 10 and feed:
            neg_timestamp, tweetId, index, user = heapq.heappop(feed)

            most_recent.append(tweetId)

            new_index = index - 1
            if new_index >= 0:
                heapq.heappush(feed, (-self.tweets[user][new_index][0], self.tweets[user][new_index][1], new_index, user))

        return most_recent

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

# Driver code
twitter = Solution()
twitter.postTweet(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))  # [2]
twitter.follow(1, 2)
print(twitter.getNewsFeed(1))  # [6, 2]
twitter.unfollow(1, 2)
twitter.postTweet(1, 7)
print(twitter.getNewsFeed(1))  # [7, 2]