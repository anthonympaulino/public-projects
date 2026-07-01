
import smtplib
from email.message import EmailMessage

smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

sender = "anthonympaulino1@gmail.com"  #this is the sender
password = "zbcbfawfjbwcxcwg" # 16-digit code
receiver = "anthonymichael680@gmail.com, boldengbol700@gmail.com"  #this is the receiver
subject = "bol"
message = "Hello, how are you?????"

smtp.login(sender, password)


msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

msg.set_content("This is a new email.")

smtp.send_message(msg)

smtp.quit() #this ends the session or disconnect