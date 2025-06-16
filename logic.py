# logic.py

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

def load_data():
    df = sns.load_dataset("penguins")
    df.dropna(inplace=True)
    X = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]
    y_species = df["species"]
    y_sex = df["sex"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y_species, y_sex, scaler

def train_models():
    X_scaled, y_species, y_sex, scaler = load_data()
    
    # Train for species
    X_train_s, _, y_train_s, _ = train_test_split(X_scaled, y_species, test_size=0.2, random_state=42)
    species_model = LogisticRegression(max_iter=1000)
    species_model.fit(X_train_s, y_train_s)

    # Train for sex
    X_train_x, _, y_train_x, _ = train_test_split(X_scaled, y_sex, test_size=0.2, random_state=42)
    sex_model = LogisticRegression(max_iter=1000)
    sex_model.fit(X_train_x, y_train_x)

    return species_model, sex_model, scaler
