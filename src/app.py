from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import ivf_router


app = FastAPI(

    title="Sunfish Backend",
    version = "1.0",
    description = "Sunfish Backend"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],  # Specify allowed methods
    allow_headers=["Content-Type", "Authorization"], # Specify allowed headers
)

app.include_router(ivf_router.router)
