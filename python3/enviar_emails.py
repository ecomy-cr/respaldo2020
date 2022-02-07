#Importante el correo que se use
#para enviar los emails debe tener activada 
#la opcion de aplicaciones de terceros
#link:   https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Ojt1DghzRnCVLArDyc7Rx0JZrGHAySL7RVsenMLNbboJkgcqDcTibyDFXzQIdqPLGz0-V5n3S8py5r9VydKtjY0l7Q_Q

#librerias necesarias
import smtplib
import ssl
from email.message import EmailMessage

#cuerpo del email en proceso
subject = "Gmail - Email - Python SMTP"
body = "Enviando correo por Gmail automatizado con python"



#datos de envio EMAILS
email_de_envio = 'aqui el correo de envio solo @gmail.com'
email_que_recibe = 'aqui el correo que recibe'
password = 'aqui la contrase;a del correo que enviara el sms'

sender_email = email_de_envio
receiver_email = email_que_recibe



try:
    #configuracion del paquete 
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject


    #cuerpo del paquete
    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """


    message.add_alternative(html, subtype="html")
    context = ssl.create_default_context()

    mensaje_info = 'Enviando el mensaje destinatario:{0}    quien envia:{1}!'.format(sender_email, receiver_email)
    print(mensaje_info)

    #conectando con los servidores gmail y enviando
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password) #iniciando sesion
        server.sendmail(sender_email, receiver_email, message.as_string())#enviando el correo

    #envio con exito
    
    #puedes crear una lista de correos destinatarios y enviar el 
    #message a todos mediante un bucle for
    print("Enviado con exito")
    
except Exception as e:
    print('Error: ')