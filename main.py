import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Получаем токен из файла .env
TOKEN = os.environ.get('5868951568:AAGBvUtwIb0d7hUtzRcDmEwBw1ScaZY-9-A')


# Создаем обработчик команд
def start(update, context):
  update.message.reply_text('Hello!')


# Создаем обработчик сообщений
def echo(update, context):
  update.message.reply_text(update.message.text)


# Создаем функцию main
def main():
  # Создаем экземпляр Updater и передаем ему токен
  updater = Updater(TOKEN, use_context=True)

  # Получаем диспетчер для регистрации обработчиков
  dp = updater.dispatcher

  # Регистрируем обработчик команд
  dp.add_handler(CommandHandler('start', start))

  # Регистрируем обработчик сообщений
  dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

  # Запускаем бота
  updater.start_polling()

  # Ждем завершения работы бота
  updater.idle()


# Вызываем функцию main
if __name__ == '__main__':
  main()
