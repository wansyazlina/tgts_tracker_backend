from fastapi import FastAPI
from schemas.customer import Customer
from schemas.dashboard import Dashboard
from schemas.alerts import Alert
from schemas.ui_config import UIConfig
import crud

app = FastAPI(
    title="TGTS Tracker API",
    version="1.0"
)

@app.post("/customer")
async def create_customer(data: Customer):
    await crud.upsert_customer(data.dict())
    return {"status": "Customer saved"}

@app.post("/dashboard")
async def create_dashboard(data: Dashboard):
    await crud.upsert_dashboard(data.dict())
    return {"status": "Dashboard saved"}

@app.post("/alert")
async def create_alert(data: Alert):
    await crud.upsert_alert(data.dict())
    return {"status": "Alert saved"}

@app.post("/ui")
async def create_ui(data: UIConfig):
    await crud.upsert_ui(data.dict())
    return {"status": "UI config saved"}

@app.get("/profile/{accountNumber}")
async def profile(accountNumber: str):
    data = await crud.get_merged_profile(accountNumber)
    return data
