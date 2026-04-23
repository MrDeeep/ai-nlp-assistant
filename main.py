from flask import Flask, render_template, request, jsonify

# Import your existing modules
from config import authenticate
from task_a_eda import generate_eda_code
from task_b_resume import generate_resume
from task_c_interview import generate_interview_questions
from task_d_summary import summarize_meeting

app = Flask(__name__)

# Authenticate once when the server starts
authenticate()

@app.route('/')
def home():
    # Serves the HTML file from the 'templates' folder
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    task = data.get('task')
    user_input = data.get('input_text', '')

    try:
        # Route the request to your existing modules
        if task == "eda":
            # If your generate_eda_code doesn't take arguments, you can pass user_input into it in task_a_eda.py later
            result = generate_eda_code(user_input) 
        elif task == "resume":
            result = generate_resume(user_input)
        elif task == "interview":
            # Defaulting to Python, passing the user's input as the topic
            result = generate_interview_questions("Python", user_input)
        elif task == "summary":
            result = summarize_meeting(user_input)
        else:
            return jsonify({"error": "Invalid task selected."}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)