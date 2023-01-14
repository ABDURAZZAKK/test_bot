import telebot
from telebot import types
from sqlA_orm import save_worker
from services import get_xlsx_name


TG_TOKEN = ''


bot = telebot.TeleBot(TG_TOKEN)
states = dict()



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    save_worker = types.KeyboardButton('Записать работника')
    markup.add(save_worker)
    states[message.chat.id] = 0
    bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup)



@bot.message_handler(func=lambda message:  message.text == "Записать работника")
def send_get_fio(message):
    states[message.chat.id] = 1
    bot.send_message(message.chat.id, "Введите ФИО работника")


@bot.message_handler(func=lambda message: states[message.chat.id] == 1 if message.chat.id in states else False)
def save_and_get_table(message):
    try:
        save_worker(message.text)
        file = open(get_xlsx_name(message.chat.id), 'rb')
        bot.send_document(message.chat.id, file)
    except Exception as e:
        print(e)
        

    states[message.chat.id] = 2

    bot.send_message(message.chat.id, "Вы в главном меню")



if __name__ == "__main__":
    bot.polling(non_stop=True, interval=0)