from resend import Resend
import os
from typing import BinaryIO

def send_report_email(to_email: str, pdf_path: str) -> None:
    resend = Resend(api_key=os.getenv("RESEND_API_KEY"))
    
    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()
    
    resend.emails.send({
        "from": "no-reply@geneticos.app",
        "to":"normangrande@gmail.com" //to_email,
        "subject": "Your Genetic OS Report is Ready",
        "text": "Your Genetic OS report is ready! Please find it attached to this email.",
        "attachments": [
            {
                "filename": "genetic_report.pdf",
                "content": pdf_content
            }
        ]
    }) 