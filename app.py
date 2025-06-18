import streamlit as st
import numpy as np
from joblib import load
from PIL import Image

# Load models and extras
lr_model = load("models/lr_model.pkl")
knn_model = load("models/knn_model.pkl")
scaler = load("models/scaler.pkl")
label_map = load("models/label_map.pkl")
feature_names = load("models/feature_names.pkl")
reverse_label_map = {v: k for k, v in label_map.items()}

# App config (no page title or icon)
st.set_page_config(layout="centered")

# Custom CSS for theming
st.markdown("""
    <style>
        body {
            background-color: #f4f4f9;
            color: #333333;
        }
        .main {
            background-color: #f4f4f9;
        }
        h1, h2, h3 {
            color: #1a4f84;
        }
        .stButton>button {
            background-color: #1a4f84;
            color: white;
            border-radius: 8px;
            padding: 10px 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #1463a3;
        }
        .stSelectbox>div>div {
            background-color: white;
            color: #1a4f84;
        }
        .stSlider>div {
            color: #1a4f84;
        }
        section[data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 2px solid #1a4f84;
        }
        section[data-testid="stSidebar"] .stRadio,
        section[data-testid="stSidebar"] label {
            color: #1a4f84 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Logo (Large)
try:
    logo = Image.open("logo.png")
    st.image(logo, width=300)
except:
    st.write("🐧 **Penguin Identifier**")

st.markdown("### Predict the species of a penguin from its measurements and habitat info.")

# Sidebar
st.sidebar.title("Choose Model")
model_choice = st.sidebar.radio("Algorithm", ["Logistic Regression", "KNN"])

# Main inputs
st.header("Physical Features")
bill_length = st.slider("Bill Length (mm)", 30.0, 70.0, 45.0)
bill_depth = st.slider("Bill Depth (mm)", 13.0, 25.0, 17.0)
flipper_length = st.slider("Flipper Length (mm)", 150.0, 250.0, 200.0)
body_mass = st.slider("Body Mass (g)", 2000.0, 7000.0, 4000.0)

st.header("Biological & Location Info")
sex = st.selectbox("Sex", ["Male", "Female"])
island = st.selectbox("Island", [
    'Biscoe', 'Dream', 'Torgersen', 'Antarctica', 'South Georgia',
    'Macquarie', 'Kerguelen', 'Falkland Islands', 'Galápagos', 
    'Marion', 'Tristan da Cunha'
])

# Format input
input_df = {
    "Bill_Length_mm": bill_length,
    "Bill_Depth_mm": bill_depth,
    "Flipper_Length_mm": flipper_length,
    "Body_Mass_g": body_mass,
    "Sex_Male": 1 if sex == "Male" else 0,
}
for isl in ["Antarctica", "Biscoe", "Dream", "Falkland Islands", "Galápagos", 
            "Kerguelen", "Macquarie", "Marion", "South Georgia", 
            "Torgersen", "Tristan da Cunha"]:
    input_df[f"Island_{isl}"] = 1 if island == isl else 0

input_data = np.array([[input_df.get(feat, 0) for feat in feature_names]])
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Penguin Species"):
    prediction = lr_model.predict(input_scaled)[0] if model_choice == "Logistic Regression" else knn_model.predict(input_scaled)[0]
    species = reverse_label_map[prediction]
    st.success(f"**Predicted Species:** {species}")

# Footer
st.markdown("---")
st.caption("Version 1.0 | Built by Costas Pinto | Educational Use Only")
