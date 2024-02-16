from fastapi import APIRouter, Depends


from src.schemes.meta import ApiMetadata


router = APIRouter()


@router.get("/ping")
def endpoint_ping():
    """
    Endpoint to check the health of the service.

    Returns:
        dict: A JSON response containing a "message" key with the value "ping".
    """

    return {"message": "ping"}


@router.get("/health")
def endpoint_health(app_meta: ApiMetadata = Depends(ApiMetadata)):
    """
    Endpoint to check the health and uptime of the service.

    Args:
        app_meta (ApiMetadata, optional): Metadata about the API application. Defaults to using `ApiMetadata` dependency.

    Returns:
        dict: A JSON response containing the status of the service ("status": "ok") and its uptime ("uptime").
    """
    
    return {
        "status": "ok",
        "uptime": app_meta.human_readable_uptime,
    }
