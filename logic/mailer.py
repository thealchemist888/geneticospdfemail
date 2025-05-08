from resend import Resend
import os
from typing import BinaryIO
from dotenv import load_dotenv
import base64

# Load environment variables from .env file
load_dotenv()

def send_report_email(to_email: str, pdf_path: str) -> None:
    resend = Resend(api_key=os.getenv("RESEND_API_KEY"))
    
    with open(pdf_path, "rb") as pdf_file:
        pdf_content = pdf_file.read()
    
    try:
        response = resend.emails.send({
            "from": "Genetic OS <onboarding@resend.dev>",
            "to": "normangrande@gmail.com"",
            "subject": "Your Genetic OS Report is Ready",
            "text": "Your Genetic OS report is ready! Please find it attached to this email.",
            "attachments": [
                {
                    "filename": "genetic_report.pdf",
                    "content": base64.b64encode(pdf_content).decode('utf-8')
                }
            ]
        })
        print(f"Email sent successfully: {response}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        raise 