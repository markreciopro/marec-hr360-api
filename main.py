from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
# UNIVERSAL DASHBOARD (MULTI-ORG)
# -----------------------------

@app.get("/dashboard")
def get_dashboard(company: str = Query(default="default")):

    # 🔹 TECH COMPANY
    if company == "tech":
        return {
            "company": "TechCorp",
            "industry": "Technology",
            "workforce": 950,
            "attrition": 10,
            "timeToHire": 22,
            "attritionTrend": [8, 9, 10, 11, 10],
            "headcountTrend": [500, 600, 720, 820, 950],
            "departments": {
                "Engineering": 450,
                "Product": 150,
                "Data": 120,
                "Sales": 150,
                "HR": 80
            }
        }

    # 🔹 HEALTHCARE
    elif company == "healthcare":
        return {
            "company": "City Hospital",
            "industry": "Healthcare",
            "workforce": 1200,
            "attrition": 15,
            "timeToHire": 35,
            "attritionTrend": [12, 14, 15, 16, 15],
            "headcountTrend": [800, 900, 1000, 1100, 1200],
            "departments": {
                "Nursing": 500,
                "Physicians": 200,
                "Admin": 250,
                "Operations": 150,
                "HR": 100
            }
        }

    # 🔹 RETAIL
    elif company == "retail":
        return {
            "company": "RetailCo",
            "industry": "Retail",
            "workforce": 2000,
            "attrition": 25,
            "timeToHire": 18,
            "attritionTrend": [20, 22, 25, 27, 25],
            "headcountTrend": [1500, 1600, 1700, 1850, 2000],
            "departments": {
                "Store Operations": 1200,
                "Warehouse": 300,
                "Logistics": 200,
                "Customer Service": 200,
                "HR": 100
            }
        }

    # 🔹 FINANCE
    elif company == "finance":
        return {
            "company": "FinGroup",
            "industry": "Finance",
            "workforce": 700,
            "attrition": 8,
            "timeToHire": 30,
            "attritionTrend": [7, 8, 9, 8, 8],
            "headcountTrend": [500, 550, 600, 650, 700],
            "departments": {
                "Investment": 200,
                "Risk": 120,
                "Compliance": 100,
                "Operations": 180,
                "HR": 100
            }
        }

    # 🔹 DEFAULT (FALLBACK)
    else:
        return {
            "company": "Default Company",
            "industry": "General",
            "workforce": 842,
            "attrition": 12,
            "timeToHire": 28,
            "attritionTrend": [10, 12, 9, 14, 11],
            "headcountTrend": [400, 500, 620, 710, 842],
            "departments": {
                "HR": 120,
                "IT": 300,
                "Sales": 200,
                "Finance": 222
            }
        }

# -----------------------------
# PHILOSOPHY
# -----------------------------

@app.get("/philosophy")
def get_philosophy():
    return {
        "mission": "Transform HR into strategic workforce intelligence",
        "vision": "AI-powered HR decision making platform",
        "values": [
            "Data-driven",
            "Human-first",
            "Scalable",
            "Predictive insight"
        ]
    }
