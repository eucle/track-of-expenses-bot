from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from create import dp
from keyboards.user_keyboard import group_choice, category_choice, payment_method_choice
from states.record import CreateRecord


@dp.message_handler(commands=['117279'])
async def show_groups(message: types.Message, state: FSMContext):
    await message.answer(text='Выбери группу, затем категорию расходов.\n'
                              'Если ничего не нужно, то жми отмену.',
                         reply_markup=group_choice)
    await state.set_state(CreateRecord.waiting_for_group.state)


@dp.callback_query_handler(text='automobile', state=CreateRecord.waiting_for_group)
async def choose_group(call: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_group=call.data)
    # callback_data = call.data
    # logging.info(f'call = {callback_data}')
    await call.message.edit_reply_markup(category_choice)
    await state.set_state(CreateRecord.waiting_for_category.state)
    await call.answer('Сохранено.')


@dp.callback_query_handler(text='fuel', state=CreateRecord.waiting_for_category)
async def choose_category(call: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_category=call.data)
    # callback_data = call.data
    # logging.info(f'call = {callback_data}')
    await state.set_state(CreateRecord.waiting_for_cost.state)
    await call.message.edit_text(text='Укажи сумму расходов:')
    await call.answer(f'Сохранено.')


@dp.message_handler(state=CreateRecord.waiting_for_cost)
async def choose_cost(message: types.Message, state: FSMContext):
    await message.answer(text='Укажи способ оплаты:',
                         reply_markup=payment_method_choice)
    await state.update_data(chosen_cost=message.text)
    await state.set_state(CreateRecord.waiting_for_payment_method.state)


@dp.callback_query_handler(text='cash', state=CreateRecord.waiting_for_payment_method)
async def choose_payment_method(call: CallbackQuery, state: FSMContext):
    await state.update_data(chosen_payment_method=call.data)
    # callback_data = call.data
    # logging.info(f'call = {callback_data}')
    user_data = await state.get_data()
    print(user_data)
    await call.answer(f'Сохранено.')
    await state.finish()
