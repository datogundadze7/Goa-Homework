// Get elements
const addResultButton = document.getElementById("addResultButton");
const resultsList = document.getElementById("resultsList");
const averageScoreDisplay = document.getElementById("averageScore");

// Array to store results
const scores = [];

// Function to add result
function addResult() {
    // Get input values
    const subject = document.getElementById("subjectInput").value;
    const score = parseInt(document.getElementById("scoreInput").value);

    if (!subject || isNaN(score)) {
        alert("Please enter both a subject and a valid score.");
        return;
    }

    // Add result to the list
    const resultDiv = document.createElement("div");
    resultDiv.classList.add("result");
    resultDiv.innerHTML = `<span class="result-title">${subject}</span><span class="result-score">${score}/100</span>`;
    resultsList.appendChild(resultDiv);

    // Store score and update average
    scores.push(score);
    updateAverageScore();

    // Clear input fields
    document.getElementById("subjectInput").value = "";
    document.getElementById("scoreInput").value = "";
}

// Function to update the average score
function updateAverageScore() {
    const total = scores.reduce((sum, score) => sum + score, 0);
    const average = scores.length > 0 ? (total / scores.length).toFixed(2) : 0;
    averageScoreDisplay.textContent = average;
}

// Add event listener to button
addResultButton.addEventListener("click", addResult);
