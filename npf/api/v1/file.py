from fastapi import (
    APIRouter,
    status,
    UploadFile,
    File,
    HTTPException,
    Depends
)

from services.file import get_file_service, FileService


router = APIRouter()


@router.post(
    '/upload',
    summary="Сохраним говно-файл и вернем результат",
    tags=['File'],
    status_code=status.HTTP_201_CREATED,
    response_model=None
)
async def create_upload_file(
        film_service: FileService = Depends(get_file_service)
) -> dict:
    out_file_path = await film_service.get_metrix()

    return {"url": f"/{out_file_path}"}
