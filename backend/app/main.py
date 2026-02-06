from fastapi import FastAPI
from contextlib import asynccontextmanager
from .core.cors import setup_cors
from .db.session import SessionLocal, engine
from .db.base import Base
from .db.init_db import init_db
from .routes import auth, categories, products, packs, orders, admin, uploads


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables and seed data
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()
    yield
    # Shutdown


app = FastAPI(
    title="FoodNova API",
    description="Food ordering and grocery delivery API",
    version="1.0.0",
    lifespan=lifespan
)

# Setup CORS
setup_cors(app)

# Include routers with /api prefix
app.include_router(auth.router, prefix="/api")
app.include_router(categories.router, prefix="/api")
app.include_router(products.router, prefix="/api")
app.include_router(packs.router, prefix="/api")
app.include_router(orders.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(uploads.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/api")
async def api_root():
    return {"message": "Welcome to FoodNova API"}
