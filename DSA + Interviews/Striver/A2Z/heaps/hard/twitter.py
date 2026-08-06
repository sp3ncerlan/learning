import heapq
from collections import defaultdict

# Class representing the Twitter system
class Solution:
    def __init__(self):

    def postTweet(self, userId: int, tweetId: int) -> None:
        

    def getNewsFeed(self, userId: int):

    def follow(self, followerId: int, followeeId: int) -> None:

    def unfollow(self, followerId: int, followeeId: int) -> None:


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