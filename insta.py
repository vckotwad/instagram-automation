from instabot import Bot
import os

bot=Bot()
bot.login(username='',password="")
for i in range(20,36): #change the range accordingly
    try:
        bot.upload_photo(str(i)+".png",caption="#python #pythonprogramming #pythoncode #python_public")
    except:
        print("error")
    os.remove(str(i)+".png")
    
