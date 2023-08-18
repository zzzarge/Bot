from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.models import Service, Appointment

def services_markup(services: list[Service]):
    markup = InlineKeyboardMarkup(row_width=2)

    for service in services:
        button = InlineKeyboardButton(text=service.name, callback_data=f"service_delete:/{service.id}")
        markup.add(button)

    return markup


def appointments_markup(appoinments: list[Appointment]):
    markup = InlineKeyboardMarkup(row_width=2)

    for appointment in appoinments:
        button = InlineKeyboardButton(text=f"{appointment.time} - {appointment.client}",callback_data=f"appointment:/{appointment.id}")
        markup.add(button)

    return(markup)




def del_photo_markup(photo_id):
    markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="Удалить", callback_data=f"last_work_delete:/{photo_id}")
    markup.add(button)

    return markup