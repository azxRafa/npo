from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def init_cors(app: FastAPI) -> None:
    origins = [
        "http://localhost",
        "http://localhost:80",
        "http://127.0.0.1",
        "http://127.0.0.1:80",
        "http://nginx",
        "http://nginx:80",
        "http://backend:8000",
    ]

    # origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
