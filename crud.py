from models import customers, dashboards, alerts, ui_configs

async def upsert_customer(data):
    await customers.update_one(
        {"_id": data["accountNumber"]},
        {"$set": data},
        upsert=True
    )

async def upsert_dashboard(data):
    await dashboards.update_one(
        {"_id": data["accountNumber"]},
        {"$set": data},
        upsert=True
    )

async def upsert_alert(data):
    await alerts.update_one(
        {"_id": data["accountNumber"]},
        {"$set": data},
        upsert=True
    )

async def upsert_ui(data):
    await ui_configs.update_one(
        {"_id": data["accountNumber"]},
        {"$set": data},
        upsert=True
    )

async def get_merged_profile(account):
    cust = await customers.find_one({"_id": account}) or {}
    dash = await dashboards.find_one({"_id": account}) or {}
    alert = await alerts.find_one({"_id": account}) or {}
    ui = await ui_configs.find_one({"_id": account}) or {}

    return {
        "customer": cust,
        "dashboard": dash,
        "alerts": alert,
        "ui_config": ui
    }
