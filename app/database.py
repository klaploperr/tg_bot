import asyncpg
from typing import Tuple
from config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

# 🔌 Подключение к БД
async def connect_db():
    return await asyncpg.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT
    )

# 📥 Добавление пользователя
async def add_user(user_id: int):
    conn = await connect_db()
    try:
        await conn.execute(
            "INSERT INTO users(user_id) VALUES($1) ON CONFLICT (user_id) DO NOTHING",
            str(user_id)
        )
    finally:
        await conn.close()

# 📤 Получение всех пользователей
async def get_all_users() -> Tuple[int]:
    conn = await connect_db()
    try:
        rows = await conn.fetch("SELECT user_id FROM users")
        return tuple(int(row['user_id']) for row in rows)
    finally:
        await conn.close()