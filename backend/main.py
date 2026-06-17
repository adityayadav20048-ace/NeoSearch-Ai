from fastapi import FastAPI
from routes.ai_routes import router
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI()

# ✅ Add CORS (IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes
app.include_router(router)

# ✅ Home route (optional but useful)
@app.get("/")
def home():
    return {"message": "AI Search API running"}
