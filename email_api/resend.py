import resend
import random
from dotenv import load_dotenv
import os

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

def resend_api(to_person: str, length=4):
    try:
        min_value = 10**(length-1)
        max_value = (10**length) - 1
        MFA_Code = random.randint(min_value, max_value)
        params = {
            "from": "onboarding@resend.dev",
            "to": [to_person],
            "subject": "MFA Code",
            "html": f"<strong>Sign in code: {MFA_Code}</strong>"
        }

        r = resend.Emails.send(params)
        print(r)

        return ("Ok", MFA_Code)
    except:
        return ("Error", -999)
    pass

if __name__ == "__main__":
    print(resend_api("your_email@gmail.com"))