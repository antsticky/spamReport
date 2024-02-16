import os

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.factory import APIConfig
from src.schemes.meta import ApiMetadata


from src.routes.base import router as base_router
from src.routes.reports import router as reports_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://localhost:{os.getenv('REACT_APP_PORT_OUT')}"],
    allow_credentials=True,
    allow_methods=["GET", "PUT"],
    allow_headers=["*"],
)

app_config = APIConfig.from_envvar()


app_meta = ApiMetadata()


app.include_router(base_router, tags=["base"], dependencies=[Depends(lambda: app_meta)])
app.include_router(reports_router, prefix="/reports", tags=["reports"])


def start():
    uvicorn.run(
        "src.server:app",
        host=app_config.host,
        port=app_config.port,
        reload=app_config.is_reload,
    )


if __name__ == "__main__":
    start()
