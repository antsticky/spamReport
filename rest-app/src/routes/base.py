from fastapi import APIRouter, Depends


from src.schemes.meta import ApiMetadata


router = APIRouter()


@router.get("/ping")
def endpoint_ping():
    return {"message": "ping"}


@router.get("/health")
def endpoint_health(app_meta: ApiMetadata = Depends(ApiMetadata)):
    return {
        "status": "ok",
        "uptime": app_meta.human_readable_uptime,
    }
