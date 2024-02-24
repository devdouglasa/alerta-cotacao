import smtplib
import email.message, requests
from time import sleep

cotacao_anterior = 0

def enviar_email(cotacao: float):
    corpo_email = f"""
    <h1>COTAÇÃO DO DÓLAR</h1>

    <h2>A cotação atual do dólar é {cotacao}</h2>
    """

    msg = email.message.Message()
    msg['Subject'] = "TESTE SEND"
    msg['From'] = 'douglasalisson27@gmail.com'
    msg['To'] = 'douglasalisson27@gmail.com'
    password = 'vjdwrygwfofaidmx'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


print('Initializing App...')

while True:
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    response = requests.get(url=url)
    response_json = response.json()
    cotacao_atual = float(response_json['USDBRL']['bid'])
    if cotacao_atual != cotacao_anterior:
        enviar_email(cotacao_atual)
        cotacao_anterior = cotacao_atual
        print(cotacao_atual)
    sleep(10)

