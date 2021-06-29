import praw
reddit = praw.Reddit(
    client_id="6E9DNKh0DVWa2g",
    client_secret="EqChbA7105ZW9f6B3gFghGC2bDKScg",
    password="Magha@702",
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
