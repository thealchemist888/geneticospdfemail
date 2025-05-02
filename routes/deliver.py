from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID
import tempfile
import os

from models import GeneticReport, User
from logic.pdf_renderer import render_markdown_to_pdf
from logic.mailer import send_report_email
from database import SessionLocal

router = APIRouter()

class ReportDeliveryRequest(BaseModel):
    report_id: UUID

@router.post("/report")
async def deliver_report(request: ReportDeliveryRequest):
    db = SessionLocal()
    try:
        # Get the report
        report = db.query(GeneticReport).filter(GeneticReport.id == request.report_id).first()
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        
        # Get the user's email
        user = db.query(User).filter(User.id == report.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Create a temporary file for the PDF
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            pdf_path = temp_pdf.name
        
        try:
            # Render the PDF
            render_markdown_to_pdf(report.raw_assistant_response, pdf_path)
            
            # Send the email
            send_report_email(user.email, pdf_path)
            
            return {"status": "success", "message": "Report delivered successfully"}
        finally:
            # Clean up the temporary file
            if os.path.exists(pdf_path):
                os.unlink(pdf_path)
    finally:
        db.close() 