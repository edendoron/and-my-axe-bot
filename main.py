import praw
import config

prefixes = ["have my", "you have my", "you can have my"]

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    password=config.password,
    user_agent=config.user_agent,
    username=config.username,
)

print("-----Starting bot------")
subreddits = reddit.subreddit("all")
for comment in subreddits.stream.comments(skip_existing=True):
    body = comment.body
    if len(body.split()) > 6:
        continue
    lower_cased_comment = body.lower()
    for prefix in prefixes:
        if lower_cased_comment.startswith(prefix):
            if comment.body.isupper():
                reply = comment.reply("AND MY AXE!")
            else:
                reply = comment.reply("And my axe!")
            print(f"Replied! link to comment: https://reddit.com{reply.permalink}")
