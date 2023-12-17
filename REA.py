# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ⫷✿⫸ Commands for BOT Users
 〇☞ /start - বোট শুরু করুন
 〇☞ /about - এই বট সম্পর্কে
 〇☞ /help - এই বট কমান্ড সাহায্য করুন
 〇☞ /ping - লাইভ বট চেক করতে
 〇☞ /uptime - বট স্ট্যাটাস দেখতে 
 
 ⫷✿⫸ Command For Admin BOT
 〇☞ /logs - বট লগ দেখতে
 〇☞ /setvar - ডিবট কমান্ড দিয়ে var সেট করতে
 〇☞ /delvar - ডিবট কমান্ড দিয়ে var মুছে ফেলতে
 〇☞ /getvar - ডিবট কমান্ডের সাথে একটি ভার্স দেখতে
 〇☞ /users - বট ব্যবহারকারী পরিসংখ্যান দেখতে
 〇☞ /batch - একাধিক ফাইলের লিঙ্ক তৈরি করতে
 〇☞ /speedtest - বট সার্ভারের গতি পরীক্ষা করতে
 〇☞ /broadcast - বট ব্যবহারকারীদের সম্প্রচার বার্তা পাঠাতে

👨‍💻 Develoved by </b><a href='https://t.me/Farooq_is_KING'><b>𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭</b></a>


"""

    close = [
        [InlineKeyboardButton("✘ শেষ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("✘ শেষ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("🌼 Order Bot", callback_data="order"),
            InlineKeyboardButton("✘ শেষ", callback_data="close")
        ],
    ]

    ORDER = """
<b>About this Bot:

@{} is a Telegram bot for saving posts or files that can be accessed via a special link.

 〇≫ Creator: @{}
 〇≫ Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>


 Want to make a bot like this chat @WD_Contact_Bot
 
👨‍💻 Develoved by </b><a href='https://t.me/Farooq_is_KING'>𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭</a>
"""
