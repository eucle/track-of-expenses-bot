from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

group_choice = InlineKeyboardMarkup(row_width=2)
category_choice = InlineKeyboardMarkup(row_width=2)
payment_method_choice = InlineKeyboardMarkup(row_width=2)

# Группы расходов
automobile = InlineKeyboardButton(text='Автомобиль', callback_data='automobile')
group_choice.insert(automobile)

entertainment = InlineKeyboardButton(text='Развлечения', callback_data='entertainment')
group_choice.insert(entertainment)

shops = InlineKeyboardButton(text='Магазины', callback_data='shops')
group_choice.insert(shops)

children = InlineKeyboardButton(text='Дети', callback_data='children')
group_choice.insert(children)

# Категории расходов
fuel = InlineKeyboardButton(text='Топливо', callback_data='fuel')
category_choice.insert(fuel)

service = InlineKeyboardButton(text='Обслуживание', callback_data='service')
category_choice.insert(service)

# Способы оплаты
cash = InlineKeyboardButton(text='Наличные', callback_data='cash')
payment_method_choice.insert(cash)

credit_card_vtb = InlineKeyboardButton(text='ВТБ кредитка', callback_data='credit_card_vtb')
payment_method_choice.insert(credit_card_vtb)
