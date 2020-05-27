import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Zain Abbas'
email['to'] = '17-SE-103@students.uettaxila.edu.pk'
email['subject'] = 'You Won $1 Million'
email.set_content(html.substitute(name='Zain'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zainabbas0987@gmail.com', 'CompLab@12')
    smtp.send_message(email)
    print('Message Sent...')
