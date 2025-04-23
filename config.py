from dotenv import load_dotenv
import os

load_dotenv()

# Аутентификация
TOKEN=os.getenv('TOKEN')
SECRET_KEY=os.getenv('SECRET_KEY')
ADMIN_ID=os.getenv('ADMIN_ID')
ACCOUNT_ID=os.getenv('ACCOUNT_ID')

# БД
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')

# Цены
CONS_PRICE=os.getenv('CONS_PRICE')
STUDENTS_COUNT=os.getenv('STUDENTS_COUNT')

# Время
ONE_MINUTES=1 #60
FIVE_MINUTES=1 #300
THREE_MINUTES=1 #180
TEN_MINUTES=1 #600
TWELVE_HOURS=1 #43200
THIRTY_SECONDS=1 #30
