# Predictive Modeling of Customer Churn in the Moroccan Banking Sector

This project aims to build an end-to-end Machine Learning solution to predict customer churn (attrition) in the banking sector.

## 📌 Project Overview

Originally inspired by a real-world use case in a major Moroccan bank, the objective is to identify customers at risk of leaving by detecting early behavioral signals and providing actionable insights for marketing and retention teams.<br>
<img width="864" height="540" alt="Capture1" src="https://github.com/user-attachments/assets/5119b951-c6a0-4a2b-ace6-694745655a11" />


The solution provides:
- Individual churn scoring
- Interactive web application
- Business dashboards for decision-making

> Note: For confidentiality reasons, real banking data and internal information cannot be shared.



## 🛠️ Tech Stack

- **Language:** Python 3.11  
- **Machine Learning:** Random Forest, XGBoost, Logistic Regression and CatBoost (final model)  
- **Data Processing:** Pandas, NumPy  
- **Deployment:** Streamlit (web application)  
- **Visualization:** Power BI, Matplotlib, Seaborn  
- **Environment:** Visual Studio Code + Python Virtual Environment (venv)


## 🚀 Methodology (CRISP-DM)
The project follows the CRISP-DM methodology:<br>
<img width="936" height="472" alt="image" src="https://github.com/user-attachments/assets/c42b22d9-232f-4513-a8c7-3fdd1937d2c8" />


### 1. Business Understanding  
Defining churn in the context of retail banking and identifying key business indicators of customer disengagement.

### 2. Data Preparation 
🔹Merging and aggregating multiple datasets:
- Customer profile data
- Digital activity  
- Transaction history  
- Financial balances
- Average outstanding <br>
<img width="626" height="297" alt="Capture2" src="https://github.com/user-attachments/assets/4f9c257c-80e5-4dea-b3a3-8166bf1adf19" />


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
<br>
<img width="686" height="402" alt="image" src="https://github.com/user-attachments/assets/7e8f3186-3cd7-4a58-81b8-3568abb07f84" />
<img width="842" height="562" alt="image" src="https://github.com/user-attachments/assets/8930c3e2-b985-4656-bdef-eacd34acbc80" />
<img width="817" height="475" alt="image" src="https://github.com/user-attachments/assets/b18d1eb0-16d6-45f6-83b4-3cc627024353" />


## 📊 Key Results

- The model successfully identifies nearly **70% of at-risk customers**.  
- Feature importance analysis highlights strong behavioral drivers, such as:
  - Declining average balances  
  - Reduced transaction activity  
<br>
<img width="771" height="379" alt="image" src="https://github.com/user-attachments/assets/4b7d1631-b3be-47b3-b548-4a43353f8b65" />


## 🖥️ Solution Features

### 1. Streamlit Web Application
🔹An interactive interface allowing business users to:
- Select the churn definition rule  
- Upload new customer data  
- Generate real-time churn scores  
- Visualize individual risk profiles  
<br>
<img width="800" height="568" alt="Capture7" src="https://github.com/user-attachments/assets/3bb6e76d-20c1-4616-9102-e951208c34f0" />
<img width="783" height="523" alt="Capture6" src="https://github.com/user-attachments/assets/17d99a41-937c-4de6-829e-5376bcbb4c1d" />


### 2. Power BI Dashboards

**Macro View**
- Global churn trends  
- High-risk customer segments
<br>
<img width="926" height="494" alt="Capture4" src="https://github.com/user-attachments/assets/88c336f2-9a69-4372-a061-fee70aa54438" />


**Individual View**
- Detailed profiles of at-risk customers  
- Support for targeted retention actions  
<br>
<img width="899" height="508" alt="Capture5" src="https://github.com/user-attachments/assets/feb2f37f-2f1d-45d7-a298-b34f84f33fcd" />


## ⚙️ Development Environment

🔹The project was developed using:
- **Visual Studio Code**
- **Python virtual environment (venv)**

### Setup Instructions

git clone https://github.com/BMSalem/Customer_churn.git<br>
cd Customer_churn<br>
python -m venv venv

🔹Activate environment:
- Windows : venv\Scripts\activate
- Linux / Mac : source venv/bin/activate


## 🧠 Model Training

Due to computational constraints, model training was performed on Kaggle notebooks.

🔹The training pipeline includes:
- Train / test split
- Feature encoding
- Hyperparameter tuning
- Model persistence

Training scripts are available in: /notebooks/training/

## ▶️ Run the Application
streamlit run app.py

## 📁 Project Structure

Customer_churn/<br>
│<br>
├── Notebooks/                # training,Merging & preprocessing notebooks<br>
    │<br>
    ├── Merging/      <br>        
    ├── Preprocessing/    <br>    
    ├── training/        <br>     
├── streamlit/                # Streamlit application & Saved CatBoost model (.pkl)<br>
├── screens/                  # Power BI Screenshots<br>
└── README.md


## 📈 Key Learnings

- Real-world churn problems rarely have clean labels
- Feature engineering is critical for performance
- Handling imbalanced datasets is essential
- End-to-end ML pipelines are more valuable than isolated models
- Business interpretability is as important as accuracy


## 🔮 Limitations & Future Work

🔹Anonymized data
🔹No real-time data ingestion
🔹Future improvements:
   - SHAP explainability
   - Model monitoring
   - API integration
   - Automated retraining pipeline


## 👤 Author
Mohamed Salem BERRADA 
- Junior Data & Machine Learning Engineer
