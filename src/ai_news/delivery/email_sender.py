"""
email_sender.py - Gmail SMTP sender

Learn: SMTP, MIME messages, HTML emails
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from jinja2 import Template
from ..models import Digest
from ..config import settings


class EmailSender:
    def __init__(self):
        self.template_path = Path("templates/digest_email.html")

    def send(self, digest: Digest):
        template = Template(self.template_path.read_text())
        html = template.render(digest=digest)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"AI News Digest - {digest.generated_at.strftime('%B %d, %Y')}"
        msg["From"] = settings.gmail_address
        msg["To"] = settings.gmail_address
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(settings.gmail_address, settings.gmail_password)
            server.send_message(msg)
