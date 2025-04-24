import datetime

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram import F, Router
from aiogram import html
from aiogram.fsm.context import FSMContext
from aiogram.utils.media_group import MediaGroupBuilder

from app.strings import *
from app.functions import *
import app.keyboards as kb
from app.payment import create_payment, check_payment, get_payment_list
import config
from app.database import add_user

router = Router()

async def funnel(message: Message):
    await add_user(message.from_user.id)
    await message.answer_photo(FSInputFile("media/matrix-me.png"), demo_lessons)

    await asyncio.sleep(config.THIRTY_SECONDS)
    await message.answer_photo(FSInputFile("media/life-is-running.png"), mentor_sales, reply_markup=kb.question)

    await asyncio.sleep(config.THREE_MINUTES)
    album_builder = MediaGroupBuilder(caption="🤕 Учусь в университете, работаю курьером и постоянно тревожусь за свое будущее.")
    album_builder.add_photo(media=FSInputFile("media/old_salary.png"))
    album_builder.add_photo(media=FSInputFile("media/old_me2.jpg"))
    album_builder.add_photo(media=FSInputFile("media/old_me3.jpg"))
    await message.answer_media_group(media=album_builder.build())
    await message.answer(my_story,
    reply_markup=kb.question)

    await asyncio.sleep(config.TWELVE_HOURS)
    await message.answer(await end(html.quote(message.from_user.first_name)))


@router.message(CommandStart(deep_link=True, magic=F.args == 'guide'))
async def cmd_start_guide(message: Message):
    await message.answer(await hello_guide(html.quote(message.from_user.first_name)),
    reply_markup=kb.guide)
    await asyncio.sleep(config.THREE_MINUTES)
    await message.answer_photo(FSInputFile("media/screen_questions.png"), gift,
    reply_markup=kb.questions)
    await asyncio.sleep(config.THREE_MINUTES)
    await funnel(message)


@router.message(CommandStart())
@router.message(CommandStart(deep_link=True, magic=F.args == 'article'))
async def cmd_start_article(message: Message):
    await message.answer(await hello_article(html.quote(message.from_user.first_name)),
    reply_markup=kb.article)
    await asyncio.sleep(config.THREE_MINUTES)
    await message.answer_photo(FSInputFile("media/screen_questions.png"), gift,
    reply_markup=kb.questions)
    await asyncio.sleep(config.THREE_MINUTES)
    await funnel(message)


@router.message(Command("buy"))
async def buy(message: Message, state: FSMContext):
    sale_url, sale_id = create_payment(config.CONS_PRICE, message.chat.id)
    await message.answer(sale,
                         reply_markup=await kb.sale_button(sale_url))

# 📩 Команда /post
@router.message(Command("post"))
async def cmd_post(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Только администраторы могут использовать эту команду.")
        return
    await state.set_state(PostForm.waiting_for_text)
    await message.answer("✏️ Введите текст поста:")


@router.message(PostForm.waiting_for_text)
async def get_post_text(message: Message, state: FSMContext):
    post_text = message.html_text
    photo = None

    if message.photo:
        photo = message.photo[-1].file_id  # Берём самую качественную версию
    await state.update_data(post_text=post_text, photo=photo)
    await state.set_state(PostForm.waiting_for_time)
    await message.answer("⏰ Введите время публикации в формате: 2025-04-13 15:30")


@router.message(PostForm.waiting_for_time)
async def schedule_post(message: Message, state: FSMContext):
    try:
        post_time = datetime.datetime.strptime(message.text, "%Y-%m-%d %H:%M")
        now = datetime.datetime.now()
        if post_time < now:
            await message.answer("⛔ Время в прошлом. Введите корректное будущее время.")
            return
    except ValueError:
        await message.answer("⛔ Неверный формат. Используйте: 2025-04-13 15:30")
        return

    data = await state.get_data()
    post_text = data['post_text']
    photo = data.get('photo')
    delay = (post_time - datetime.datetime.now()).total_seconds()
    await message.answer(f"✅ Пост запланирован на {post_time.strftime('%Y-%m-%d %H:%M')}")

    # Планируем рассылку
    asyncio.create_task(send_post_later(post_text, delay, photo))
    await state.clear()

@router.callback_query(F.data == 'FAQ')
async def FAQ(callback: CallbackQuery):
    await callback.answer('FAQ')
    await callback.message.answer(faq)

