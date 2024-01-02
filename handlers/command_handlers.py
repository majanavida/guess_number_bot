from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from users_data.user import users


# Initializing the module level router 
router = Router()


# This handler will work on command /start and add user in users list 
@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0,
            'lesions': 0,
        }
    await message.answer(('Hello!\n'
                          'To find out the rules of the game and '
                          'available commands - send a command /help'))
                
    
# This handler will work on command /help and send available commands and rules 
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(('Rules:\n'
                          'I wish for a number from 1 to 100, '
                          'you have 5 attempts\n'
                          'Available commands:\n'
                          '/help - rules and command list\n'
                          '/cancel - stop playing\n'
                          '/stats - check your game statistics\n'
                          'Let\'s play?'))
    
    
# This handler will work on command /stats and send user statistics 
@router.message(Command(commands=['stats']))
async def process_stats_command(message: Message):
    await message.answer(
        f'Total games: {users[message.from_user.id]['total_games']}\n'
        f'Wins: {users[message.from_user.id]['wins']}\n'
        f'Lesions: {users[message.from_user.id]['lesions']}'
    )
    
    
# This handler will work on command /cancel and end the game 
@router.message(Command(commands=['cancel']))
async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        await message.answer(
            'You are out of the game. If you want to play '
            'again - write about it'
        )
    else:
        await message.answer('We\'re not playing yet!')