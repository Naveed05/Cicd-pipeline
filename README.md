📌 Iris Classification – ML Model with CI/CD Pipeline

This project demonstrates a complete Machine Learning workflow including:

✅ Data preprocessing
✅ Feature engineering
✅ Logistic Regression & Random Forest
✅ Model evaluation
✅ Visualizations (Confusion Matrix, Feature Importance)
✅ Automated CI/CD pipeline using GitHub Actions
✅ Artifacts upload (PNG, TXT)
🚀 Project Overview

This project uses the famous Iris dataset to build classification models that predict flower species based on petal and sepal measurements.

Models used:

Logistic Regression

Random Forest Classifier

The CI/CD pipeline ensures that:

Code is tested automatically

Model is trained on every push📂 Folder Structure
├── .github/
│   └── workflows/
│       └── cicd.yml
├── train_model.py
├── test.py
├── iris.csv
├── scores.txt
├── test.txt
├── ConfusionMatrix.png
├── FeatureImportance.png
└── README.md

⚙️ Tech Stack
Component	Technology
Language	Python
ML Libraries	scikit-learn, pandas, numpy
Visualization	matplotlib, seaborn
Automation	GitHub Actions
Deployment	Streamlit (optional)
🧪 Model Performance (Auto-generated)

Results of Logistic Regression & Random Forest are generated automatically and saved as:

scores.txt

ConfusionMatrix.png

FeatureImportance.png

Every GitHub push updates these files using CI/CD.

🔄 CI/CD Pipeline Workflow

The pipeline performs:

Checkout code

Install dependencies

Run tests via test.py

Train model

Generate artifacts

Upload artifacts to GitHub

CI/CD file: .github/workflows/cicd.yml

▶️ How to Run Locally
pip install -r requirements.txt
python train_model.py
python test.py



Updated metrics and visualizations are uploaded as artifacts

