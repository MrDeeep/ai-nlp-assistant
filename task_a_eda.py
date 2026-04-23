import openai

def generate_eda_code(dataset_name):
    """Generates Python code for EDA and Visualization based on user input."""
    # Default to 'data.csv' if the user left it blank
    if not dataset_name:
        dataset_name = 'data.csv'
        
    prompt = (
        f"Write Python code using pandas for exploratory data analysis and "
        f"matplotlib/seaborn for data visualization on a dataset named '{dataset_name}'."
    )
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.3,
        max_tokens=300
    )
    return response.choices[0].text.strip()