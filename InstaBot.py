from instabot import Bot
bot = Bot()
bot.login(username="", password="")

# Upload a Picture
bot.upload_photo("xyz.jpg", caption="Demo Upload")

# Follow someone
bot.follow("elonrmuskk")

# Send a message
bot.send_message("Hello from MiKee", ['user1','user2'])

# Get followers info
my_followers = bot.get_user_followers("web3guy")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()