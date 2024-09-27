import smtplib
from src.send_image.constants import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from src.send_image.utils.common import read_yaml

class Send_Email:
    def __init__(self,
                email_to,
                config_filepath = CONFIG_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.email_to = email_to
        self.load_config()

    def load_config(self):
        # Assign constant values from configuration
        self.smtp_server = self.config.smtp_server
        self.email_from= self.config.email_from
        self.smtp_port = self.config.smtp_port
        self.subject = self.config.subject
        self.filname = self.config.filname
        self.psw = self.config.psw

    def send_email(self):
        # Make the body of the email
        body = f""" 
        <html>
            <body>
        <p>Hello,</p>
        <p>This is an example email body with an image.</p>
        <img src="cid:image1"><br>
        <p>Best regards,<br>Sender</p>
            </body>
        </html>
        """

        # Make the message
        msg = MIMEMultipart()
        msg['From'] = self.email_from
        msg['To'] = self.email_to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(body, 'html'))

        # Load the image file
        with open(self.filname, 'rb') as img_file:
            
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)
        
        # Cast as string
        text = msg.as_string()

        # Connecting to the server
        print("Connecting to server ...")
        TIE_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        TIE_server.starttls()
        TIE_server.login(self.email_from, self.psw)
        print("Successfully connected to server ...")
        print()

        # Send email to person
        print(f"Sending email to - {self.email_to}")
        TIE_server.sendmail(self.email_from, self.email_to, text)
        print(f"Email successfully sent to - {self.email_to}")
        print()
        TIE_server.quit()

# Example usage:
# email_sender = Send_Email('your_email@example.com', 'recipient@example.com')
# email_sender.send_email()

