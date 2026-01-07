// ================= USER =================
function submitReview() {
    const ratingEl = document.getElementById("rating");
    const reviewEl = document.getElementById("review");
    const resultBox = document.getElementById("result");

    if (!ratingEl || !reviewEl || !resultBox) return;

    const rating = ratingEl.value;
    const review = reviewEl.value;

    resultBox.innerHTML = "";

    if (!rating || !review.trim()) {
        resultBox.style.color = "red";
        resultBox.innerText = "Please provide both rating and review.";
        return;
    }

    fetch("/submit-review", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            rating: parseInt(rating),
            review: review
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.message === "success") {
            resultBox.style.color = "green";
            resultBox.innerHTML = `
                <strong>Submission Successful!</strong><br><br>
                <strong>AI Response:</strong><br>
                ${data.ai_response}
            `;
        } else {
            resultBox.style.color = "red";
            resultBox.innerText = data.error || "Something went wrong.";
        }
    })
    .catch(err => {
        resultBox.style.color = "red";
        resultBox.innerText = "Server error. Please try again.";
        console.error(err);
    });
}

// ================= ADMIN =================
function fetchReviews() {
    const body = document.getElementById("reviews-body");
    if (!body) return; // ✅ CRITICAL

    fetch("/admin/reviews")
        .then(res => res.json())
        .then(data => {
            body.innerHTML = "";
            data.forEach(row => {
                const tr = document.createElement("tr");
                row.forEach(col => {
                    const td = document.createElement("td");
                    td.innerText = col;
                    tr.appendChild(td);
                });
                body.appendChild(tr);
            });
        })
        .catch(err => console.error(err));
}

// ✅ Run admin logic ONLY if admin table exists
document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("reviews-body")) {
        fetchReviews();
        setInterval(fetchReviews, 5000);
    }
});
