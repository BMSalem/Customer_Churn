# Predictive Modeling of Customer Churn in the Moroccan Banking Sector
## 📌 Project Overview
This project aims to build an end-to-end Machine Learning solution to predict customer churn (attrition) in the banking sector.

Originally inspired by a real-world use case in a major Moroccan bank, the objective is to identify customers at risk of leaving by detecting early behavioral signals and providing actionable insights for marketing and retention teams.<br>
<screenshot title>

The solution provides:
- Individual churn scoring
- Interactive web application
- Business dashboards for decision-making

> <b>Note:<\b> For confidentiality reasons, real banking data and internal information cannot be shared.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11  
- **Machine Learning:** Random Forest, XGBoost, Logistic Regression and CatBoost (final model)  
- **Data Processing:** Pandas, NumPy  
- **Deployment:** Streamlit (web application)  
- **Visualization:** Power BI, Matplotlib, Seaborn  
- **Environment:** Visual Studio Code + Python Virtual Environment (venv)

---

## 🚀 Methodology (CRISP-DM)
The project follows the CRISP-DM methodology:
<screen crisp>

### 1. Business Understanding  
Defining churn in the context of retail banking and identifying key business indicators of customer disengagement.

### 2. Data Preparation 
<screen all_dataset>
🔹Merging and aggregating multiple datasets:
- Customer profile data  
- Digital activity  
- Transaction history  
- Financial balances  

All datasets are transformed to obtain **one row per customer**.

### 3. Heuristic Labeling  
🔹Since no explicit churn label was available, a heuristic labeling strategy was implemented using business-inspired rules, mainly based on:
- Progressive decline in average balances  
- Prolonged inactivity  

This simulates real-world scenarios where churn labels are not directly observable.

### 4. Modeling  
🔹Several algorithms were tested using :
- Logistic Regression  
- Random Forest   
- XGBoost  
- CatBoost  

🔹CatBoost was selected for its:
- High performance on imbalanced data  
- Native handling of categorical variables  
- Robustness to missing values  

### 5. Evaluation  
🔹Final model performance:
- **Accuracy:** 86%  
- **ROC-AUC:** 0.93  
- **Recall (churn class):** 0.69  
- **Precision:** 0.79  

[SCREENSHOT: CRISP-DM Workflow / ROC Curve]

---

## 📊 Key Results

- The model successfully identifies nearly **70% of at-risk customers**.  
- Feature importance analysis highlights strong behavioral drivers, such as:
  - Declining average balances  
  - Reduced transaction activity  

[SCREENSHOT: Confusion Matrix / Feature Importance]

---

## 🖥️ Solution Features

### 1. Streamlit Web Application
🔹An interactive interface allowing business users to:
- Select the churn definition rule  
- Upload new customer data  
- Generate real-time churn scores  
- Visualize individual risk profiles  

[SCREENSHOT: Streamlit Application Interface]

---

### 2. Power BI Dashboards

**Macro View**
- Global churn trends  
- High-risk customer segments

[SCREENSHOT: Power BI Macro Dashboard]  

**Individual View**
- Detailed profiles of at-risk customers  
- Support for targeted retention actions  

[SCREENSHOT: Power BI Individual View]

---

## ⚙️ Development Environment

🔹The project was developed using:
- **Visual Studio Code**
- **Python virtual environment (venv)**

### Setup Instructions

git clone https://github.com/BMSalem/Customer_churn.git
cd Customer_churn
python -m venv venv

🔹Activate environment:
- Windows : venv\Scripts\activate
- Linux / Mac : source venv/bin/activate

---

## 🧠 Model Training

Due to computational constraints, model training was performed on Kaggle notebooks.

🔹The training pipeline includes:
- Train / test split
- Feature encoding
- Hyperparameter tuning
- Model persistence

Training scripts are available in: /notebooks/training/

---

## ▶️ Run the Application
streamlit run app.py

---

## 📁 Project Structure

Customer_churn/
│
├── Notebooks/                # training,Merging & preprocessing notebooks
    │
    ├── Merging/              
    ├── Preprocessing/        
    ├── training/             
├── streamlit/                # Streamlit application & Saved CatBoost model (.pkl)
├── screens/                  # Power BI Screenshots
└── README.md

---

## 📈 Key Learnings

- Real-world churn problems rarely have clean labels
- Feature engineering is critical for performance
- Handling imbalanced datasets is essential
- End-to-end ML pipelines are more valuable than isolated models
- Business interpretability is as important as accuracy

---

## 🔮 Limitations & Future Work

🔹No real-time data ingestion
🔹Future improvements:
   - SHAP explainability
   - Model monitoring
   - API integration
   - Automated retraining pipeline

---

## 👤 Author
Mohamed Salem BERRADA 
- Junior Data & Machine Learning Engineer
