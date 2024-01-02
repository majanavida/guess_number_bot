from aiogram import Router
from aiogram.types import Message
from users_data.user import users


# Initializing the module level router 
router = Router()


# This handler will work when user sends unavailable answer 
async def process_other_answers(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer(
            'We\'re playing, '
            'send number from 1 to 100'
        )
    else:
        await message.answer('I don\'t understeand you =(')