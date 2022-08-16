import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib

from . import logger


@logger.catch
async def send_email(form_data):
    sender = os.getenv('MAIL_USERNAME')
    password = os.getenv('MAIL_PASSWORD')

    server = aiosmtplib.SMTP('smtp.gmail.com', 587)
    await server.connect()
    await server.starttls()

    try:
        await server.login(sender, password)
    except Exception as _ex:
        logger.exception(_ex)

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = sender
    msg['Subject'] = 'Hey there!'

    if form_data.message:
        msg.attach(MIMEText(form_data.message))

    if form_data.template:
        try:
            with open('email_template.html', encoding='utf-8') as f:
                template = f.read()
        except IOError as error:
            logger.exception(error)
            template = None
        else:
            if template is not None:
                msg.attach(MIMEText(template, 'html'))

    if form_data.file[0]:
        for item in form_data.file:
            file_type, subtype = item.content_type.split('/')
            file = MIMEBase(file_type, subtype)
            file.set_payload(await item.read())
            encoders.encode_base64(file)

            file.add_header(
                'content-disposition', 'attachment', filename=item.filename
            )

            msg.attach(file)

    await server.send_message(msg)
    await server.quit()

    return 'The message was sent successfully!'
