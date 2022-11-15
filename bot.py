import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


#PRICE =types.LabeledPrice(label="Подписка навсегда", amount=5 * 100)

#1 month
#@dp.message_handler(commands=['buy'])
#async def buy(message: types.Message):
#    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
#        await bot.send_message(message.chat.id, "Тестовый платёж")

#    await bot.send_invoice(message.chat.id,
#                            title="Подписка навсегда! 5 USD / 300 RUB",
#                            description="Подписка навсегда на все услуги",
#                            provider_token=config.PAYMENTS_TOKEN,
#                            currency="usd",
#                            photo_url="https://i.ibb.co/smGBTbR/8321cf6c06273596ed140bbd1673b2d8.jpg",
#                            photo_width=416,
#                            photo_height=234,
#                            photo_size=416,
#                            is_flexible=False,
#                            prices=[PRICE],
#                            start_parameter="one-month_subscription",
#                            payload="test-invoice-payloader")

#@dp.pre_checkout_query_handler()
#async def pre_cheackout_query(pre_cheackout_q: types.PreCheckoutQuery):
#    await bot.answer_pre_checkout_query(pre_cheackout_q.id, ok=True)

#suc pay
#@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
#async def succesful_payment(message: types.Message):
#    print("Succesfly:")
#    payment_info = message.successful_payment.to_python()
#    for k, v in payment_info.items():
#        print(f"{k} = {v}")

#    await bot.send_message(message.chat.id,
#                        f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошёл успешно!")





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

    #await bot.send_message(message.chat.id, "Привет! Это оффициальный бот канала @dogehacksso2\n ↓ Список всех команд указан ниже ↓ \n /desc - описание \n /buy - купить услуги \n /tg - ссылка на оффициальный канал \n /web - Можно купить если бот не работает")
    await bot.send_message(message.chat.id, "Привет, {0.first_name}! Это бот созданный нн типом -> @txtxtadh \n Тут можно чо то сделать \n Список команд \n /about \n /relisum \n /channel".format(message.from_user))


#Categories
#@dp.message_handler(commands=['list'])
#async def list(message):
#   markup_test = types.InlineKeyboardMarkup()
#    btncs = types.InlineKeyboardButton("🥶Приобрести DogeCheat CSGO на 30 дней!🥶", url='https://oplata.qiwi.com/form?invoiceUid=6d4ab8be-609b-4a39-aee4-4d6803f20598')
#   btnst = types.InlineKeyboardButton("🔥ПРиобрести DogeCheat Standoff 2 на 30 дней!🔥", url='https://oplata.qiwi.com/form?invoiceUid=6d4ab8be-609b-4a39-aee4-4d6803f20598')
#    markup_test.add(btncs)
#    markup_test.add(btnst)
#    await bot.send_message(message.chat.id, "Привет, {0.first_name}! Выбери товар и оплати его)".format(message.from_user), reply_markup=markup_test)

#relisium
@dp.message_handler(commands=['relisium'])
async def start(message: types.Message):

    #await bot.send_message(message.chat.id, "Привет! Это оффициальный бот канала @dogehacksso2\n ↓ Список всех команд указан ниже ↓ \n /desc - описание \n /buy - купить услуги \n /tg - ссылка на оффициальный канал \n /web - Можно купить если бот не работает")
    await bot.send_message(message.chat.id, "скоро".format(message.from_user))
    #await bot.send_message(message.chat.id, "Если вам нужны другие товары, введите команду \n /buy")
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
    #await bot.send_message(message.chat.id, "{0.first_name}! После оплаты напишите @txtxtadh чтобы мы могли зарегистрировать вас".format(message.from_user))





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





