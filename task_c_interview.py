import openai

def generate_interview_questions(language, topic):
    """Generates interview questions for a specific language and topic."""
    prompt = f"Generate a set of 5 technical interview questions in {language} focusing on {topic}."
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=250
    )
    return response.choices[0].text.strip()