import asyncio
import logging

from app.handlers import router
from bot_instance import *

async def main():
    dp.include_router(router) # роутер, который занимается обработкой хендлеров в handlers
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

