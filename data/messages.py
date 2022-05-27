MESSAGES = {
    'start': 'Hi there, <b>{}</b>! \n If you willing to know forecast - click the button bellow ',

    'get_weather': 'You can simple enter the city in to the text field'
             ' or use the "Send current location" button',

    'forecast_duration': 'Got it, and now choose the forecast option',
    'geocoding_failure': 'It is impossible to find you by geolocation, could you enter city name in to the text field',

    'weather_for_location_retrieval_failed': 'Could not get forecast for this location 😞,' +
                                             'you can look out the window. '
                                             '\n\n /help - a manual how to use bot.',

    'general_failure': 'I can not dance like that 😞.\n\n /help - a manual how to use bot.',

    'current_weather_message': 'City weather: {}\n '
                               'Temp: {}C°\n '
                               'Humidity: {}\n Wind: {}\n Sunset: {}',
    '5_days_weather_message': '\n'
                              '{} ---- {}C° ---- {} \n'
                              '{} ---- {}C° ---- {} \n'
                              '{} ---- {}C° ---- {} \n'
                              '{} ---- {}C° ---- {} \n'
                              '{} ---- {}C° ---- {} \n'
                              '\n'
                              'If you want to get more info click "Details"',

    'help': 'I help you to know what to wear:\n Step№1 - Click "Get Weather" '
            'Step№2 - Enter the city in to the text field or use the "Send current location" button \n '
            'Step№3 - Choose an option \n And use the information as you need! \n '
            'Just /start the bot using menu or text field',
}


def get_message(message_key: str):
    return MESSAGES[message_key]
