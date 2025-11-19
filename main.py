from data_generator import generate_workforce_data
from ai_validator import DataValidator
from genai_report import generate_executive_summary # <--- NEW IMPORT
import json

def main():
    print("--- Starting AI Data Validation Pipeline ---\n")

    # Step 1: Generate Mock Data
    generate_workforce_data()

    # Step 2: Initialize Validator
    validator = DataValidator('raw_data.csv')

    # Step 3: Run Standard Checks
    validator.run_standard_checks()

    # Step 4: Run AI Anomaly Detection (Classical ML)
    validator.run_ai_anomaly_detection()

    # Step 5: Save Clean Data
    validator.save_clean_data()
    
    print("\n--- Final Validation Report ---")
    print(json.dumps(validator.get_report(), indent=4))

    # Step 6: Run GenAI Reporting (The New LLM Step)
    generate_executive_summary() # <--- RUN GEN AI
    
    print("\nPipeline Finished Successfully.")

if __name__ == "__main__":
    main()