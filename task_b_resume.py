import openai

def generate_resume(experience_text):
    """Generates a formatted resume from a paragraph."""
    prompt = f"Convert the following experience into a professional resume format:\n\n{experience_text}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.5,
        max_tokens=400
    )
    return response.choices[0].text.strip()