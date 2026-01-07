import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()

# ---------------- DB ----------------
db = sqlite3.connect("data.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    rating INTEGER,
    review TEXT,
    summary TEXT,
    action TEXT,
    response TEXT
)
""")
db.commit()

# ---------------- MODELS ----------------
class Review(BaseModel):
    rating: int
    review: str

# ---------------- API ----------------
@app.post("/submit-review")
def submit_review(data: Review):
    summary = "AI service unavailable. Review stored."
    action = "Manual review needed"
    response = "Thank you for your feedback."

    cur.execute(
        "INSERT INTO reviews VALUES (?, ?, ?, ?, ?)",
        (data.rating, data.review, summary, action, response)
    )
    db.commit()

    return {
        "message": "success",
        "ai_response": response
    }

@app.get("/admin/reviews")
def get_reviews():
    cur.execute("SELECT * FROM reviews")
    return cur.fetchall()

# ---------------- UI ----------------
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/user", response_class=HTMLResponse)
def user_page():
    return open("templates/user.html", encoding="utf-8").read()

@app.get("/admin", response_class=HTMLResponse)
def admin_page():
    return open("templates/admin.html", encoding="utf-8").read()

# use this to run 
# python -m uvicorn main:app --reload