import telebot
from telebot import types
from config import token
import db


bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def on_start(message):
	a = types.InlineKeyboardMarkup()
	ru = types.InlineKeyboardButton(text = '🇷🇺',callback_data = 'ru')
	uzb = types.InlineKeyboardButton(text = '🇺🇿',callback_data = 'uz')
	a.add(ru, uzb)
	m = bot.send_message(message.chat.id,'Выберите язык\n\nTilni tanlang', reply_markup = a)

@bot.callback_query_handler(func = lambda call: True)
def select_lang(call):
	global lang
	if call.data == 'ru':
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		button_phone = types.KeyboardButton(text='отправить контакт', request_contact=True)
		keyboard.add(button_phone)
		bot.send_message(call.message.chat.id, 'Чтобы зарегистрироватся нажмите на кнопку "отправить контакт"', reply_markup=keyboard)
		lang = 'ru'

	elif call.data == 'uz':
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		button_phone = types.KeyboardButton(text='malumotni yuborish', request_contact=True)
		keyboard.add(button_phone)
		bot.send_message(call.message.chat.id, 'Royhatdan otish uchun "malumotni yuborish" tugmasini bosing', reply_markup=keyboard)
		lang = 'uzb'

@bot.message_handler(content_types=['contact'])
def contact(message):	
	id_ = None
	temp = True
	id_ = db.Select_user_id()
	for i in id_:
		for y in i:
			if message.chat.id == y:
				if lang == 'uzb':
					bot.send_message(message.chat.id,"Siz ruyhatda borsiz")
					keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
					yuridik = types.KeyboardButton('promokod olish')
					fizik = types.KeyboardButton('promokodni kiritish')
					keyboard.add(yuridik, fizik)
					bot.send_message(message.chat.id, 'tugmani tanlang', reply_markup=keyboard)
				else:
					bot.send_message(message.chat.id,"вы уже зарегестрированы")
					keyboard = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
					yuridik = types.KeyboardButton('получить реферальную ссылку')
					fizik = types.KeyboardButton('получить свой рейтинг')
					keyboard.add(yuridik, fizik)
					bot.send_message(message.chat.id, 'выбериту кнопку', reply_markup=keyboard)
				temp = False
				break
	if temp:	
		if message.contact is not None: 
			contact = message.contact
			db.Create_user_data(contact.user_id,contact.first_name,contact.phone_number)
			if lang == 'uzb':
				msg = bot.send_message(message.chat.id,"Вы успешно зарегестрированы")
				keyboard = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
				yuridik = types.KeyboardButton('получить реферальную ссылку')
				fizik = types.KeyboardButton('получить свой рейтинг')
				keyboard.add(yuridik, fizik)
				bot.send_message(message.chat.id, 'выбериту кнопку', reply_markup=keyboard)
			else:		
				msg = bot.send_message(message.chat.id,"Вы успешно зарегестрированы")
				keyboard = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
				yuridik = types.KeyboardButton('получить реферальную ссылку')
				fizik = types.KeyboardButton('получить свой рейтинг')
				keyboard.add(yuridik, fizik)
				bot.send_message(message.chat.id, 'выбериту кнопку', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def function(message):
	if message.text == 'получить реферальную ссылку':
		id = db.Select_id(message.chat.id)
		bot.send_message(message.chat.id,f"Чтобы участвовать в розыгрыше перейдите по ссылке и получайте ценные призы\nссылка - http://127.0.0.1:8000/personal_link/{id[0][0]}/")
		bot.send_message(message.chat.id,"скидывайте это вашим друзьям и следите за вашис рейтингом!")
	elif message.text == 'получить свой рейтинг':
		q = db.Select_q(message.chat.id)
		bot.send_message(message.chat.id,f"ваша имя: {message.from_user.first_name}; ваш прогресс: {q}")

if __name__ == "__main__":
	bot.polling(none_stop = True)