# MateusKelvin_sitemasDistribuidos_trabalhoFinal

# Hotel Telegram Chatbot

Este é um projeto de chatbot de Telegram para gerenciar reservas de um hotel. O chatbot permite que os usuários vejam as suítes disponíveis, façam reservas e realizem check-in. O bot é construído com Python, SQLite, Docker, e a biblioteca `python-telegram-bot`.

## Funcionalidades

- Listar as suítes disponíveis.
- Fazer reservas especificando nome, data de chegada e tipo de quarto.
- Realizar check-in em reservas existentes.


## Pré-requisitos

- Docker e Docker Compose instalados.
- Um token do Telegram para o bot.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/username/hotel_bot.git
   cd hotel_bot
 Crie um arquivo .env com seu token de bot do Telegram:
 
    echo 'TELEGRAM_TOKEN=SEU_TOKEN_DO_TELEGRAM' > .env
    
 Construa e execute o contêiner com Docker Compose:  

    docker-compose up --build

Comandos do Bot
/suites: Lista as suítes disponíveis.
/reserva: Inicia o processo de reserva.
/checkin Nome: Realiza o check-in para uma reserva existente.
 
Com essa organização, seu projeto ficará bem estruturado e fácil de manter.
   

