from fastapi import FastAPI
from app.api.v1 import vendedor_router, venta_router, comision_router, regla_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(vendedor_router, prefix="/api/v1")
app.include_router(venta_router, prefix="/api/v1")
app.include_router(comision_router, prefix="/api/v1")
app.include_router(regla_router.router, prefix="/api/v1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
