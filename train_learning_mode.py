# import pandas as pd
# import os
# from glob import glob

# # Define the directory containing CSV files
# data_dir = "data/KT1"
# output_file = "data/processed_data.csv"

# # Get a list of all CSV files in the directory
# csv_files = glob(os.path.join(data_dir, "*.csv"))

# # List to store processed DataFrames
# processed_data = []

# # Process each CSV file
# for file in csv_files:
#     try:
#         # Load dataset
#         data = pd.read_csv(file)
        
#         # Feature engineering
#         data['is_fast_learner'] = data['elapsed_time'] < data['elapsed_time'].median()
#         data['topic_difficulty'] = data.groupby('question_id')['correct'].transform('mean')
        
#         # Append to list
#         processed_data.append(data)
    
#     except Exception as e:
#         print(f"Error processing {file}: {e}")

# # Combine all processed data
# final_data = pd.concat(processed_data, ignore_index=True)

# # Save to CSV
# final_data.to_csv(output_file, index=False)

# print(f"Processed {len(csv_files)} files and saved to {output_file}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load processed data
data_path = 'data/processed_data.csv'
data = pd.read_csv(data_path)

# Check for missing values
if data.isnull().sum().any():
    print("Warning: Missing values detected. Filling with median values.")
    data.fillna(data.median(), inplace=True)

# Features and target
X = data[['elapsed_time', 'topic_difficulty']]
y = data['is_fast_learner']

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)  # Set n_estimators for stability
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Model Performance:")
print(classification_report(y_test, y_pred))

# Save model
model_path = 'learning_mode_model.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
