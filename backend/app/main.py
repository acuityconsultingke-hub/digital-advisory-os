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
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get connection string
db_user = os.getenv("DB_USER", "advisory_app")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME", "digital_advisory")
db_instance = os.getenv("DB_INSTANCE", "digital-advisory-prod:us-central1:advisory-postgres-prod")

# For Cloud Run with Cloud SQL Proxy
if os.getenv("ENVIRONMENT") == "production":
    # Unix socket connection (Cloud Run + Cloud SQL)
    DATABASE_URL = f"postgresql://{db_user}:{db_password}@/{db_name}?host=/cloudsql/{db_instance}"
else:
    # Regular TCP connection (local development)
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_size=int(os.getenv("DB_POOL_SIZE", "10")),
    max_overflow=int(os.getenv("DB_MAX_OVERFLOW", "20")),
    echo=os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
