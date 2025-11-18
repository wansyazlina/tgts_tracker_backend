# TGTS Tracker – MongoDB Backend with -> FastAPI + Motor

This project consists of the backend for the TGTS Tracker shipment-tracking system.  
The system includes :

- CRUD operations for customers, dashboards, alerts, and UI configs  
- Merged profile endpoint (`/profile/:id`)  
- TTL auto-deletion of expired alerts  
- Aggregation pipeline (dashboard labels + alert count)  
- JSON Schema validation for dashboards  
- Indexing for efficient point-reads  
- Logical sharding demonstration  
- Evidence screenshots (Compass + Swagger UI)

Technologies used: **FastAPI (Python)**, **Motor (MongoDB)**, **VS Code**, **Swagger UI**, **MongoDB Compass**.

---

## 🏃🏻‍♀️ Running the Project

### 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the API server

```bash
uvicorn main:app --reload
```

### 4. Access Swagger UI

Open in your browser:

👉 http://127.0.0.1:8000/docs

Use this to run all CRUD operations.

### 📂 Folder Structure

```
tgts_tracker/
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas/
│   ├── alerts.py
│   ├── customer.py
│   ├── dashboard.py
│   └── ui_config.py
└── README.md
```

## 📌 Sample API Calls

### Create Customer

```json
POST /customer
{
  "accountNumber": "AC00001",
  "name": "Harris Lutfi",
  "currency": "MYR"
}
```

### Merged Profile

```json
GET /profile/AC00001
```

### TTL Alert Example

```json
POST /alert
{
  "accountNumber": "TTLTEST1",
  "recipients": ["ops@test.com"],
  "expiresAt": "2025-11-19T01:20:00+08:00"
}
```

### 📊 Aggregation Example

The system includes a pipeline to return dashboard labels + alert count.

### 🔧 Required Index

TTL index for alerts:
```
db.alerts.createIndex({ expiresAt: 1 }, { expireAfterSeconds: 0 })
```

### 🗂 Sharding Demo (Logical)

```
sh.enableSharding("tgts_tracker")
sh.shardCollection("tgts_tracker.customers", { _id: "hashed" })
sh.status()
```

(These are shown for assignment demonstration purposes only)

## 📄 License

This is project is created for the submission for TGTS Tracker project- Code and documentation is written by Wan Syazlina bt. Wan Aasim


