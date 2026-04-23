# 🤖 AI NLP Assistant Web App

A modular, full-stack web application that leverages OpenAI's GPT-3.5 API to automate daily text-based tasks. Built with Python, Flask, and Vanilla JavaScript, this tool acts as a versatile AI assistant right in your browser.

![App Screenshot](https://github.com/MrDeeep/ai-nlp-assistant/blob/main/NLP-project.png)

---

## ✨ Features

This application is split into four dedicated AI modules:

1. **📊 Exploratory Data Analysis (EDA) Generator:** Input a dataset name, and the AI writes the exact Pandas, Matplotlib, and Seaborn Python code needed to analyze it.
2. **📄 Resume Builder:** Paste a casual paragraph about your work experience, and the AI converts it into a polished, professional resume bullet list.
3. **🎯 Interview Prep:** Input a technical topic or job role, and the AI generates 5 highly targeted technical interview questions.
4. **📝 Meeting Summarizer:** Paste a raw, messy transcript of meeting notes, and the AI condenses it into a clear, concise summary paragraph.

---

## 🧠 System Architecture & Data Flow

Below is the flowchart explaining how data moves from the user's browser, through the Flask backend, to OpenAI, and back.

```mermaid
graph TD
    %% Define Nodes
    User((User))
    UI[Frontend UI<br/>HTML / CSS]
    JS[Client Logic<br/>script.js]
    Flask[Backend Server<br/>Flask app.py]
    
    %% Python Modules
    ModA[task_a_eda.py]
    ModB[task_b_resume.py]
    ModC[task_c_interview.py]
    ModD[task_d_summary.py]
    
    %% External API
    OpenAI{OpenAI API<br/>gpt-3.5-turbo}

    %% Flow Details
    User -- "Selects task & types input" --> UI
    UI -- "Clicks Generate" --> JS
    JS -- "POST /api/generate" --> Flask
    
    Flask -- "Routes task: eda" --> ModA
    Flask -- "Routes task: resume" --> ModB
    Flask -- "Routes task: interview" --> ModC
    Flask -- "Routes task: summary" --> ModD
    
    ModA -- "Constructs Prompt" --> OpenAI
    ModB -- "Constructs Prompt" --> OpenAI
    ModC -- "Constructs Prompt" --> OpenAI
    ModD -- "Constructs Prompt" --> OpenAI
    
    OpenAI -- "Returns AI Text" --> Flask
    Flask -- "Sends JSON Response" --> JS
    JS -- "Updates Output Textarea" --> UI
    UI -- "Reads Result" --> User

    %% Styling
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style OpenAI fill:#00d2ff,stroke:#333,stroke-width:2px,color:#000
