from aiogram.dispatcher.filters.state import State, StatesGroup


class ForecastQuery(StatesGroup):
    # State for location
    waiting_for_location = State()

    # State for forecast duration
    waiting_for_duration = State()



