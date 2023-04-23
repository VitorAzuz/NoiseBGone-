import telebot
import smtplib
from email.mime.text import MIMEText

# Insira o token de acesso do seu bot aqui
token = '6042171980:AAFssLfJ8Gb0eIzGFeh0PHkCA0vu4Qx8DQo'

# Credenciais de acesso à sua conta de e-mail
email_user = 'NBGufrpe@outlook.com'
email_password = 'ufrpe123'
email_to = 'vitorjorge88@hotmail.com'

# Cria uma instância do bot
bot = telebot.TeleBot(token)

# Manipulador de mensagens para receber os valores
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Verifica se a mensagem recebida contém apenas números
    if message.text.isnumeric():
        # Adiciona o valor recebido à lista de valores
        valores.append(int(message.text))
        
        # Verifica se já recebeu valores de todos os dispositivos
        if len(valores) == 3:
            # Calcula a média dos valores
            media = sum(valores) / len(valores)
            
            # Envia a resposta com a média calculada
            bot.reply_to(message, f"A média dos valores é {media:.2f}")
            
            # Envia o resultado por e-mail
            enviar_email(media)
            
            # Limpa a lista de valores para uma nova média ser calculada
            valores.clear()

# Lista para armazenar os valores recebidos
valores = []

def enviar_email(media):
    # Configura a mensagem a ser enviada
    mensagem = MIMEText(f"A média dos valores é {media:.2f}")
    mensagem['From'] = email_user
    mensagem['To'] = email_to
    mensagem['Subject'] = 'Resultado da média'
    
    # Conecta ao servidor de e-mail e envia a mensagem
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_to, mensagem.as_string())
    server.quit()

# Inicia o bot
bot.polling()