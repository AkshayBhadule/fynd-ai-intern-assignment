import os
import sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# ---------------------------
# Gemini Client (Server-side only)
# ---------------------------
from google.genai import Client

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = None
if GEMINI_API_KEY:
    client = Client(api_key=GEMINI_API_KEY)

# ---------------------------
# FastAPI App
# ---------------------------
app = FastAPI(title="AI Review Management System")

# ---------------------------
# Database (SQLite)
# ---------------------------
db = sqlite3.connect("data.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INTEGER,
    review TEXT,
    ai_summary TEXT,
    ai_action TEXT,
    ai_response TEXT
)
""")
db.commit()

# ---------------------------
# Request Schema
# ---------------------------
class ReviewRequest(BaseModel):
    rating: int
    review: str

# ---------------------------
# Static Files
# ---------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ---------------------------
# User Page
# ---------------------------
@app.get("/", response_class=HTMLResponse)
def user_page():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

# ---------------------------
# Admin Page
# ---------------------------
@app.get("/admin", response_class=HTMLResponse)
def admin_page():
    with open("templates/admin.html", "r", encoding="utf-8") as f:
        return f.read()

# ---------------------------
# Submit Review API
# ---------------------------
@app.post("/submit-review")
def submit_review(data: ReviewRequest):
    if not data.review.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Review cannot be empty"}
        )

    # Default fallback values
    ai_summary = "AI service unavailable"
    ai_action = "No action generated"
    ai_response = "AI service unavailable. Review stored for later processing."

    # Try AI call
    if client:
        try:
            prompt = f"""
You are a customer feedback assistant.

Given the following review, return STRICT JSON only with keys:
summary, action, response

Review:
{data.review}
"""

            result = client.models.generate_content(
                model="models/gemini-1.5-pro",
                contents=prompt
            )

            text = result.text.strip()

            # Very simple safe parsing (assignment-level)
            ai_summary = text
            ai_action = text
            ai_response = text

        except Exception as e:
            print("🔥 GEMINI ERROR:", str(e))

    # Store in DB
    cur.execute(
        "INSERT INTO reviews (rating, review, ai_summary, ai_action, ai_response) VALUES (?, ?, ?, ?, ?)",
        (data.rating, data.review, ai_summary, ai_action, ai_response)
    )
    db.commit()

    return {
        "message": "success",
        "ai_response": ai_response
    }

# ---------------------------
# Admin API
# ---------------------------
@app.get("/admin/reviews")
def get_reviews():
    cur.execute("""
        SELECT rating, review, ai_summary, ai_action, ai_response
        FROM reviews
        ORDER BY id DESC
    """)
    return cur.fetchall()
