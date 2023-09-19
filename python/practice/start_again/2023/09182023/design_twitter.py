#   https://leetcode.com/problems/design-twitter/
# 355. Design Twitter
# Medium
# 3.5K
# 441
# Companies
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

class User:
    def __init__(self,userId):
        self.userId=userId
        self.tweets= []
        self.followers=set()
        self.follows=set()

class Twitter:
    def __init__(self):
        self.users={}
        self.globalTime=0
    def CreateNewUser(self, userId):
        if userId not in self.userId:
            self.users[userId] = User(userId)
    def postTweet(self, userId:int, tweetId: int) -> None:
        self.CreateNewUser(userId)
        self.users[userId].tweets.append((self.globalTime, tweetId))
        self.globalTime +=1
    def getnewsFeed(self, userId):
        self.CreateNewUser(userId)
        aggregated_tweets=list(self.users[userId].tweets)
        for followee in self.user[userId].follows:
            aggregated_tweets.extend(followee.tweets)
        aggregated_tweets.sort(key=lambda x:x[0], reverse=True )

        feed=[tweet[1] for tweet in aggregated_tweets[:10]]
        return feed
    def follow( self, followerId: int, follweeId:int) -> None:
        #Create the users if new 
        self.CreateNewUser(followerId)
        self.CreateNewUser(followeeId)
        #Add the following edge 
        self.users[followerId].follows.add(self.users[followeeId])
        #Add the follower edge
        self.users[follweeId].follows.add(self.users[followerId])
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #Create the user if its new 
        self.CreateNewUser(followeeId)
        self.CreateNewUser(followerId)
        #unfollow if there is actually a follower
        if self.users[followerId] in self.users[followeeId].followers:
            #Remove the follower edge 
            self.users[followeeId].followers.remove(self.users[followerId])
            #remove the following edge 
            self.users[followerId].followers.remove(self.users[followerId])

              





 

