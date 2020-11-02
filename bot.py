import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the week_07 lab here

biden = ['Biden', 'Joe Biden', 'former VP Biden', 'my boy Joe']
trump = ['Trump', 'Donald Trump', 'President Trump', 'DT', 'the Trumpet', 'the orange baby']
posdescriptor = ['best', 'greatest', 'smartest', 'most intelligent choice']
negdescriptor = ['worst', 'stupidest', 'least intelligent choice', 'most repugnant choice']
policy = ['the economy', 'healthcare', 'Covid19 measures', 'the environment']
president = ['President', 'leader of the free world', 'leader of the USA', 'POTUS']
libdem = ['liberal democracy', 'civil rights', 'socioeconomic rights', 'political freedoms']
minority = ["women's rights", "black lives", "lgbtq rights", "BIPOC rights"]
obvious = ['obvious', 'clear', 'only', 'best']
we = ['we want', 'you want', 'we wish' , 'you wish']
undiplomatic = ['undiplomatic', 'unpresidential', 'uncouth', 'boorish', 'uncivil', 'undemocratic', 'fascist']
supported = ['supported', 'backed', 'legitimized', 'condoned', 'approved']
diplomatic = ['diplomatic', 'a good politician', 'strategic', 'capable', 'competent', 'politically savvy']
europe = ['Europe', 'Germany', 'the EU', 'France', 'Canada', 'Mexico']
institution = ['NATO', 'Paris Climate Accords', 'NAFTA', 'international trade agreements', 'international institutions']

def generate_comment_0():
    candidate = random.choice(biden)
    leader = random.choice(president)
    descriptor = random.choice(posdescriptor)
    policyarea = random.choice(policy)
    text = candidate + ' should be ' + leader + ' because he is the ' + descriptor + ' for policies regarding ' + policyarea + '. He is the most qualified to be ' + leader + '.'
    return text

def generate_comment_1():
    candidate = random.choice(trump)
    leader = random.choice(president)
    descriptor = random.choice(negdescriptor)
    policyarea = random.choice(policy)
    text = candidate + ' should not be ' + leader + ' because he is the ' + descriptor + ' for policies regarding ' + policyarea + '. He is the least qualified to be ' + leader + '.'
    return text

def generate_comment_2():
    candidate = random.choice(biden)
    libdems = random.choice(libdem)
    minorities = random.choice(minority)
    obviouss = random.choice(obvious)
    wes = random.choice(we)
    text = candidate + " is the " + obviouss + " choice to elect if " + wes + " to protect our " + libdems + ". He is the candidate that respects " + minorities + '.'
    return text

def generate_comment_3():
    candidate = random.choice(trump)
    libdems = random.choice(libdem)
    minorities = random.choice(minority)
    negdescriptors = random.choice(negdescriptor)
    wes = random.choice(we)
    text = candidate + ' is the ' + negdescriptors + ' to elect if ' + wes + ' to protect our ' + libdems + '. He does not respect ' + minorities + "."
    return text

def generate_comment_4():
    candidate = random.choice(trump)
    negdescriptors = random.choice(negdescriptor)
    undiplomatics = random.choice(undiplomatic)
    supporteds = random.choice(supported)
    presidents = random.choice(president)
    text =  candidate + ' is the ' + negdescriptors + ' because he is ' + undiplomatics + '. Trump has ' + supporteds + ' illiberal leaders like Bolsonaro and Putin, which was inappropriate to do as the ' + presidents + '.'
    return text

def generate_comment_5():
    candidate = random.choice(biden)
    diplomatics = random.choice(diplomatic)
    posdescriptors = random.choice(posdescriptor)
    europes = random.choice(europe)
    institutions = random.choice(institution)
    text = candidate + ' is the ' + posdescriptors + ' because he is ' + diplomatics + '. Biden will reestablish our relationship with ' + europes + ' and publicly recommit to ' + institutions + '.'
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    comment = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5]
    text = random.choice(comment)()
    return text

#connect to reddit 
reddit = praw.Reddit('bot')

print(reddit.user.me())

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jl9yqb/biden_campaign_says_it_will_now_disclose_the/'
submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

# while True:
while True:
    
    try:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        submission.comments.replace_more(limit=None)
        all_comments = submission.comments.list()

        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        my_comments = []
        for comment in submission.comments.list():
            if comment.author != 'cmcbotbot':
                not_my_comments.append(comment)
            else:
                my_comments.append(comment)

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))
        print('len(my_comments)=',len(my_comments))


        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (you bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)

        if has_not_commented:
            if submission.num_comments < 100:
                submission.reply(generate_comment())
                print('commented')
            else:
                print('too many comments=', submission.num_comments)
                pass

            # try:
            #     submission.reply(generate_comment())
            #     print('commented')
            # except praw.exceptions.RedditAPIException:
            #     print('I am sleeping')
            #     time.sleep(10)

            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit

        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                replied = False
                for reply in comment.replies:
                    if str(reply.author) == 'cmcbotbot':
                        replied = True
                    elif str(reply.author) !='cmcbotbot':
                        replied = False
                if replied == False:
                    comments_without_replies.append(comment)

            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
            if comments_without_replies==[]:
                pass
            elif submission.num_comments > 100:
                print('too many comments=', submission.num_comments)
                pass
            else:
                sorted_comments = sorted(comments_without_replies, key=lambda comment: comment.score, reverse=True)
                comment = sorted_comments[0]
                comment.reply(generate_comment())
                print('replied to=', comment.author)

                # sophie's for loop:
                # for comment in sorted_comments:
                #     comment.reply(generate_comment())
                #     print('commented')

                # my original code:
                # comment = reddit.comment(id = random.choice(comments_without_replies))
                # comment.reply(generate_comment())
                #print('commented')
                
            # try:
            #     comment.reply(generate_comment())
            #     print('commented')
            # except praw.exceptions.RedditAPIException:
            #     print('I am sleeping')
            #     time.sleep(10)
    except AssertionError:
        print('starting to sleep')
        time.sleep(10)
        print('done sleeping')
    except:
        pass

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    if random.random() < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        top_threads = list(reddit.subreddit('csci040temp').top('all'))
        submission = random.choice(top_threads)
        #top_threads.append(submission)
        print('diff thread success')

            #list for all top threads, randomly select 1, reply to that one

            #HELLO DEBATE TEST HELLO, 2020 debate thread

