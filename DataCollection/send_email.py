from email.mime.text import MIMEText
import smtplib

def send_email(usr_email, height, avg_height, count):
    from_email = "myheightstats@gmail.com"
    from_password = "4mp3gb4r@1"
    to_email = usr_email

    subject = "Height data"
    message = f"Hey there, your height is <strong>{height}</strong> cm. Average height of all is <strong>{avg_height}</strong> cm. and that is calculated out of <strong>{count}</strong> people."

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
