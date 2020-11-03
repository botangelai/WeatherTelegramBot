import requests
import telebot
import json
from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton


token = '1358591912:AAGGVF-v-umkGTiyTj4QcoZzBnVSH-H6Zfo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
async def start(message):
    await m.reply_text(
        text=f"Hello,\n\nWelcome to my weather bot. Enter your city name\n\nJoin my channel for getting news about me 👉 @AI_bot_projects",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌  Support Group', url='https://t.me/AI_BOT_HELP'),
                    InlineKeyboardButton('🔖  Projects Channel', url='https://t.me/AI_bot_projects')
                ],
                [
                    InlineKeyboardButton('💡  Youtube Channel', url='https://www.youtube.com/channel/UCyn07B5o6N67FkAEGmW5VfQ'),
                    InlineKeyboardButton('👨  Master', url='https://t.me/pppppgame')
                ]
            ]
        )
    )    


@bot.message_handler(content_types=['text'])
def weather(message):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    city = message.text
    r = requests.post(url = api_url, params = {'q' : city, 'APPID' : '7dcdaee53699b80f434071b42c259178', 'units' : 'metric'})
    if r.status_code == 200:
        
        response = json.loads(r.content)
        temp = str(response['main']['temp'])
        max_temp = str(response['main']['temp_max'])
        min_temp = str(response['main']['temp_min'])
        wind_speed = str(response['wind']['speed'])
        pressure = str(response['main']['pressure'])
        humidity = str(response['main']['humidity'])

        msg = 'The current weather in ' + city + ' ' + temp + '°C' + '\n' + 'Maximum temperature: ' + max_temp + '°C' + '\n' + 'Minimum temperature: ' + min_temp + '°C' + '\n' + 'Wind speed: ' + wind_speed + '\n' + 'Pressure: ' + pressure + '\n' + 'Humidity: ' + humidity

        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, 'Sorry, I was not able to get a temperature. Please check your name of the city!')

bot.polling(none_stop=True)
