from data_generator import generate_workforce_data
from ai_validator import DataValidator
import json

def main():
    print("--- Starting AI Data Validation Pipeline ---\n")

    # Step 1: Generate Mock Data (Simulating an ETL extraction)
    generate_workforce_data()

    # Step 2: Initialize Validator
    validator = DataValidator('raw_data.csv')

    # Step 3: Run Standard Data Engineering Checks
    validator.run_standard_checks()

    # Step 4: Run AI/ML Checks
    validator.run_ai_anomaly_detection()

    # Step 5: Finalize
    validator.save_clean_data()
    
    # Print Final Report
    print("\n--- Final Validation Report ---")
    print(json.dumps(validator.get_report(), indent=4))
    print("\nPipeline Finished Successfully.")

if __name__ == "__main__":
    main()