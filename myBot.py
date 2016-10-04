
#Reddit Spelling Checker Bot
# ~~ By Brian Jopling, 2015 ~~
# ---------------------------------------------------------------------------------
#Purpose: To ensure that the word "spelling" (or any other word of your desire)
#         would always be corrected when someone on Reddit spells it wrong.
# ---------------------------------------------------------------------------------
#Why was this created?
#I created this as a means of learning more about automation. This was the first
#automated tool I had built, and I learned a lot working with Python and the
#PRAW library.
# ---------------------------------------------------------------------------------

import praw
import time

r = praw.Reddit(user_agent = "I'm a bot whose duty is to make sure the word 'spelling' is spelled correctly! Evil-doers beware!") #Description of bot sent to Reddit
r.login("USERNAME", "PASSWORD") #Use the login info of your bot's Reddit account.

words_to_match = ["speeling", "speling"] #Frequent misspellings of "spelling".
cache = [] #Used to store most recent comments so we don't reply more than once.

def run():
    subreddit = r.get_subreddit("test") #What subreddit do you want this bot to work in? If all (/r/all), do "all". I chose "test" for this example (/r/test)
    comments = subreddit.get_comments(limit=30) #Gets the 30 (limit) most recent comments.
    for comment in comments: #For every comment of the 30 we found...
        comment_text = comment.body.lower() #Get the text of the comment.
        match = any(string in comment_text for string in words_to_match) #Check if the text contains one of the misspellings we're looking for.
        if comment.id not in cache and match: #If we haven't replied, and it's a match...
            comment.reply('Aye! You spelled "spelling" wrong!') #Makes a comment.
            cache.append(comment.id) #Adds the comment id (something unique to Reddit's API) to the cache, so we don't comment again.
            print "We found one! Comment made."

while True: #Check for comments every 10 seconds. :D
    run()
    time.sleep(10)
