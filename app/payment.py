from xml.etree.ElementTree import indent

import yookassa
from yookassa import Payment
import uuid
from config import ACCOUNT_ID, SECRET_KEY
import json

yookassa.Configuration.account_id = ACCOUNT_ID
yookassa.Configuration.secret_key = SECRET_KEY

def create_payment(amount, chat_id):
    id_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "payment_method": {
          "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/ilyaatarbot"
        },
        "capture": True,
        "description": "Билет на консультацию с Ильей"
    }, id_key)
    return payment.confirmation.confirmation_url, payment.id

def check_payment(id):
    payment = yookassa.Payment.find_one(id)
    if payment.status == 'succeeded':
        return payment.metadata
    else:
        return False

def get_payment_list():
    payment_list = Payment.list()
    if payment_list is None or not isinstance(payment_list, dict):
        return "Список платежей пуст"

    output = []
    i = 1
    succeeded = 0
    if "items" in payment_list:
        for item in payment_list["items"]:
            payment_id = item.get("id", "N/A")
            status = item.get("status", "N/A")
            if status == 'succeeded':
                succeeded += 1
            created_at = item.get("created_at", "N/A")
            output.append(f"{i}. ID: {payment_id}, Status: {status}, Created At: {created_at}")
            i += 1
    print("\n".join(output))
    return "\n".join(output), succeeded
