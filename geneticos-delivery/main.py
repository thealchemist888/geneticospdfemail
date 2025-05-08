from fastapi import FastAPI
from routes.deliver import router as deliver_router

app = FastAPI(
    title="Genetic OS Delivery Service",
    description="Service for delivering Genetic OS reports via PDF and email",
    version="1.0.0"
)

# Include routers
app.include_router(deliver_router, prefix="/deliver", tags=["delivery"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 