from string import Template
from datetime import datetime

meu_email = 'filipe.henrique.reis@gmail.com'
meu_senha = 'Fhlr1992'

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Luiz Otavvio', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Filipe Henrique Leite dos Reis'
msg['to'] = meu_email
msg['subject'] = 'Atencao: este é um email de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, meu_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail nao enviado...')
        print('Erro: ', e)
