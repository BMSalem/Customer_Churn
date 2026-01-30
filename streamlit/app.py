import streamlit as st 
import pandas as pd 
from catboost import CatBoostClassifier 
import joblib
from io import BytesIO 
import base64
import os

st.set_page_config(page_title="Churn Score", layout="centered") 
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

#set_background("r.jpg")  # 🔁 Adapt the path to your image file

#=== Page Configuration ===
 
st.title("📊 Customer Churn Prediction")

#=== Model selection ===
model_options = {
    "Catboost v1 (Rule 1)": "D:/Lab_DL/venv_berrada/Attrition/streamlit/catboost_model_score1.pkl",
    "Catboost v2 (Rule 2)": "D:/Lab_DL/venv_berrada/Attrition/streamlit/catboost_model_score2.pkl"
}
selected_model_name = st.selectbox("🎯 Choose your prediction model :",
                                   options=list(model_options.keys()))

selected_model_path = model_options[selected_model_name]
 
#=== Model loading ===
 
@st.cache_resource 
def load_model(model_path): 
    try:
        model = joblib.load(model_path)  # Set correct path and return model.
        st.success(f"✅ Model '{selected_model_name}' loaded successfully !") 
        return model
    except FileNotFoundError:
        st.error(f"❌ Error : Model file not found at location : {model_path}. Verify the path.")
        return None
    except Exception as e:
        st.error(f"❌ Error during model loading '{selected_model_name}' : {e}")
        return None

model = load_model(selected_model_path)
 
#=== Features ===
 
cat_features = [ 'Niveau_Service_Regroupe', 'Type Personne', 'catégorie_âge', 'Ligne Métier_x', 'Statut' ]  # Adapter selon ton jeu de données

# Validation Function
def validate_dataset(df, model, cat_features):
    expected_cols = model.feature_names_
    issues = []

    # Missing columns
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        issues.append(f"🟥 Missing columns : {missing_cols}")

    # Incorrect data types for categorical columns
    for col in cat_features:
        if col in df.columns and not pd.api.types.is_string_dtype(df[col]):
            issues.append(f"🟧 The feature '{col}' is not of string type")

    return issues

#=== Uploadload file ===
 
file = st.file_uploader("📂 Load Excel file excluding the target variable", type=["xlsx"])
 
if file:
    df_raw = pd.read_excel(file)
    df_raw = df_raw.loc[:, ~df_raw.columns.str.contains('^Unnamed')]
    st.write("✅ File loaded successfully. Dimensions :", df_raw.shape)

        # Verification button
    if st.button("🔍 Verify File"):
        issues = validate_dataset(df_raw, model, cat_features)
        if issues:
            for issue in issues:
                st.warning(issue)
        else:
            st.success("✅ The file is valid for prediction.")

    # Prediction button
    if st.button("🚀 Run Prediction"):
        try:
            # Preparation
            expected_cols = model.feature_names_
            df = df_raw.copy()

            id_client = df["ID client"] if "ID client" in df.columns else None

            df_model = df[expected_cols].copy() # Reorganise

            for col in cat_features:
                if col in df_model.columns:
                    df_model[col] = df_model[col].astype(str)

            df_model = df_model.fillna(0)

            # Prediction
            y_proba = model.predict_proba(df_model)[:, 1]
            y_pred = model.predict(df_model)

            # Results
            df_result = df_raw.copy()
            df_result["Attrition_Prob"] = y_proba * 100
            df_result["Attrition_Predite"] = y_pred

            if id_client is not None and "ID client" not in df_result.columns:
                df_result.insert(0, "ID client", id_client)

            st.session_state.df_result = df_result
            st.success("✅ Prediction completed successfully.")
        except Exception as e:
            st.error(f"Error during prediction : {e}")

    if "df_result" in st.session_state:
        df_result = st.session_state.df_result
        st.subheader("Preview of Results")
        st.dataframe(df_result.head())

        total_clients = len(df_result)
        at_risk_clients = df_result["Attrition_Predite"].sum()
        attrition_rate = (at_risk_clients / total_clients)*100 if total_clients > 0 else 0

        col_metrics1, col_metrics2 = st.columns(2)

        with col_metrics1 :
            st.metric(label="Total At-Risk Customers", value=int(at_risk_clients))
        
        with col_metrics2 :
            st.metric(label="Global Attrition Rate", value=f"{attrition_rate:.2f}%")

        def convert_df(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Résultats')
            output.seek(0)
            # Convert DataFrame to bytes for download
            return output
        
        col1, col2 = st.columns([1,1])

        with col1:
            st.download_button(
                label="📂 Export results as Excel",
                data=convert_df(df_result).getvalue(),
                key="download_excel",
                file_name="Attrition_Scoring_Result.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        with col2:
            #st.markdown("---")
            #st.header("📎 Ouvrir le fichier Power BI localement")

            pbix_path = "C:/Users/Mohamed Salem/Desktop/template2.pbix"  # 🔁 Adapt the path

            if st.button("📊 Open Power BI Dashboard"):
                try:
                    os.startfile(pbix_path)
                    st.success("✅ The Power BI file has been opened in the default application.")
                except Exception as e:
                    st.error(f"Error opening the file : {e}")