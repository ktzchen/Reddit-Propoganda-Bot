import praw
from textblob import TextBlob

reddit = praw.Reddit('bot')


for submission in list(reddit.subreddit('csci040temp').top(time_filter='all')):
    blob = TextBlob(str(submission.title))
    polarity = blob.sentiment.polarity
    submission.comments.replace_more(limit=None)
    #print('looped in subreddit')
    #print (polarity, submission.title.lower())
    if 'biden' in submission.title.lower():
        if polarity > 0:
            submission.upvote()
            print('upvoted submission')
        else:
            submission.downvote()
            print('downvoted submission')
    if 'trump' in submission.title.lower():
        if polarity < 0:
            submission.upvote()
            print('upvoted submission')
        else:
            submission.downvote()
            print('downvoted submission')
    all_comments = submission.comments.list()
    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        #print('looped in thread2')
        if 'biden' in comment.body.lower():
            if polarity > 0:
                comment.upvote()
                print('upvoted comment')
            else:
                comment.downvote()
                print('downvoted comment')
        if 'trump' in comment.body.lower():
            if polarity < 0:
                comment.upvote()
                print('upvoted comment')
            else:
                comment.downvote()
                print('downvoted comment')


# for submission in list(reddit.subreddit('csci040temp').top(time_filter='all')):
#     print('looped in subreddit')
#     if 'biden' in submission.title.lower():
#         submission.upvote()
#         print('upvoted submission') 
#     submission.comments.replace_more(limit=None)
#     all_comments = submission.comments.list()
#     for comment in submission.comments.list():
#         print('looped in thread')
#         if 'biden' in comment.body.lower():
#             comment.upvote()
#             print('upvoted comment')


#how does this run in tandem with bot.py