import smtplib
import random
import string
import sqlite3

# Generate OTP
def generate_otp(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Function to send email with OTP
def send_email(email, otp):
    # Email configuration
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'
    smtp_server = 'smtp.example.com'
    smtp_port = 587

    # Compose message
    subject = 'Your OTP for Verification'
    body = f'Your OTP is: {otp}'
    message = f'Subject: {subject}\n\n{body}'

    # Connect to SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message)

# Connect to your database
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

# Retrieve email from the database (replace 'your_query' with your SQL query)
cursor.execute("SELECT * FROM USER WHERE Email=?", (email,)")
email = cursor.fetchone()[0]  # Assuming the email is in the first column

# Generate OTP
otp = generate_otp()

# Send email with OTP
send_email(email, otp)

# Close database connection
conn.close()
