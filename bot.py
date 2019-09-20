import logging
from datetime import date

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PROXY = {
    'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

def greet_user(bot, update):

    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def answer_planet(bot, update):

    user_text = update.message.text.split()

    try:
        planet = user_text[1].lower().capitalize()
    except IndexError:
        update.message.reply_text("Вы не ввели название планеты после /planet")

    today = date.today().strftime('%Y/%m/%d')
    logging.info(f"User: {update.message.chat.username}, Message: {update.message.text}, Planet: {planet}")

    try:
        get_planet = getattr(planet, ephem)(today)
    except AttributeError:
        update.message.reply_text("Я не могу определить, в каком созвездии ваша планета, или вы ввели не название планеты.")

    const = ephem.constellation(get_planet)
    update.message.reply_text(f"Сегодня {planet} находится в созвездии {const[1]}.")

def word_count(bot, update):

    user_id = update.message.chat.id
    user_name = update.message.chat.username
    user_text = update.message.text.split()

    print(f"user input {user_id}-{user_name} :{user_text}")

    ammount_of_words = len(user_text) - 1
    postfix = ""
    if ammount_of_words == 1:
        postfix = "word"
    else:
        postfix = "words"

    return_text = f"{len(user_text) - 1} {postfix}"
    update.message.reply_text(return_text)
    print(f"bot: {return_text}")

def next_full_moon(bot, update):

    user_id = update.message.chat.id
    user_name = update.message.chat.username
    user_text = update.message.text.split()
    try:
        user_date = str(user_text[1])
        date_next = ephem.next_full_moon(user_date)
        reply_text = f"Next full moon date is {date_next}"
        print(reply_text)
        update.message.reply_text(reply_text)
    except IndexError:
        print(f"user entered '{user_text}' : IndexError")
        update.message.reply_text("Enter a date after '/next_full_moon'")       
    except ValueError:
        update.message.reply_text("Enter a date in 'year-month-day' format")  

    print(f"user input {user_id}@{user_name} :{user_text}")

def cities(bot, update):
    dict_cities = {
                'a': 'Абакан', 
                'б': 'Барнаул'
                }
    user_id = update.message.chat.id
    user_name = update.message.chat.username
    user_text = update.message.text.split()
    user_text.pop(0)


def talk_to_me(bot, update):

    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

API_KEY = None
with open("token.txt","r") as f:
    API_KEY = f.read().strip()

def main():

    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", answer_planet))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("cities", cities))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
