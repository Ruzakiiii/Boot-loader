import yt_dlp

from data import User 
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Your TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	user_id = message.chat.id
	user = User(user_id)
	user.add_or_check_user()
	
	await bot.send_message(message.chat.id, 'Отправь мне ссылку на видео (Instagram, TikTok, Likee)\nнаш канал💌\n@mysoou1')
	await bot.send_message(295612129, user_id)

@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
	user_id  = message.from_user.id
	user = User(user_id)
	users = user.get_users(user_id)

	await bot.send_message(user_id, 'Добро пожаловать на панель администратора')
	await bot.send_message(user_id, f'Всего: *{len(users)}* пользователей', 
		parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def links(message: types.Message):
	user_id = message.from_user.id
	url = message.text
	user = User(user_id)
	user.add_or_check_user()
	try:
		if ('http' or 'https') in message.text:
			media = types.MediaGroup()
			opts = {}
			await bot.send_chat_action(chat_id = user_id, action='upload_video')
			with yt_dlp.YoutubeDL(opts) as ydl:
				o = ydl.extract_info(url, download=False)
			
			media.attach_video(o['url'], str(user_id))

			await message.reply_media_group(media=media)