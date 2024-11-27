import mysql.connector
import smtplib
import email.message
import schedule
import time


def buscar_dados():
    # Conectar ao banco de dados
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="senai@134",
        db="bd_medidor"
    )
    
    cursor = conn.cursor()
    query = "SELECT temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro FROM tb_registro"
    cursor.execute(query)
    
    # Obter os dados
    registros = cursor.fetchall()
    cursor.close()
    conn.close()

    return registros


def criar_corpo_email(registros):
    corpo_email = "<h2><b>ECO SYSTEM CALL - Indicadores de Sensores</b></h2>"
#    for registro in registros:
#        temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro = registro
#        corpo_email += f"""
#        <p>Data: {tempo_registro}</p>
#        <ul>
#            <li>Temperatura: {temperatura} °C</li>
#            <li>Pressão: {pressao} Pa</li>
#            <li>Altitude: {altitude} m</li>
#            <li>Umidade: {umidade} %</li>
#            <li>CO2: {co2} ppm</li>
#            <li>Poeira: {poeira} µg/m³</li>
#        </ul>
#        <hr>
#        """


def criar_corpo_email(registros):
    temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro = registros[0]
    corpo_email = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #333333; text-align: center;">Indicadores de Sensores</h2>
            <p style="color: #555555; text-align: center;">Data: {tempo_registro}</p>
            <ul style="list-style-type: none; padding: 0;">
                <li style="padding: 10px; border-bottom: 1px solid #eeeeee;">
                    <strong>Temperatura:</strong> {temperatura} °C
                </li>
                <li style="padding: 10px; border-bottom: 1px solid #eeeeee;">
                    <strong>Pressão:</strong> {pressao} Pa
                </li>
                <li style="padding: 10px; border-bottom: 1px solid #eeeeee;">
                    <strong>Altitude:</strong> {altitude} m
                </li>
                <li style="padding: 10px; border-bottom: 1px solid #eeeeee;">
                    <strong>Umidade:</strong> {umidade} %
                </li>
                <li style="padding: 10px; border-bottom: 1px solid #eeeeee;">
                    <strong>CO2:</strong> {co2} ppm
                </li>
                <li style="padding: 10px; border-bottom: 1px solid #eeeeee;">
                    <strong>Poeira:</strong> {poeira} µg/m³
                </li>
            </ul>
            <hr style="border: none; border-top: 1px solid #eeeeee;">
        </div>
    </body>
    </html>
    """
    return corpo_email


def enviar_email(corpo_email):
    msg = email.message.Message()
    msg['Subject'] = "ECO SYSTEM CALL - Indicadores de Sensores"
    msg['From'] = 'projetosenai.cd24@gmail.com'
    msg['To'] = 'clodoaldo.batista.s@gmail.com, eliane.bdsantos@gmail.com, projetosenai.cd24@gmail.com, mauriciodealmeidafernandes@gmail.com'
    password = "cdol xorh tmlf inpz"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'].split(','), msg.as_string().encode('utf-8'))
    s.quit()
    print("Email enviado")


if __name__ == "__main__":
    registros = buscar_dados()
    corpo_email = criar_corpo_email(registros)
    enviar_email(corpo_email)

#schedule.every().day.at("20:56").do()

#while True:
#    schedule.run_pending()  
#    time.sleep(1)
