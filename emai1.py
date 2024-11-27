import smtplib 
import email.message

##def enviar_email():
 ##   corpo_email = """
 ##   <p>Olá Usuário</p>
##    <p>AAqui estão os indicadores mais recentes:</p>
 ##   """


def criar_corpo_email(registros):
    corpo_email = "<h2>Indicadores de Sensores</h2>"
    for registro in registros:
        temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro = registro
        corpo_email += f"""
        <p>Data: {tempo_registro}</p>
        <ul>
            <li>Temperatura: {temperatura} °C</li>
            <li>Pressão: {pressao} Pa</li>
            <li>Altitude: {altitude} m</li>
            <li>Umidade: {umidade} %</li>
            <li>CO2: {co2} ppm</li>
            <li>Poeira: {poeira} µg/m³</li>
        </ul>
        <hr>
        """
    return corpo_email

    msg = email.message.Message()
    msg['Subject'] = "Indicadores"
    msg['From'] = 'projetosenai.cd24@gmail.com'
    msg['To'] = 'clodoaldo.batista.s@gmail.com, eliane.bdsantos@gmail.com'
    password = "cdol xorh tmlf inpz"
    msg.add_header('Contect-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'],password)
    s.sendmail(msg['From'], msg['To'].split(','), msg.as_string().encode('utf-8'))
    print('Email enviado')
    
if __name__ == "__main__":
    enviar_email()