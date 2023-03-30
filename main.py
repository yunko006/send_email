import os
from dotenv import load_dotenv
import yagmail
from utils import get_epub_file, move_file


load_dotenv()

SENDER = os.getenv("gmail_username")
PASSWORD = os.getenv("gmail_password")
RECEIVER = os.getenv("gmail_username")

def send_email(str_input):
    body = ""
    # filename = "document.pdf"
    files = get_epub_file(str_input)

    yag = yagmail.SMTP(SENDER, PASSWORD)
    yag.send(
        to=RECEIVER,
        subject="Livres",
        contents=body, 
        attachments=[file for file in files],
    )


if __name__ == "__main__":
    str_input = str(input('Path : ["telegram" ou "telechargement]: '))
    send_email(str_input)
    print('email envoyé.')
    move_file(str_input)
    print("terminé.")
