import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)



#tg
@dp.message_handler(commands=['tg'])
async def tg(message: types.Message):
    await bot.send_message(message.chat.id, "Это я -> @txtxtadh")



#desc
@dp.message_handler(commands=['desc'])
async def desc(message: types.Message):
    await bot.send_message(message.chat.id, "чо")
    #await bot.send_message(message.chat.id, "Тут вы можете приобрести услуги от нашего канала")
    #await bot.send_message(message.chat.id, "Введя команду /buy")


#buy chanel
@dp.message_handler(commands=['channel'])
async def channel(message: types.Message):
    await bot.send_message(message.chat.id, "Мой паблик тут всё, @timur4ik_parkur4ik")


#start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    
    await bot.send_message(message.chat.id, "Привет, {0.first_name}! Это бот созданный нн типом -> @txtxtadh \n Тут можно чо то сделать \n Список команд \n /about \n /relisum \n /channel".format(message.from_user))



#relisium
@dp.message_handler(commands=['relisium'])
async def start(message: types.Message):

    
    await bot.send_message(message.chat.id, "скоро".format(message.from_user))

#btn
@dp.message_handler(commands=['about']) #создаем команду
async def btn(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("❤My Github❤", url='https://github.com/andrejparkur2007')
    button2 = types.InlineKeyboardButton("🧡My Web (new)🧡", url='https://www.groznij.tk')
    button3 = types.InlineKeyboardButton("💙Relisium (soon)💙", url='https://www.relisium.tk')
    button4 = types.InlineKeyboardButton("🤍Public (чо)🤍", url='https://t.me/timur4ik_parkur4ik')
    button5 = types.InlineKeyboardButton("👉Donate👈", url='https://www.supportgroznij.tk')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    await bot.send_message(message.chat.id, "Привет, {0.first_name}! eisfjhs".format(message.from_user), reply_markup=markup)






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





