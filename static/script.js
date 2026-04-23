document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".task-btn");
    const label = document.getElementById("input-label");
    const inputArea = document.getElementById("user-input");
    const outputArea = document.getElementById("output-result");
    const generateBtn = document.getElementById("generate-btn");
    const loader = document.getElementById("loader");

    let currentTask = "eda";

    // Text instructions for each module
    const taskDetails = {
        "eda": { label: "Enter the dataset name:", placeholder: "e.g., employee_records.csv" },
        "resume": { label: "Paste raw experience details:", placeholder: "e.g., I have worked with Python, Pandas, and Flask..." },
        "interview": { label: "Enter the technical topic:", placeholder: "e.g., Object Oriented Programming, APIs..." },
        "summary": { label: "Paste raw meeting notes:", placeholder: "e.g., Alice: Fix the server. Bob: Done." }
    };

    // Switch between tasks
    buttons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            buttons.forEach(b => b.classList.remove("active"));
            e.target.classList.add("active");

            currentTask = e.target.dataset.task;
            label.textContent = taskDetails[currentTask].label;
            inputArea.placeholder = taskDetails[currentTask].placeholder;
            inputArea.value = "";
            outputArea.value = "";
        });
    });

    // Send data to main.py
    generateBtn.addEventListener("click", async () => {
        const text = inputArea.value.trim();
        if (!text) {
            alert("Please enter some input text!");
            return;
        }

        outputArea.value = "";
        loader.style.display = "block";
        generateBtn.disabled = true;

        try {
            const response = await fetch("/api/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ task: currentTask, input_text: text })
            });

            const data = await response.json();

            if (response.ok) {
                outputArea.value = data.result;
            } else {
                outputArea.value = "Error: " + data.error;
            }
        } catch (error) {
            outputArea.value = "Failed to connect to the backend.";
        } finally {
            loader.style.display = "none";
            generateBtn.disabled = false;
        }
    });
});