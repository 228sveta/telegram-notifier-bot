import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, JOKES

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        '😂 *Бот-анекдотчик!*\n\n'
        'Используй команды:\n'
        '/start - показать это сообщение\n'
        '/joke - случайный анекдот\n'
        '/help - помощь\n\n'
        '_Приятного использования!_ 😊',
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    await update.message.reply_text(
        '🤖 *Помощь по боту*\n\n'
        'Это учебный бот для отправки случайных анекдотов.\n'
        'Команда /joke отправит случайный анекдот про программистов.\n\n'
        'Бот создан в рамках учебного задания.',
        parse_mode='Markdown'
    )

async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /joke - ОТПРАВКА СЛУЧАЙНОГО АНЕКДОТА"""
    try:
      
        joke = random.choice(JOKES)
        
        await update.message.reply_text(
            f"🎭 *Случайный анекдот:*\n\n{joke}\n\n_Приятного дня!_ 😊",
            parse_mode='Markdown'
        )
        logger.info(f"Анекдот отправлен пользователю {update.effective_user.id}")
        
    except Exception as e:
        error_msg = f'❌ Ошибка при отправке анекдота: {str(e)}'
        await update.message.reply_text(error_msg)
        logger.error(error_msg)

def main():
    """Основная функция запуска бота"""
    try:
        # Создаем приложение
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("joke", joke_command))
        
        # Запускаем бота
        logger.info("Бот-анекдотчик запускается...")
        print("🤖 Бот запущен! Для остановки нажми Ctrl+C")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        print(f"❌ Ошибка: {e}")
    finally:
        logger.info("Бот остановлен")
        print("👋 Бот остановлен")

if __name__ == "__main__":
    main()