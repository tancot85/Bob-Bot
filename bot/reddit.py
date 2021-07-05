import praw
import os
reddit = praw.Reddit(
    client_id=os.environ("Client_ID"),
    client_secret=os.environ("Client_Secret"),
    password=os.environ("pass"),
    user_agent="testscript by u/RagingBox08",
    username="RagingBox08",
)
def getNewPost(rslash):
    # rslash = input("enter the name of the subreddit: ")
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.new(limit=1):
        print(submission.url)
        return submission.url, subreddit.title

def getHotPost(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    c  = 0
    for submission in subreddit.hot(limit = 2):
        if c == 0:
            c +=1
            continue
        print(submission.url)
        return submission.url, subreddit.title

def getTopPost(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.top(limit= 1):
        print(submission.title)
        print(submission.url)
        return submission.url,subreddit.title
        

# getTopPost('cursedcomments')