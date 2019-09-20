import logging
from datetime import date
import random

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
                'а': ['Абакан', 'Азов', 'Альметьевск', 'Ангарск', 'Арзамас', 'Армавир', 'Архангельск', 'Астрахань', 'Ачинск'], 
                'б': ['Барнаул', 'Белгород', 'Бийск', 'Благовещенск', 'Братск', 'Брянск'],
                'в': ['Великие Луки', 'Великий Новгород', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волжский', 'Вологда', 'Воркута', 'Воронеж'],
                'г': ['Грозный'],
                'д': ['Дзержинск'],
                'е': ['Екатеринбург', 'Елец', 'Есентуки'],
                'и': ['Иваново', 'Ижевск', 'Иркутск'],
                'й': ['Йошкар-Ола'],
                'к': ['Казань', 'Калининград', 'Калуга', 'Камышин', 'Кемерово', 'Киров', 'Кисловодск', 'Ковров', 'Коломна', 'Комсомольск-на-Амуре', 'Кострома', 'Красногорск', 'Краснодар', 'Красноярск', 'Курган', 'Курск', 'Кызыл'],
                'л': ['Липецк'],
                'м': ['Магадан', 'Магнитогорск', 'Майкоп', 'Междуреченск', 'Миасс', 'Москва', 'Мурманск', 'Муром', 'Мытищи'],
                'н': ['Набережные Челны', 'Назрань', 'Нальчик', 'Находка', 'Нефтекамск', 'Нефтеюганск', 'Нижневартовск', 'Нижнекамск', 'Нижний Новгород', 'Нижний Тагил', 'Новокузнецк', 'Новокуйбышевск', 'Новороссийск', 'Новосибирск', 'Новоуральск', 'Новочеркасск', 'Новый Уренгой', 'Норильск', 'Ноябрьск'],
                'о': ['Обнинск', 'Одинцово', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево'],
                'п': ['Пенза', 'Пермь', 'Петрозаводск', 'Петропавловск-Камчатский', 'Псков', 'Пятигорск'],
                'р': ['Ростов-на-Дону', 'Рыбинск', 'Рязань'],
                'с': ['Самара', 'Санкт-Петербург', 'Саранск', 'Саратов', 'Сергиев Посад', 'Серпухов', 'Смоленск', 'Соликамск', 'Сочи', 'Ставрополь', 'Старый Оскол', 'Стерлитамак', 'Сызрань', 'Сыктывкар'],
                'т': ['Таганрог', 'Тамбов', 'Тверь', 'Тобольск', 'Тольятти', 'Томск', 'Туапсе', 'Тюмень'],
                'у': ['Улан-Удэ', 'Ульяновск', 'Уссурийск', 'Уфа', 'Ухта'],
                'х': ['Хабаровск', 'Химки'],
                'ч': ['Чебоксары', 'Челябинск', 'Череповец', 'Чита'],
                'э': ['Элиста', 'Энгельс'],
                'ю': ['Южно-Сахалинск'],
                'я': ['Якутск', 'Ярославль']
                }
                
    # user_id = update.message.chat.id
    # user_name = update.message.chat.username
    user_text = str(update.message.text)
    user_text = user_text.replace('/cities ', '').lower()
    print(user_text)
    if user_text is not "":
        position_last_letter = len(user_text) - 1
        last_letter = user_text[position_last_letter]
        if last_letter in dict_cities.keys():
            reply_city = random.choice(dict_cities[last_letter])
            update.message.reply_text(f"{reply_city}")
            print(reply_city)
        else:
            update.message.reply_text(f"I don't know any city, that starts with '{last_letter}'")
            print(f"I don't know any city, that starts with '{last_letter}'")
            position_last_letter -= 1
            while position_last_letter > -1:
                last_letter = user_text[position_last_letter]
                if last_letter in dict_cities.keys():
                    reply_city = random.choice(dict_cities[last_letter])
                    update.message.reply_text(f"{reply_city}")
                    print(reply_city)
                    break
    else:
        update.message.reply_text("Enter a city after '/cities' command")
        print("Enter a city after '/cities' command")

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
