import smtplib
import ssl
import certifi
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def open(self):
        context = ssl.create_default_context(cafile=certifi.where())
        
        if self.use_ssl:
            self.connection = smtplib.SMTP_SSL(self.host, self.port, context=context)
        else:
            self.connection = smtplib.SMTP(self.host, self.port)
            if self.use_tls:
                self.connection.starttls(context=context)
        
        self.connection.login(self.username, self.password)

    def close(self):
        if self.connection:
            self.connection.quit()
