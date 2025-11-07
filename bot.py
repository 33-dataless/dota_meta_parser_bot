import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from handlers.registr import register_handlers
from util.get_data_env import get_tg_bot_api_env

logging.basicConfig(level=logging.INFO)

bot = Bot(token=get_tg_bot_api_env(), default=DefaultBotProperties(parse_mode="HTML"))

async def main():
    dp = Dispatcher()
    register_handlers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n EXIT")
    #aaaМОЕ ТП ОТМЕНЕНО ИГРА ПРОЕБАНА ДАВНО И ЭТО ВСЕ МОЯ ВИНАААА
