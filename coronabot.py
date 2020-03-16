import telebot
from telebot import types

bot = telebot.TeleBot('1059075556:AAFBaR_SSRUdrj1gizQ0RgLRB0n9IkE39aY')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Что такое корона вирус','Симптомы коронавируса COVID-19')
keyboard1.row('Распространение коронавируса','Записаться на обследование')
keyboard1.row('Проверочный тест на корона вирус')
x='6'
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, ' Вас приветсвует телеграм бот созданный для информирование людей о короновирусе COVID-19')
    bot.send_message(message.chat.id, "Выберите то что вас интересует из списка ниже", reply_markup=keyboard1)
#1
@bot.message_handler(func=lambda message: message.text == "Что такое корона вирус")
def first_question(message):
    bot.send_message(message.chat.id,'Коронавирус — это острое вирусное заболевание, характеризующееся преимущественным поражением дыхательной системы и желудочно-кишечного тракта. Коронавирус является зоонозной инфекцией по происхождению. ')
#2
@bot.message_handler(func=lambda message: message.text == "Симптомы коронавируса COVID-19")
def second_question(message):
    bot.send_message(message.chat.id,'Здесь симтомы будут')
#3
@bot.message_handler(func=lambda message: message.text == "Распространение коронавируса")
def third_question(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Посмотреть', url='https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Распространение коронавируса", reply_markup = markup)


#4
@bot.message_handler(func=lambda message: message.text == "Записаться на обследование")
def fifth_question(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Запись к доктору', url='https://egov.kz/cms/ru/services/health_care/495pass_mz')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Онлайн запись к доктору через egov", reply_markup = markup)

#5
@bot.message_handler(func=lambda message: message.text == "Проверочный тест на корона вирус")
def seventh_question(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Быстрый тест', url='http://u7018851.beget.tech/insan/index.html')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Тест", reply_markup = markup)
bot.polling()
