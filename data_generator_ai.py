import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

def generate_workforce_data(num_records=1000):
    """
    Generates synthetic workforce data with intentional anomalies 
    to test the AI validation logic.
    """
    data = []
    departments = ['Engineering', 'Sales', 'HR', 'Finance', 'Marketing']
    
    print(f"Generating {num_records} records...")

    for _ in range(num_records):
        record = {
            'EmployeeID': fake.uuid4(),
            'Name': fake.name(),
            'Department': random.choice(departments),
            # Normal distribution for salary (Mean: 80k, Std: 20k)
            'Salary': max(30000, int(np.random.normal(80000, 20000))),
            # Normal distribution for hours (Mean: 40, Std: 5)
            'WeeklyHours': max(0, int(np.random.normal(40, 5))),
            'RiskScore': round(random.uniform(0, 10), 2)
        }
        data.append(record)
    
    df = pd.DataFrame(data)

    # --- INJECT INTENTIONAL ERRORS (For the AI to catch) ---
    
    # 1. Null Values (Data Quality Issue)
    df.loc[0:20, 'Department'] = None 
    
    # 2. Duplicates (Data Integrity Issue)
    df = pd.concat([df, df.iloc[0:10]], ignore_index=True)
    
    # 3. Anomalies/Outliers (The "AI" part will catch these)
    # Someone earning 1 Million (Anomaly)
    df.loc[50, 'Salary'] = 1000000 
    # Someone working 160 hours a week (Impossible/Anomaly)
    df.loc[51, 'WeeklyHours'] = 160 
    # Negative Salary (Data Entry Error)
    df.loc[52, 'Salary'] = -5000

    print("Data Generation Complete. Saving to raw_data.csv")
    df.to_csv('raw_data.csv', index=False)
    return df

if __name__ == "__main__":
    generate_workforce_data()