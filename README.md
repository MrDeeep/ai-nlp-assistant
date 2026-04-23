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
    User((User))
    UI[Frontend UI<br/>HTML / CSS]
    JS[Client Logic<br/>script.js]
    Flask[Backend Server<br/>Flask app.py]
    
    ModA[task_a_eda.py]
    ModB[task_b_resume.py]
    ModC[task_c_interview.py]
    ModD[task_d_summary.py]
    
    OpenAI{OpenAI API<br/>gpt-3.5-turbo}

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

    style User fill:#f9f,stroke:#333,stroke-width:2px
    style OpenAI fill:#00d2ff,stroke:#333,stroke-width:2px,color:#000
````
---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)  
- **Backend:** Python 3, Flask  
- **AI Integration:** OpenAI Python SDK (`openai==0.28`)  

---

## 🚀 Installation & Local Setup

If you want to run this project on your own machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/MrDeep/ai-nlp-assistant.git
cd ai-nlp-assistant
```
```bash
cd ai-nlp-assistant
```

---

### 2. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install flask openai==0.28
```

---

### 3. Add Your API Key

Create a file named `GPT-3-SECRET-KEY.json` in the root directory.

Add your OpenAI API key in the following format:

```json
{
  "OPEN_API_KEY": "sk-your-actual-api-key-here"
}
```

> ⚠️ This file is included in `.gitignore` to prevent leaking your secret key.

---

### 4. Run the Server

Start the Flask backend:

```bash
python main.py
```

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the issues page on GitHub.

---

## 📝 License

This project is open-source and available under the **MIT License**.
