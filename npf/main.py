import uvicorn
from fastapi import FastAPI
from core.logger import logger_setup
from core.config import settings
from fastapi.responses import ORJSONResponse
from core.init import init_cors

from api.v1 import file, health


logger_setup()


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    description="NPF upload file",
    version="1.0.0"
)

init_cors(app=app)


app.include_router(
    file.router,
    prefix='/api/v1/file',
    tags=['File']
)

app.include_router(
        health.router,
        prefix='/health',
        tags=['Статус']
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
