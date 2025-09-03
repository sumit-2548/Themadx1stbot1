# filename: madxpawan_redirect_bot.py
# Requirements:
# pip install pyTelegramBotAPI

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# ---------- CONFIG ----------
BOT_TOKEN = "8051381827:AAH7yUUEaSDwjfR3A1U-WfFWNFM2q7rBD08"

# Image URLs (replace with your own image links)
WELCOME_IMG_URL = "https://i.postimg.cc/3wrrhPS0/thumbnail.png"
OTT_IMG_URL     = "https://i.postimg.cc/W4qrGqV7/1756802830381.jpg"
STUDY_IMG_URL   = "https://i.postimg.cc/Gpg72yQJ/file-000000008c6c61fa87bf2d8dde530d4f.png"
ALL_IMG_URL     = "https://i.postimg.cc/QdWvvSJG/file-00000000c54061faa32129743023b7cb.png"

# Channel links
OTT_CHANNEL_LINK   = "https://t.me/ottcrackedbymadx"     # <- OTT Mods ka link yaha daalna
STUDY_CHANNEL_LINK = "https://t.me/madxstudymods"
ALL_CHANNEL_LINK   = "https://t.me/Madxallmodz"
# ----------------------------

bot = telebot.TeleBot(BOT_TOKEN)

# Helper: main menu inline keyboard
def main_menu_keyboard():
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton("🎬 OTT Mods", callback_data="ott"),
        InlineKeyboardButton("📚 Study Mods", callback_data="study"),
    )
    kb.row(
        InlineKeyboardButton("🛠️ All Mods", callback_data="all"),
        InlineKeyboardButton("🔁 Refresh", callback_data="refresh")
    )
    return kb

# Helper: build join keyboard for a given channel link
def join_keyboard(channel_link):
    kb = InlineKeyboardMarkup()
    kb.row(InlineKeyboardButton("👉 Join Channel", url=channel_link))
    kb.row(InlineKeyboardButton("🔙 Back to Menu", callback_data="back"))
    return kb

# /start handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    caption = (
        "<b>Welcome to MadXpawan Bot 🚀</b>\n\n"
        "Yaha se aap apni favorite category choose karke direct join kar sakte ho.\n\n"
        "🔹 <i>Choose your category below:</i>\n\n"
        "<i>⚡ System faad denge is baar! ⚡</i>"
    )
    try:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=WELCOME_IMG_URL,
            caption=caption,
            parse_mode="HTML",
            reply_markup=main_menu_keyboard()
        )
    except:
        bot.send_message(
            chat_id=message.chat.id,
            text=("Welcome to MadXpawan Bot 🚀\n\n"
                  "Choose your category below:"),
            reply_markup=main_menu_keyboard()
        )

# Callback query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == "ott":
            caption = (
                "🎬 <b>Welcome to the World of OTT Mods!</b>\n\n"
                "👉 Sabse latest aur updated OTT Mods yahi milenge.\n\n"
                f"🔥 <i>System faad denge — Binge mode ON!</i>"
            )
            edit_media_photo(call, OTT_IMG_URL, caption, join_keyboard(OTT_CHANNEL_LINK))

        elif call.data == "study":
            caption = (
                "📚 <b>Study Mods — Padho aur Rock Karo!</b>\n\n"
                "👉 Notes, PDFs, aur smart-study content.\n\n"
                f"🔥 <i>System faad denge — Knowledge Mode!</i>"
            )
            edit_media_photo(call, STUDY_IMG_URL, caption, join_keyboard(STUDY_CHANNEL_LINK))

        elif call.data == "all":
            caption = (
                "🛠️ <b>All Mods Universe</b>\n\n"
                "👉 Apps, Tools, Games — sab ek jagah.\n\n"
                f"🔥 <i>System faad denge — Full Power!</i>"
            )
            edit_media_photo(call, ALL_IMG_URL, caption, join_keyboard(ALL_CHANNEL_LINK))

        elif call.data == "refresh":
            caption = (
                "<b>Welcome to MadXpawan Bot 🚀</b>\n\n"
                "Yaha se aap apni favorite category choose karke direct join kar sakte ho.\n\n"
                "🔹 <i>Choose your category below:</i>\n\n"
                "<i>⚡ System faad denge is baar! ⚡</i>"
            )
            edit_media_photo(call, WELCOME_IMG_URL, caption, main_menu_keyboard())

        elif call.data == "back":
            caption = (
                "<b>Back to Menu — Choose kar lo!</b>\n\n"
                "Phir se category select karo.\n\n"
                "<i>⚡ System faad denge! ⚡</i>"
            )
            edit_media_photo(call, WELCOME_IMG_URL, caption, main_menu_keyboard())

        else:
            bot.answer_callback_query(call.id, "Unknown action.")
    except:
        bot.answer_callback_query(call.id, "Kuch error hua — try again.")

# Utility function
def edit_media_photo(call, photo_url, caption_text, reply_markup):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    media = InputMediaPhoto(media=photo_url, caption=caption_text, parse_mode="HTML")
    try:
        bot.edit_message_media(
            media=media,
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=reply_markup
        )
        bot.answer_callback_query(call.id)
    except:
        bot.send_photo(
            chat_id=chat_id,
            photo=photo_url,
            caption=caption_text,
            parse_mode="HTML",
            reply_markup=reply_markup
        )
        bot.answer_callback_query(call.id)

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(timeout=60, long_polling_timeout=60)