from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

# Import routers
from backend.app.routers import advisory

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("🚀 Digital Advisory API starting up...")
    logger.info(f"Environment: {os.getenv('ENVIRONMENT')}")
    yield
    # Shutdown
    logger.info("🛑 Digital Advisory API shutting down...")

# Create FastAPI app
app = FastAPI(
    title="Digital Advisory OS API",
    description="Production-grade financial advisory engine for Kenya",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
allowed_origins = os.getenv("CORS_ORIGINS", "['http://localhost:3000']")
import json
try:
    allowed_origins = json.loads(allowed_origins)
except:
    allowed_origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "environment": os.getenv("ENVIRONMENT"),
        "service": "digital-advisory-api"
    }

# Include routers
app.include_router(advisory.router, prefix="/api/advisory", tags=["Advisory"])

@app.get("/")
async def root():
    return {
        "message": "Digital Advisory OS API",
        "version": "1.0.0",
        "docs": "/docs"
    }    
