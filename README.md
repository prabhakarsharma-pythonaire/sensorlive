SensorLive
SensorLive is a machine learning project for predicting potential brake failures using sensor data, aiming to reduce the high costs of traditional inspections. This project focuses on minimizing Type II errors (false negatives) since an undetected brake failure poses serious safety risks.

Project Overview
Brake failures are critical concerns, and timely, accurate detection is essential. SensorLive leverages sensor data to analyze and predict brake component issues, enhancing reliability and cost-effectiveness.

Pipeline Structure
The project pipeline is organized as follows:

1. Data Ingestion
Source: Data is fetched from MongoDB.
Extraction: Relevant fields are queried and extracted.
Cleaning: Initial cleaning addresses missing values and redundant data.
2. Data Validation
Schema Validation: Ensures correct data structure.
Range & Value Checks: Verifies sensor values fall within expected ranges.
Duplicate & Anomaly Detection: Identifies duplicates and anomalies to ensure data integrity.
3. Data Transformation
Feature Engineering: Generates meaningful features to enhance model performance.
Scaling & Encoding: Prepares data by scaling numerical values and encoding categorical data.
Data Splitting: Divides data into training and testing sets for model evaluation.
4. Model Training
Model Selection: Chooses an appropriate model to predict brake status.
Hyperparameter Tuning: Optimizes parameters to reduce Type II errors.
Cross-Validation: Assesses model robustness through multiple validations.
5. Deployment (Pusher)
Model Serialization: Saves the trained model for deployment.
Deployment Setup: Configures endpoints for real-time prediction.
Monitoring: Includes logging and monitoring to track model accuracy and detect data drift.
Installation
To install dependencies and run the project locally:

bash
Copy code
git clone https://github.com/prabhakarsharma-pythonaire/sensorlive.git
cd sensorlive
pip install -r requirements.txt
Usage
Load sensor data into the designated directory.
Run the main script for model training or inference:
bash
Copy code
python main.py
Deployment
See deployment_steps.txt for full deployment instructions, including production setup and monitoring.

License
This project is licensed under the MIT License.