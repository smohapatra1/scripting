#   https://www.geeksforgeeks.org/python/scraping-reddit-using-python/

import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id = "",
                               client_secret = "",
                               user_agent="")
subreddit = reddit_read_only.subreddit("redditdev")
print ("Display name:", subreddit.display_name)
print ("Title:", subreddit.title)
print ("Description:", subreddit.description)