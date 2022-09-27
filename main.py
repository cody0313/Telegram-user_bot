from pyrogram import Client
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

api_id = 123 #Write your id here
api_hash = 123 #Write your hash here 

app = Client("my_account", api_id=api_id, api_hash=api_hash)
 
# type
#Type the following command to make it work: .type text
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒" #printing symbol
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.001) # 1 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.001)
 
        except FloodWait as e:
            sleep(e.x)
 

#heart
#Type the following command to make it work: .heart
@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def heart(_, msg):
    emoji = ("🤍🤍🤍🤍🤍🤍🤍🤍🤍 \n 🤍🤍❤️❤️🤍❤️❤️🤍🤍 \n 🤍❤️❤️❤️❤️❤️❤️❤️🤍 \n 🤍❤️❤️❤️❤️❤️❤️❤️🤍 \n 🤍❤️❤️❤️❤️❤️❤️❤️🤍 \n 🤍🤍❤️❤️❤️❤️❤️🤍🤍 \n 🤍🤍🤍❤️❤️❤️🤍🤍🤍 \n 🤍🤍🤍🤍❤️🤍🤍🤍🤍 \n 🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    while 1 == 1:
        emoji = (emoji.replace("❤️", "🧡"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("🧡", "💛"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("💛", "💚"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("💚", "💙"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("💙", "💜"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("💜", "🖤"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("🖤", "💖"))
        msg.edit(emoji)
        sleep (0.003)
        emoji = (emoji.replace("💖", "❤️"))
        msg.edit(emoji)
        sleep (0.003)


#spam
#Type the following command to make it work: .spam text number
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(_, msg,):
    orig_text = msg.text.split()[1]
    msg.edit(orig_text)
    num = msg.text.split()[2]
    for x in range(0, int(num)):
        msg.reply(orig_text)  
           
        
 
app.run()
