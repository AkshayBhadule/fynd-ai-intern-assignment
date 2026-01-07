# Fynd AI Intern – Take Home Assessment

This repository contains my submission for the **Fynd AI Intern Take Home Assessment**, covering both required tasks:

- **Task 1:** Rating Prediction via Prompt Engineering  
- **Task 2:** Two-Dashboard AI Feedback System (Web-Based)

---

## 📌 Task 1: Rating Prediction using Prompt Engineering

### Objective

Evaluate how different prompt designs influence an LLM’s ability to predict **1–5 star ratings** from customer review text using **prompt-only approaches** (no training or fine-tuning).

### Files

task1/
├── task1_rating_prediction.ipynb
└── yelp_reviews.csv


### Description

- A real-world review dataset (`yelp_reviews.csv`) is used as **ground truth**.
- A subset of ~200 reviews is sampled for evaluation efficiency.
- **Three prompt versions (V1, V2, V3)** are designed and tested.
- Each prompt:
  - Predicts a star rating (1–5)
  - Returns **strict JSON-only output**
- Performance comparison includes:
  - Accuracy (Actual vs Predicted)
  - JSON validity rate
  - Reliability and consistency

**Output Format:**
```json
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}

Task 2: AI-Powered Review Management System
Objective

Build a production-style web application with two dashboards that:Accept user reviews Generate AI-based insights Store structured outputs Provide an admin monitoring interface All LLM calls are handled server-side only, as required.

Tech Stack

Backend: FastAPI
Database: SQLite (auto-created at runtime)
Frontend: HTML, CSS, JavaScript (served via FastAPI)
AI Integration: Gemini API (with graceful fallback handling)
Deployment: Render

task2/backend/
├── main.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── admin.html
└── static/
    ├── script.js
    └── style.css

User Dashboard (Public-Facing)

Users can:
Select a star rating (1–5)
Write a short review
Submit the review

On submission:
An AI-generated response is shown to the user
The submission is stored persistently
Clear success / error feedback is provided

Admin Dashboard (Internal-Facing)

The Admin Dashboard displays:
User rating
User review
AI-generated summary
AI-recommended action
AI-generated response

Additional features:
Auto-refresh every 5 seconds
Shared persistent data source with User Dashboard

AI Fallback Handling
If the AI service is unavailable or fails:
    The review is still stored in the database
    A default fallback response is returned
    The system remains stable and functional
This ensures graceful degradation and data integrity.

Deployment (Live)

User Dashboard:
https://fynd-ai-intern-assignment-mszq.onrender.com/

Admin Dashboard:
https://fynd-ai-intern-assignment-mszq.onrender.com/admin

API Documentation (Swagger):
https://fynd-ai-intern-assignment-mszq.onrender.com/docs

Both dashboards:
Are publicly accessible
Persist data across refreshes
Work without local setup

Run Locally
From the task2/backend/ directory:
uvicorn main:app --reload

Access:

User UI: http://127.0.0.1:8000/
Admin UI: http://127.0.0.1:8000/admin
API Docs: http://127.0.0.1:8000/docs

Submission Status
Task 1: Completed
Task 2: Completed
Live Deployment: Completed
All constraints satisfied (no Streamlit / Gradio / notebook apps)

Author
Akshay Bhadule
