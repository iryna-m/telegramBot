# WeatherTelegramBot (pet project)
Forecast Weather TG Bot that allows you to get weather info for current day and for 5 days as well.
Bot can be found by https://t.me/ss_weather_bot

## Service Info
- Programing language - python
- Used library - aiogram
- Designed long polling bot - there is no need to use external IP, can be run on any machine that is using api.telegram.org.

## Workflow
- User send the current geo location or enter neede place to the text field and send it to the bot
- Using this parameters client send the request to https://openweathermap.org/ and from the response the bot forms message with asking weather info and send it to a user as a text message

## How to run
It is better to run on UNIX-like system (Linux or Mac OS)
Add to enviromental variables 
- API token for Telegram (To get it go to @BotFather and run the /newbot command)
- API token for OpenWeatherMap 

To run the bot please use Python 3,7 or higer

Set dependencies

`pip install -r requirements.txt`

Run the bot

`python3 app.py`
