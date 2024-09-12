# bot/database.py
import sqlite3

def criar_banco():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_chegada TEXT NOT NULL,
            tipo_quarto TEXT NOT NULL,
            checkin_realizado INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO suites (nome, descricao)
        VALUES
        ('Simples', 'Quarto simples para uma pessoa.'),
        ('Duplo', 'Quarto para duas pessoas.'),
        ('Suíte', 'Suíte com mais conforto e espaço.')
    ''')

    conn.commit()
    conn.close()

def inserir_reserva(nome, data_chegada, tipo_quarto):
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservas (nome, data_chegada, tipo_quarto)
        VALUES (?, ?, ?)
    ''', (nome, data_chegada, tipo_quarto))
    conn.commit()
    conn.close()

def verificar_reserva(nome):
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservas WHERE nome = ? AND checkin_realizado = 0', (nome,))
    reserva = cursor.fetchone()
    conn.close()
    return reserva

def realizar_checkin(reserva_id):
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE reservas SET checkin_realizado = 1 WHERE id = ?', (reserva_id,))
    conn.commit()
    conn.close()

def listar_suites():
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, descricao FROM suites')
    suites = cursor.fetchall()
    conn.close()
    return suites
