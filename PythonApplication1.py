import telegram
import requests

def get_data_from_api(api_key):
    url = 'https://api.example.com/data'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я телеграм-бот. Чтобы получить данные из API, введите /get_data.")

def get_data(update, context):
    api_key = 'YOUR_API_KEY'
    data = get_data_from_api(api_key)
    if data is not None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(data))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Не удалось получить данные из API.")

def main():
    bot_token = 'YOUR_BOT_TOKEN'
    updater = telegram.Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
    dispatcher.add_handler(telegram.ext.CommandHandler('get_data', get_data))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

