
"""we first import the necessary libraries, thennnnnnnnnn, we get to connect to the 
server using ssl and then we login suing smtp.login(sender, password) then we start creting 
our letter using EmailMessage(). so the thing is
we need a to, from, subject and connect all using msg
msg["To"]
msg.set_content(input content here)
smtp.send_message(msg)
smtp.quit()
"""



import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog
import mimetypes


smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

#to, from, conten, subject


sender = "anthonympaulino1@gmail.com"  #this is the sender
password = "zbcbfawfjbwcxcwg" # 16-digit code


msg = EmailMessage()

msg["From"] = sender

#receiver = "anthonymichael680@gmail.com, boldengbol700@gmail.com"  
#subject = "readdddddddddddddddd. leave tiktok"









smtp.login(sender, password)




#we need to login
#set content
#send message
#quit to cancel the connection

while True:
    print("*" *50)
    print("WELCOME TO THE EMAIL SENDER PROGRAM.")
    print("*" *50)


    recipient = input("Who is the email recipient?: \n")
    msg["To"] = recipient


    subject = input("Subject: \n")
    msg["Subject"] = subject


    content = input("Content: \n")
    msg.set_content(content)

    option = input("\n Do you want to send an image?(yes or no): \n")

    if option.lower() == "yes":


        # open file picker
        root = tk.Tk()
        root.withdraw()        

      """This is for effectively creating a dialogue and an option to choose which files we will need """

        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )

        if file_path:  # user selected something

            with open(file_path, "rb") as f:
                file_data = f.read()

            mime_type, _ = mimetypes.guess_type(file_path)
            maintype, subtype = mime_type.split("/")

            msg.add_attachment(
                file_data,
                maintype=maintype,
                subtype=subtype,
                filename=file_path.split("/")[-1]
            )
        
        break

    elif option == "no":
        print("No attachment is placed. \n")
        break
    else:
        print("Choose a correct option. \n")



smtp.send_message(msg)  #sends the email

print("Your email has been sent successfully! \n")

smtp.quit()   #closes the session
