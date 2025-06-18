import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from joblib import dump

# Load dataset
df = pd.read_csv("penguin_species_dataset.csv")
df.dropna(inplace=True)

# Encode categorical features
df_encoded = pd.get_dummies(df, columns=["Sex", "Island"], drop_first=True)

# Features and target
X = df_encoded.drop(columns=["Species"])
y = df_encoded["Species"]

# Label encoding
label_map = {name: idx for idx, name in enumerate(y.unique())}
reverse_map = {v: k for k, v in label_map.items()}
y_encoded = y.map(label_map)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train models
lr = LogisticRegression(max_iter=1000, multi_class='multinomial')
knn = KNeighborsClassifier(n_neighbors=7)
lr.fit(X_train_scaled, y_train)
knn.fit(X_train_scaled, y_train)

# Evaluate
lr_preds = lr.predict(X_test_scaled)
knn_preds = knn.predict(X_test_scaled)
lr_acc = accuracy_score(y_test, lr_preds)
knn_acc = accuracy_score(y_test, knn_preds)

# Output results
print(f"📊 Logistic Regression Accuracy: {lr_acc:.2f}")
print(f"📊 KNN Accuracy: {knn_acc:.2f}")

# Save models and artifacts
os.makedirs("models", exist_ok=True)
dump(lr, "models/lr_model.pkl")
dump(knn, "models/knn_model.pkl")
dump(scaler, "models/scaler.pkl")
dump(label_map, "models/label_map.pkl")
dump(reverse_map, "models/reverse_label_map.pkl")
dump(list(X.columns), "models/feature_names.pkl")

# Save metrics to file
with open("models/metrics.txt", "w") as f:
    f.write(f"Logistic Regression Accuracy: {lr_acc:.2f}\n")
    f.write(f"KNN Accuracy: {knn_acc:.2f}\n")

print("✅ Models and scaler saved to /models")

# Confusion matrix plot
def save_confusion(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    labels = list(reverse_map.values())
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Oranges", xticklabels=labels, yticklabels=labels)
    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    os.makedirs("cfm", exist_ok=True)
    plt.savefig(f"cfm/{model_name.lower().replace(' ', '_')}_cm.png")
    plt.close()

save_confusion(y_test, lr_preds, "Logistic Regression")
save_confusion(y_test, knn_preds, "KNN")

# Sample predictions
sample = X_test.copy()
sample["Actual"] = y_test.map(reverse_map)
sample["LR_Predicted"] = [reverse_map[i] for i in lr_preds]
sample["KNN_Predicted"] = [reverse_map[i] for i in knn_preds]
print("\n🧪 Sample Predictions:")
print(sample.head())

# Show label map
print("\n🔤 Species Label Order for Streamlit:")
for label, index in label_map.items():
    print(f"{index}: {label}")
# Save label map to file
with open("models/label_map.txt", "w") as f:
    for label, index in label_map.items():
        f.write(f"{index}: {label}\n")