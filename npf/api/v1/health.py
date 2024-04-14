from fastapi import APIRouter

router = APIRouter()


@router.get('/', summary='Проверка работоспособности сервиса')
async def health_status() -> dict:
    return {}
