import pandas as pd
from transformers import pipeline

def generate_executive_summary():
    """
    Uses a Generative AI model (LLM) to read the data anomalies 
    and write a natural language summary for executive leadership.
    """
    print("\n--- Starting GenAI Reporting Module ---")
    
    # 1. Load the anomalies detected by the previous step
    try:
        df = pd.read_csv('flagged_anomalies.csv')
    except FileNotFoundError:
        print("No anomalies file found. Run main.py first.")
        return

    if df.empty:
        print("No anomalies to report.")
        return

    # 2. Prepare a prompt for the LLM based on the data
    # We take the first few anomalies to summarize
    high_risk_count = len(df[df['Salary'] > 200000])
    total_issues = len(df)
    
    prompt_context = (
        f"Data Analysis Report: We detected {total_issues} data anomalies. "
        f"There are {high_risk_count} cases of suspicious high salaries. "
        "The Finance team should review these immediately to prevent payroll errors."
    )

    print("Loading Local LLM (DistilGPT-2)... this may take a moment...")
    
    # 3. Initialize the Generator (Free Local LLM from Hugging Face)
    # We use 'text-generation' to simulate writing an email
    generator = pipeline('text-generation', model='distilgpt2')

    # 4. Generate the Summary
    # We ask the AI to expand on the context
    response = generator(
        f"Write a professional risk alert email based on this data: {prompt_context}", 
        max_length=100, 
        num_return_sequences=1,
        truncation=True
    )
    
    generated_text = response[0]['generated_text']

    # 5. Output the Result
    print("\nGenerated Executive Summary (by GenAI):")
    print("-" * 50)
    print(generated_text)
    print("-" * 50)
    
    # Save to text file
    with open("genai_executive_summary.txt", "w") as f:
        f.write(generated_text)
    print("Summary saved to 'genai_executive_summary.txt'")

if __name__ == "__main__":
    generate_executive_summary()