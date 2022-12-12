from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateRecord(StatesGroup):
    waiting_for_group = State()
    waiting_for_category = State()
    waiting_for_cost = State()
    waiting_for_payment_method = State()
