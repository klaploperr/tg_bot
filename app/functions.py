import config
from aiogram.fsm.state import State, StatesGroup
from app.database import get_all_users
import asyncio
from bot_instance import *

# 📥 Форма для постинга
class PostForm(StatesGroup):
    waiting_for_text = State()
    waiting_for_time = State()

def is_admin(user_id: int) -> bool:
    return user_id in config.ADMIN_ID

# 📤 Отправка поста
async def send_post_later(text: str, delay: float, photo: str = None):
    await asyncio.sleep(delay)
    for user_id in await get_all_users():
        try:
            if photo:
                await bot.send_photo(user_id, photo, caption=text, parse_mode="HTML")
            else:
                await bot.send_message(user_id, text, parse_mode="HTML")
        except Exception as e:
            print(f"Ошибка при отправке пользователю {user_id}: {e}")