
import requests
import telebot
from telebot import types
import random
filename = "clovar.txt"
bot = telebot.TeleBot('')

s_city = "Moscow,ru"
appid = ""

@bot.message_handler(commands=["look"])
def start(m, res=False):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather?",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
    except Exception as e:
        pass
    print("temp:", data['main']['temp'])
    print("conditions:", data['weather'][0]['description'])
    bot.send_message(m.chat.id, "Температура в Москве")
    bot.send_message(m.chat.id,data['main']['temp'])

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(m, res=False):
    with open(filename, 'r',encoding="utf8") as filehandle:
        current_line = 1
        line_number = random.randint(1, 28)
        for line in filehandle:
            if current_line == line_number:
                break
            current_line += 1
    bot.send_message(m.chat.id, line)
    filehandle.close()
# Запускаем бота
bot.polling(none_stop=True, interval=0)
