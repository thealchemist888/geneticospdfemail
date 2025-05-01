# Genetic OS Delivery Service

A FastAPI microservice that handles the delivery of Genetic OS reports via PDF and email.

## Features

- Converts markdown reports to styled PDFs
- Sends PDF reports via email using Resend API
- Integrates with existing Genetic OS database

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# .env file
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
RESEND_API_KEY=your_resend_api_key
```

## Running the Service

```bash
uvicorn main:app --reload
```

The service will be available at `http://localhost:8000`

## API Endpoints

### POST /deliver/report

Delivers a report as a PDF via email.

Request body:
```json
{
  "report_id": "uuid-here"
}
```

## Dependencies

- FastAPI
- SQLAlchemy
- WeasyPrint
- Resend API
- Python-Markdown 