from logic.mailer import send_report_email
import os

def test_email_sending():
    # Create a test PDF file
    pdf_path = "test_report.pdf"
    with open(pdf_path, "wb") as f:
        f.write(b"Test PDF content")
    
    try:
        # Try to send the email
        send_report_email("test@example.com", pdf_path)
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        # Clean up
        if os.path.exists(pdf_path):
            os.unlink(pdf_path)

if __name__ == "__main__":
    test_email_sending() 