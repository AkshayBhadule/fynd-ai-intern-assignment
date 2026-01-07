# Fynd AI Intern – Take Home Assessment

This repository contains the completed solution for the **Fynd AI Intern Take Home Assessment**, covering both **Task 1 (Prompt Engineering & Evaluation)** and **Task 2 (End-to-End Review Processing System)**.

---

## 📌 Task 1: Rating Prediction using Prompt Engineering

### Objective

Evaluate how different prompt designs influence an LLM’s ability to predict star ratings (1–5) from customer review text.

### Files

```
task1/
├── task1_rating_prediction.ipynb
└── yelp_reviews.csv
```

### Description

* A real-world review dataset (`yelp_reviews.csv`) is used as ground truth.
* ~200 samples are selected for efficient experimentation.
* Three prompt versions (V1, V2, V3) are designed.
* Each prompt asks the LLM to predict a star rating and return **JSON-only output**.
* Prompt performance is compared and observations are documented in the notebook.

> Note: The dataset is used **only for evaluation**, not for model training or fine-tuning.

---

## 📌 Task 2: AI-Powered Review Management System

### Objective

Build an end-to-end system that accepts user reviews, processes them using an AI service, stores structured outputs, and provides an admin dashboard for monitoring.

### Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite
* **Frontend:** HTML, CSS, JavaScript (served via FastAPI)
* **AI Integration:** Gemini API (with graceful fallback handling)

### Folder Structure

```
task2/backend/
├── main.py
├── data.db
├── templates/
│   ├── user.html
│   └── admin.html
└── static/
    ├── script.js
    └── style.css
```

### Features

* User-facing page to submit rating and review
* Backend API to process and store reviews
* AI-generated **summary, action, and response** (with fallback if AI is unavailable)
* Admin dashboard displaying all reviews
* Auto-refreshing admin view (every 5 seconds)

---

## 🚀 How to Run Task 2 Locally

From the `task2/backend/` directory:

```bash
uvicorn main:app --reload
```

### Access URLs

* **User UI:** [http://127.0.0.1:8000/user](http://127.0.0.1:8000/user)
* **Admin Dashboard:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
* **API Docs (Swagger):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ⚠️ AI Fallback Handling

If the AI service is unavailable or returns an error:

* The review is still stored in the database.
* A default response is returned to the user.
* This ensures system stability and data integrity.

---

## ✅ Status

* Task 1: Completed
* Task 2: Completed
* Deployment & Report: Not required as per instructions

---

## 👤 Author

Akshay Bhadule

---

This project demonstrates prompt engineering, API design, error handling, and full-stack integration in a clean and maintainable structure.
