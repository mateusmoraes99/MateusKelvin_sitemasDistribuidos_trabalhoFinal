# bot/bot.py
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
from .handlers import iniciar_reserva, receber_quarto, receber_nome, receber_data, cancelar, listar_suites, checkin
from .database import criar_banco

def main():
    criar_banco()

    application = ApplicationBuilder().token('SEU_TOKEN_DO_TELEGRAM').build()

    reserva_handler = ConversationHandler(
        entry_points=[CommandHandler('reserva', iniciar_reserva)],
        states={
            QUARTO: [MessageHandler(filters.TEXT, receber_quarto)],
            NOME: [MessageHandler(filters.TEXT, receber_nome)],
            DATA: [MessageHandler(filters.TEXT, receber_data)],
        },
        fallbacks=[CommandHandler('cancelar', cancelar)]
    )

    application.add_handler(CommandHandler('suites', listar_suites))
    application.add_handler(reserva_handler)
    application.add_handler(CommandHandler('checkin', checkin))

    application.run_polling()

if __name__ == '__main__':
    main()
