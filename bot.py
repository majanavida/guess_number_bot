import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers, command_handlers


async def main() -> None:
    # Loading the bot config 
    config: Config = load_config()
    
    # Bot and dispatcher initialization 
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    
    # Registering routers in dispatcher 
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.include_router(command_handlers.router)
    
    # Skip the accumulated updates and start polling 
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())