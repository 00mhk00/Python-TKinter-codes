import instaloader

bot = instaloader.Instaloader()
username = '__pythonworld__'
print(bot.download_profile(username,profile_pic_only=True))