from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID
import tempfile
import os
import logging

from models import GeneticReport, User
from logic.pdf_renderer import render_markdown_to_pdf
from logic.mailer import send_report_email
from database import SessionLocal

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class ReportDeliveryRequest(BaseModel):
    id: UUID = Field(..., description="The UUID of the report to deliver")

@router.post("/report")
async def deliver_report(request: ReportDeliveryRequest):
    logger.info(f"Processing report delivery request for id: {request.id}")
    db = SessionLocal()
    try:
        # Get the report using the id field
        report = db.query(GeneticReport).filter(GeneticReport.id == request.id).first()
        if not report:
            logger.error(f"Report not found: {request.id}")
            raise HTTPException(status_code=404, detail="Report not found")
        
        logger.info(f"Found report for user_id: {report.user_id}")
        
        # Get the user's email
        user = db.query(User).filter(User.id == report.user_id).first()
        if not user:
            logger.error(f"User not found for user_id: {report.user_id}")
            raise HTTPException(status_code=404, detail="User not found")
        
        logger.info(f"Found user email: {user.email}")
        
        # Create a temporary file for the PDF
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            pdf_path = temp_pdf.name
        
        try:
            # Render the PDF
            logger.info("Rendering PDF from report content")
            render_markdown_to_pdf(report.raw_assistant_response, pdf_path)
            
            # Send the email
            logger.info(f"Sending email to: {user.email}")
            send_report_email(user.email, pdf_path)
            
            logger.info("Report delivery completed successfully")
            return {"status": "success", "message": "Report delivered successfully"}
        except Exception as e:
            logger.error(f"Error during PDF generation or email sending: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error processing report: {str(e)}")
        finally:
            # Clean up the temporary file
            if os.path.exists(pdf_path):
                os.unlink(pdf_path)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    finally:
        db.close() 