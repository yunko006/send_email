import os
from dotenv import load_dotenv
import yagmail

# from yagmail.error import SMTPSenderRefused
import smtplib
from utils import get_epub_file, move_file


load_dotenv()

SENDER = os.getenv("gmail_username")
PASSWORD = os.getenv("gmail_password")
RECEIVER = os.getenv("email_receiver")


def send_email(files):
    body = ""

    try:
        yag = yagmail.SMTP(SENDER, PASSWORD)
        yag.send(
            to=RECEIVER,
            subject="Livresss",
            contents=body,
            attachments=[file for file in files],
        )
        print("l'email a bien été envoyé.")

    except smtplib.SMTPException:
        print("fichier trop volumineux")

    except Exception as e:
        print(f"erreur: {e}")


if __name__ == "__main__":
    str_input = str(input('Path : ["telegram" ou "telechargement]: '))
    files = get_epub_file(str_input)
    send_email(files)
    print("email envoyé.")
    move_file(files)
    print("terminé.")
