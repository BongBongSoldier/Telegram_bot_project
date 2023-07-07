import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
import time
from random import randint

TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN, parse_mode='HTML')

A_Lib = open("Lob_library/library_anomaly.txt")

@bot.message_handler(commands=['creator','info','contact'])


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    r_HM = randint(1, 5)
    if r_HM == 1:
        chat_id = message.from_user.id
        await bot.send_message(chat_id, 'Привет рад тебя видеть!')
        await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJlH5kpAtLLne4lUcR5XTm9yGyawyqVgACXQEAAqH2jQNApKbzPe6_5y8E')
    elif r_HM == 2:
        chat_id = message.from_user.id
        await bot.send_message(chat_id, 'Привет!')
        await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJlH5kpAtLLne4lUcR5XTm9yGyawyqVgACXQEAAqH2jQNApKbzPe6_5y8E')
    elif r_HM == 3:
        chat_id = message.from_user.id
        await bot.send_message(chat_id, 'Рад тебя видеть!')
        await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJlH5kpAtLLne4lUcR5XTm9yGyawyqVgACXQEAAqH2jQNApKbzPe6_5y8E')
    elif r_HM == 4:
        chat_id = message.from_user.idf
        await bot.send_message(chat_id, 'Жду команды.')
        await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJmcdkpWSmF_qIgJ22VgnAVOZuQMnsdwACbwEAAqH2jQO29xXn4UteOS8E')
    else:
        chat_id = message.chat.id
        await bot.send_message(chat_id, 'Ну зачем пришел?')
        await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJmclkpWSpp_NAQ3Ndmxn5hqvPemvBrQACYAEAAqH2jQMCH9gwqgqD2C8E')

@bot.message_handler(commands=['help', 'Help', 'HELP'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Тебе никто не поможет', disable_notification=True, protect_content=True)
    await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJmU1kpT9G1AAB6NuOVByuHillElvMtP0AAnYBAAKh9o0DmAk-ydEa6eovBA')

@bot.message_handler(commands=['location'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 58.006035175949485, 56.22731177316515)

@bot.message_handler(commands=['photo'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id, 'https://img.freepik.com/free-photo/lavender-field-at-sunset-near-valensole_268835-3910.jpg', caption='Тест')

@bot.message_handler(commands=['bomb'])
async def send_welcome(message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Лови!', disable_notification=True, protect_content=True)
    await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJmUZkpTxqPMteVFFH7j8-7dGheLsUKQACZgEAAqH2jQNaaaryWMMgGC8E')
    await asyncio.sleep(2)
    await bot.send_message(chat_id, '💣')
    await asyncio.sleep(0.5)
    await bot.send_message(chat_id, '💣')
    await bot.send_message(chat_id, '💣')

@bot.message_handler(commands=['search','поиск','find'])
async def send_welcome(message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Хорошо поиск а кого искать будем?')
    await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJnB5kppnKsnNAnMhhAAEhFAKUCd7wWCUAAnUBAAKh9o0DQ2FqxOU2tLwvBA')

@bot.message_handler(func=lambda message: True)
    text_message = message.text
    text_message = text_message.lower()
    if 'an' in text_message or 'al' in text_message:
        await bot.reply_to(message, A_Lib.readline())
    else :
        await bot.reply_to(message, 'Такого нет в нашей базе данных')
        await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJnjVkp94ljSiuv67T2_68aoCjJKdk2QACewEAAqH2jQMYgGa_0vcnAS8E')


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if '1' in text_message or '1' in text_message:
        await bot.reply_to(message, '1')
    elif '1' in text_message or '1' in text_message:
        await bot.reply_to(message, '2')
    else:
        await bot.reply_to(message, ' ')

A_Lib.close()


import asyncio
asyncio.run(bot.polling())
