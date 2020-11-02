# Reddit-Propoganda-Bot

#### Candidate
My bot, cmcbotbot, supports Biden and opposes Trump.

#### Favorite Thread
This is a link to my favorite [thread](https://www.reddit.com/r/csci040temp/comments/jlokq8/biden_campaign_says_it_will_now_disclose_the/?utm_source=share&utm_medium=web2x&context=3) involving my bot. I like this thread because it contains one of my favorite bot interactions. Both my bot (cmcbotbot) and cs40-test-bot are commenting on Biden's diplomacy skills and the importance on international relationships. 
![fave_thread](https://raw.githubusercontent.com/ktzchen/Reddit-Propoganda-Bot/main/fave_thread.png_

#### bot_counter.py Output
includes the output of running the bot_counter.py file on your bot to count how many comments you've created; the output of this command must be inside of a markdown code block (i.e. use the triple backticks notation)

```
(base) Katie-MacBook-Pro:hw03 Katie$ /usr/local/bin/python3 /Users/Katie/Desktop/cs/hw03/bot_counter.py
len(comments)= 1000
len(top_level_comments)= 53
len(replies)= 947
len(valid_top_level_comments)= 49
len(not_self_replies)= 947
len(valid_replies)= 750
========================================
valid_comments= 799
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
![botcounter output](https://raw.githubusercontent.com/ktzchen/Reddit-Propoganda-Bot/main/botcounter_output.png)

#### Assignment Score
Tasks completed and final score:
22/20
* +12: Each task is worth 2 points (6 tasks * 2 points/task = 12 points). Having completed all tasks, I have 12 points
* +2: This github repository is worth 2 points
* +2: My bot posted at least 100 comments
* +1: My bot upvotes any comment mentioning Biden
* +1: My bot upvotes any submission/thread mentioning Biden
* +1: My bot replies to highly upvoted comments before replying to lower upvoted comments
* +1: My bot has written more than 500 comments
* +2: My bot uses the textblob library to measure the sentiment of every comment/submission, and upvotes or downvotes according to the candidate mentioned in the comment/submission and the associated sentiment.

Uncompleted extra credit:
* My bot does not post new submissions to the subreddit
* I do not have an army of 10 upvoting bots 
* My bot does not respond based on the comment it is replying to
* My bot does not use the GPT-2 model
