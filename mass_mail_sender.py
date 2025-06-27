import pandas as pd
import yagmail

YOUR_EMAIL = "introvertaniket@gmail.com"
APP_PASSWORD = "nspznayajqtdcpyi"

def load_contacts(filename):
    df = pd.read_csv(filename)
    return df

def send_mass_emails():
    contacts = load_contacts("contacts.csv")
    yag = yagmail.SMTP(YOUR_EMAIL, APP_PASSWORD)

    for index, row in contacts.iterrows():
        name = row['Name']
        email = row['Email']
        message = row['Message']

        subject = f"Hello {name}, this is a test email"
        body = f"Hi {name},\n\n{message}\n\nFrom,\nAniket"

        try:
            yag.send(to=email, subject=subject, contents=body)
            print(f"✅ Email sent to {name} ({email})")
        except Exception as e:
            print(f"❌ Failed to send email to {email}: {e}")

send_mass_emails()
