from aiogram import Router, F
from aiogram.types import Message
from users_data.user import users, ATTEMPTS, get_random_number


# Initializing the module level router 
router = Router()
        
        
# This handler will work when user agress to play 
@router.message(F.text.lower().in_(['yes', 'go', 'lets', 'let\'s',
                                    'play', 'game', 'want to play']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = ATTEMPTS
        await message.answer(
            f'Hooray, {message.from_user.username}!\n'
            f'I guessed a number from 1 to 100, try to guess!'
        )
    else:
        await message.answer(
            'While we playnig i can respond only '
            'to numbers from 1 to 100 and commands'
        )
        
        
# This handler will work when user doesn't agree to play 
@router.message(F.text.lower().in_(['no', 'nope', 'dont', 'don\'t',
                                    'not now', 'wont', 'won\'t']))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer(
            'It\'s a pity :(\n'
            'If you want to play, just write'
        )
    else:
        await message.answer(
            'We\'re already playing, '
            'send number from 1 to 100'
        )
        
        
# This handler will work when user tries to guess the number 
@router.message((lambda x: x.text and x.text.isdigit() and
                 1 <= int(x.text) <= 100))
async def process_numbers_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id] \
                                     ['secret_number']:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            await message.answer(
                f'Congratulations, {message.from_user.username}!\n'
                f'You won, shall we play again?'
            )
        elif int(message.text) > users[message.from_user.id] \
                                      ['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('My number is lower!')
        elif int(message.text) < users[message.from_user.id] \
                                      ['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('My number is higher!')
        if users[message.from_user.id]['attempts'] == 0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['lesions'] += 1
            users[message.from_user.id]['total_games'] += 1
            await message.answer(
                f'Unfortunately your attempts are over...\n'
                f'My number was {users[message.from_user.id]["secret_number"]}\n'
                f'Shall we play again?'
            )
    else:
        await message.answer('We\'re not playing yet. You want to play?')