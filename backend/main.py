from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cameroon Real Estate App")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Welcome to Cameroon Real Estate App"}

@app.get("/properties")
def get_properties():
    return [
        {"id": 1, "type": "land", "location": "Yaoundé", "price": 50000},
        {"id": 2, "type": "apartment", "location": "Douala", "price": 75000}
    ]
