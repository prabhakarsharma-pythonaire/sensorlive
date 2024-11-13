SensorLive: Predicting Brake Failures Using Sensor Data
SensorLive is an end-to-end machine learning project aimed at predicting brake system failures by analyzing sensor data. By identifying patterns in sensor readings, SensorLive helps reduce the need for costly physical inspections and provides early alerts for potential issues. This is crucial in mitigating Type II errors (false negatives), where undetected brake failures could lead to severe safety risks.

Project Overview
The SensorLive pipeline is designed to address the complex, multi-step process of ingesting, validating, transforming, and modeling sensor data. With continuous integration and deployment configurations, the project emphasizes reproducibility, scalability, and monitoring in production.

Folder Structure
The repository includes the following key folders and files:

.github/workflows: Contains CI/CD configurations, including continuous integration for code checks.
config/: Holds configuration files for the ingestion pipeline, data validation, transformation, and model parameters.
experiments/: Experimental notebooks and code scripts used for exploratory data analysis and model prototyping.
flowcharts/: Diagrams that outline the pipeline architecture and data flow.
saved_models/: Stores trained models serialized for deployment.
sensor/: Core code for data ingestion, validation, transformation, and model training.
Dockerfile: Configuration file for containerizing the project.
requirements.txt: Specifies the dependencies needed to run the project.
main.py: Entry point for executing the pipeline.
Pipeline Stages
1. Data Ingestion
Source Extraction: Connects to MongoDB to fetch real-time sensor data.
Data Loading: Data is extracted, loaded, and stored for preprocessing.
Raw Data Handling: Missing values are handled, and irrelevant fields are dropped for a cleaner dataset.
2. Data Validation
Schema Matching: Ensures each sensor reading matches the expected schema in terms of data types and field names.
Range Validation: Checks for valid ranges in sensor readings to catch anomalies early.
Duplicate Removal: Identifies and removes duplicates that could skew analysis.
Anomaly Detection: Flags unexpected or inconsistent data, using thresholds set in config/validation_config.yaml.
3. Data Transformation
Feature Engineering: Generates additional features from sensor readings to improve predictive power.
Scaling and Encoding: Numerical sensor values are standardized; categorical data (if any) is encoded.
Splitting: The data is split into training and testing subsets, balancing the distribution of faulty and non-faulty cases.
4. Model Training
Model Selection: Algorithms suitable for time-series or sensor data are tested (e.g., Random Forest, SVM, XGBoost).
Hyperparameter Optimization: Uses grid search or random search for tuning, prioritizing recall to reduce Type II errors.
Cross-Validation: Model is validated across multiple folds to ensure robustness against data variability.
Model Persistence: The trained model is serialized and stored in saved_models/ for deployment.
5. Deployment (Model Pusher)
Containerization: Docker is used to containerize the model, ensuring consistency across environments.
Deployment Pipeline: Automated deployment scripts in .github/workflows push the model to production once validated.
Monitoring & Logging: Implements logging for tracking model inputs and outputs to detect data drift over time.
6. Continuous Integration and Deployment
Testing: Unit and integration tests ensure each pipeline component works as expected.
CI/CD: Using GitHub Actions, the pipeline automatically tests and deploys new changes.
Alerts: Configurations include automated alerts for pipeline failures or anomalies.
Setup and Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/prabhakarsharma-pythonaire/sensorlive.git
cd sensorlive
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Environment Variables: Set up necessary environment variables for MongoDB connection and other configurations as specified in config/env_config.yaml.

Run the Pipeline: Execute the pipeline from main.py to start ingestion, validation, transformation, and model training:

bash
Copy code
python main.py
Deployment Guide
Follow the instructions in deployment_steps.txt to deploy the containerized model to a cloud service or local server.

Testing
Run the following to test each component of the pipeline:

bash
Copy code
pytest tests/
Project Contributions
Contributors: Contributions to the project are welcome. Please open an issue for bug reports or feature requests.
Pull Requests: For major changes, please discuss them in an issue first.
License
This project is licensed under the MIT License.