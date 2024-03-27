
import resend
import random

resend.api_key = "re_jTo72F9W_DCWC33TAKzvEF9Rk4t7iGkNR"

otp = '{:06d}'.format(random.randint(0, 999999))

def send_email(emailid="adityadattaofficial@gmail.com"):
    params = {
        "from": "Acme <onboarding@resend.dev>",
        "to": [emailid],
        "subject": "hi",
        "html": f"<strong>{otp}</strong>",

    }

    email = resend.Emails.send(params)
    return otp
# v=send_email()
# print(v)