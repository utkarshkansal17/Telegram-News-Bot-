import logging 
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher,CallbackContext
from telegram import Bot, Update,ReplyKeyboardMarkup
from utils import get_reply, fetch_news,topics_key_board

logging.basicConfig(    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "1160702580:AAEUEPoZ-PVbF4WYqXKtP9nLUQf-8wp7CJw"

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route(f"/{TOKEN}", methods=['GET','POST'])
def webhook():

    update = Update.de_json(request.get_json(), bot)
    dp.process_update(update)
    return "ok"




#/start
def start(update: Update, context: CallbackContext):
   
    author = update.message.from_user.first_name
    reply = "Hi! {}".format(author)
    context.bot.send_message(chat_id=update.message.chat_id, text=reply)

def _help(update: Update, context: CallbackContext):
    help_txt = "Hey! This is a help text."
    context.bot.send_message(chat_id=update.message.chat_id, text=help_txt)


def news(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text="Choose category",
                            reply_markup=ReplyKeyboardMarkup(keyboard=topics_key_board,one_time_keyboard=True))

def reply_text(update: Update, context: CallbackContext):
    intent, reply = get_reply(update.message.text, update.message.chat_id)
    if intent == "get_news":
        articles = fetch_news(reply)
        for article in articles:
            context.bot.send_message(chat_id=update.message.chat_id, text=article['link'])
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo_sticker(update: Update, context: CallbackContext):
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker=update.message.sticker.file_id)

def error(update: Update, context: CallbackContext):
    logger.error("Update '%s' caused error '%s'",update,update.error)

    
bot = Bot(TOKEN)
try:
    bot.set_webhook("https://news-bot-kansal.herokuapp.com/"+TOKEN)
except Exception as e:
    print(e)

dp = Dispatcher(bot, None)
dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",_help))
dp.add_handler(CommandHandler("news",news))
dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
dp.add_handler(MessageHandler(Filters.text, reply_text))
dp.add_error_handler(error)
if __name__ == "__main__":
    app.run(port=8443)
