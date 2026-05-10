from fastapi import APIRouter
from app.services.crawler import crawler_service

router = APIRouter(prefix="/crawler", tags=["crawler"])

@router.get("/status")
def get_crawler_status():
    return {"status": crawler_service.get_status()}
