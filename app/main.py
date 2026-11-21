from fastapi import FastAPI
from app.routers.pmb import router as pmb_router
from app.routers.krs import router as krs_router

app = FastAPI(title="PMB dan KRS API", version="2.0.0")
app.include_router(pmb_router)
app.include_router(krs_router)

@app.get("/")
def root():
    return {"message": "PMB API aktif"}
