from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# BASIC ROUTES
# -----------------------------

@app.get("/")
def root():
    return {"message": "MAREC HR360 API running"}

@app.get("/ping")
def ping():
    return {"status": "API alive"}

@app.post("/register")
def register():
    return {"status": "register works"}

@app.post("/login")
def login():
    return {"status": "login works"}

@app.post("/upload")
def upload():
    return {"status": "upload works"}

# -----------------------------
# DASHBOARD (MAIN DATA ENDPOINT)
# -----------------------------

@app.get("/dashboard")
def get_dashboard():
    return {
        "workforce": 842,
        "attrition": 12,
        "timeToHire": 28,

        # 📊 Chart Data
        "attritionTrend": [10, 12, 9, 14, 11],
        "headcountTrend": [400, 500, 620, 710, 842],
        "departments": {
            "HR": 120,
            "IT": 300,
            "Sales": 200,
            "Finance": 222
        }
    }
