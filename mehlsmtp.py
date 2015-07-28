#!/usr/bin/env python
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
"""mehl smtp routines"""
__author__      = "Rodrigo Marin"
__copyright__   = "Copyright 2015, Rodrigo Marin"
__credits__     = ["Rodrigo Marin"]
__license__     = "GPL"
__version__     = "0.1"
__maintainer__  = "Rodrigo Marin"
__email__       = "rodrigo.f.marin@gmail.com"
__status__      = "Development"

def sendmessage(smtpserver, sender, recipient, data):
    """sends supplied data to the specified smtp server"""
    __sender = sender
    __recipient = recipient

    date = time.strftime("%m/%d/%Y")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "meh.com deal for {0}".format(date)
    msg['From'] = __sender
    msg['To'] = __recipient

    # Create the body of the message (a plain-text and an HTML version).
    text = "meh.com daily deal for {0}".format(date)

    #assign the data passed in to 'html'
    html = data

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP(smtpserver)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
    