# app.py

import streamlit as st
import numpy as np
from logic import train_models

# Load models
species_model, sex_model, scaler = train_models()

# App UI
st.set_page_config(page_title="Penguin Classifier", page_icon="🐧")
st.title("🐧 Penguin Classifier")
st.write("Enter penguin body measurements to predict species and sex.")

# Input sliders
bill_length = st.slider("Bill Length (mm)", 30.0, 60.0, 45.0)
bill_depth = st.slider("Bill Depth (mm)", 13.0, 21.0, 17.0)
flipper_length = st.slider("Flipper Length (mm)", 170.0, 230.0, 200.0)
body_mass = st.slider("Body Mass (g)", 2500.0, 6500.0, 4000.0)

if st.button("Predict"):
    input_data = np.array([[bill_length, bill_depth, flipper_length, body_mass]])
    input_scaled = scaler.transform(input_data)

    species = species_model.predict(input_scaled)[0]
    sex = sex_model.predict(input_scaled)[0]

    st.success(f"🧬 Predicted Species: **{species}**")
    st.success(f"🚻 Predicted Sex: **{sex}**")

# Footer
st.markdown("---")
st.markdown("<center><sub> Made by MrCoss🐧/sub></center>", unsafe_allow_html=True)
