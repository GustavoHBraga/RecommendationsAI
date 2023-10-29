import smtplib
from email.mime.text import MIMEText
import dotenv
import os 

dotenv.load_dotenv(dotenv_path=r".\.env")

def send_email(to, subject, body):
    sender = os.getenv("STMP_EMAIL_LOGIN")
    password = os.getenv("STMP_EMAIL_PASSWORD") 

    msg = MIMEText(body)
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = subject

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server
        smtp_server.starttls()
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, to, msg.as_string())
        smtp_server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example of usage
if __name__ == "__main__":
    # Generate emails randomly with https://temp-mail.org/
    send_email('tocaw69453@undewp.com', 'Email Subject', 'Email Body')