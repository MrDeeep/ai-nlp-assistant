import openai

def summarize_meeting(notes):
    """Generates a concise summary from raw meeting notes."""
    prompt = f"Summarize the following meeting notes into a concise paragraph:\n\n{notes}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.3,
        max_tokens=150
    )
    return response.choices[0].text.strip()