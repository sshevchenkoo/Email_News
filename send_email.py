import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_email = "Your_Email@gmail.com"
    password = "Your_Email_Password"
    receiver = "Receiver_Email@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)
