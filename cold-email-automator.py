from email import encoders
from email.base64mime import body_decode
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import pandas as pd

emails = pd.read_csv('emails.csv')

print(emails)

port = 465  # For SSL
context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)

server.login("menteharshith@gmail.com", "cenu bqfv jlor mqjs")

for index in range(len(emails)):
    # Create a multipart message container
    message = MIMEMultipart()
    message["From"] = "menteharshith@gmail.com"
    message["To"] = emails["Emails"][index]
    message["Subject"] = "Application for Internship/SDE Role"

    # Attach the plain text message
    body = f"""\
Dear {emails["Names"][index]},
I hope this email finds you well. 

My name is Harshith Mente, and I am writing to express my interest in applying for internship and Software Development Engineer (SDE) roles within your organization.

I am a motivated and dedicated individual with a strong passion for software development. I specialize in building robust and scalable web applications using the MERN stack - MongoDB, Express, React, and Node.js. I am experienced in building RESTful APIs and have a deep understanding of front-end development, including HTML, CSS, and JavaScript. I am also proficient in UI/UX design, using tools such as Adobe XD, Figma, and Sketch to create beautiful and functional designs.
Thank you for considering my application.

I have attached my resume for your reference. I am available for an interview at your earliest convenience.
I look forward to the opportunity to discuss how my skills and experiences align with the goals of your organization.

Sincerely,
Harshith Mente
"""
    message.attach(MIMEText(body, "plain"))

    resume_file_path = "HarshithResume.pdf"  
    with open(resume_file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=HarshithResume.pdf",
        )
        message.attach(part)

    # Send the email inside the loop
    server.sendmail("menteharshith@gmail.com", emails["Emails"][index], message.as_string())
    print(f"Sent email to {emails['Names'][index]}")

# Close the connection outside the loop
server.quit()
