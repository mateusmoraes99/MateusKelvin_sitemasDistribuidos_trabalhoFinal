# bot/handlers.py
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from .database import inserir_reserva, verificar_reserva, realizar_checkin, listar_suites

# Estados da conversa
NOME, DATA, QUARTO = range(3)

# Função para listar suítes
async def listar_suites(update: Update, context):
    suites = listar_suites()
    resposta = "Suítes Disponíveis:\n\n" + "".join([f"🏨 {s[0]}: {s[1]}\n\n" for s in suites])
    await update.message.reply_text(resposta)

# Fluxo de reserva
async def iniciar_reserva(update: Update, context):
    suites = listar_suites()
    opcoes_suites = [[suite[0]] for suite in suites]
    markup = ReplyKeyboardMarkup(opcoes_suites, one_time_keyboard=True)
    await update.message.reply_text("Por favor, selecione o tipo de quarto:", reply_markup=markup)
    return QUARTO

async def receber_quarto(update: Update, context):
    context.user_data['tipo_quarto'] = update.message.text
    await update.message.reply_text("Informe seu nome completo.")
    return NOME

async def receber_nome(update: Update, context):
    context.user_data['nome'] = update.message.text
    await update.message.reply_text("Agora, informe a data de chegada (AAAA-MM-DD).")
    return DATA

async def receber_data(update: Update, context):
    nome = context.user_data['nome']
    data_chegada = update.message.text
    tipo_quarto = context.user_data['tipo_quarto']
    inserir_reserva(nome, data_chegada, tipo_quarto)
    await update.message.reply_text(f"Reserva confirmada para {nome} na data {data_chegada}.")
    return ConversationHandler.END

# Função para realizar check-in
async def checkin(update: Update, context):
    nome = update.message.text.split("/checkin ")[1]
    reserva = verificar_reserva(nome)
    if reserva:
        realizar_checkin(reserva[0])
        await update.message.reply_text(f"Check-in realizado para {nome}.")
    else:
        await update.message.reply_text("Nenhuma reserva encontrada ou check-in já realizado.")
