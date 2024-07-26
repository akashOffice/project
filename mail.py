"""SMTP email backend class."""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, from_password):
    # Create the container email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create the SMTP server object
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        # Login to the email server
        server.login(from_email, from_password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print(f'Failed to send email: {e}')

    finally:
        # Terminate the SMTP session and close the connection
        server.quit()

# Example usage
subject = 'Test Email'
body = 'This is a test email sent from a Python script.'
to_email = 'akashrawat851.ar@gmail.com'
from_email = 'akashrawat851.ap@gmail.com'
from_password = 'ydrd caam dznw kvge'

send_email(subject, body, to_email, from_email, from_password)
