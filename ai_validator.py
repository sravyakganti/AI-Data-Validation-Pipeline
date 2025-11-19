import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class DataValidator:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)
        self.report = {"Total_Records": 0, "Missing_Values": 0, "Duplicates": 0, "AI_Detected_Anomalies": 0}

    def run_standard_checks(self):
        """Performs standard SQL-style checks (Nulls, Duplicates)"""
        self.report["Total_Records"] = len(self.df)
        
        # Check for Missing Values
        missing_count = self.df.isnull().sum().sum()
        self.report["Missing_Values"] = int(missing_count)
        
        # Check for Duplicates
        duplicate_count = self.df.duplicated().sum()
        self.report["Duplicates"] = int(duplicate_count)
        
        print(f"Standard Checks Completed: {missing_count} missing, {duplicate_count} duplicates.")

    def run_ai_anomaly_detection(self):
        """
        Uses Unsupervised Machine Learning (Isolation Forest) 
        to detect data outliers that rule-based checks might miss.
        """
        print("Running AI Anomaly Detection...")
        
        # Select numerical features for the AI model
        features = ['Salary', 'WeeklyHours', 'RiskScore']
        
        # Handle missing values before passing to ML model (Simple imputation)
        data_for_model = self.df[features].fillna(self.df[features].mean())
        
        # Scale data (Normalization)
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data_for_model)
        
        # Initialize Isolation Forest (The "AI" Brain)
        # contamination=0.02 means we expect roughly 2% of data to be anomalies
        iso_forest = IsolationForest(contamination=0.02, random_state=42)
        
        # Predict: -1 is an anomaly, 1 is normal
        self.df['Anomaly_Score'] = iso_forest.fit_predict(scaled_data)
        
        # Filter only the anomalies
        anomalies = self.df[self.df['Anomaly_Score'] == -1]
        self.report["AI_Detected_Anomalies"] = len(anomalies)
        
        print(f"AI Logic detected {len(anomalies)} anomalous records.")
        
        # Save specific anomalies to a separate file for review
        if not anomalies.empty:
            anomalies.to_csv('flagged_anomalies.csv', index=False)
            print("Anomalies saved to 'flagged_anomalies.csv'")

    def save_clean_data(self):
        """Removes duplicates and saves the cleaned file"""
        clean_df = self.df.drop_duplicates()
        clean_df.to_csv('clean_workforce_data.csv', index=False)

    def get_report(self):
        return self.report