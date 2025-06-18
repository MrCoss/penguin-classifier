🐧 PenguinID

An elegant and educational Streamlit app to predict **penguin species** and **sex** using ML models.

---

## 🚀 Version

**Current Version:** `v1.0`
📅 **Last Updated:** June 2025
🛠️ **Major Update:** Now supports **18 species** with location-based prediction

---

## 🌍 Supported Penguin Species (18)

This version can classify these species:

1. Adelie
2. Chinstrap
3. Gentoo
4. Emperor
5. King
6. Rockhopper
7. Macaroni
8. Galápagos
9. Erect-crested
10. Fiordland
11. Humboldt
12. Magellanic
13. Royal
14. Snares
15. Yellow-eyed
16. African
17. Little Blue
18. Northern Rockhopper

🔬 These predictions are based on **body measurements**, **island habitat**, and **sex**.

---

## 🎯 Features

✅ Predict the **species** of a penguin
✅ Predict the **sex** (Male or Female)
✅ **Choose algorithm**: Logistic Regression or KNN
✅ Fully **scaled and preprocessed** inputs
✅ Supports **11+ island habitats**
✅ Clean, professional **UI with modern theme**
✅ Updated **theming and sidebar layout**
✅ Removed balloons for a smooth experience
✅ Automatically handles feature mapping

---

## 🧠 How It Works

> Just move the sliders and dropdowns to describe your penguin, then hit "Predict".

The app uses:

* Scikit-learn models (`.pkl` format)
* Feature engineering and one-hot encoding
* Scaler for normalization
* Reverse label maps for clean output

---

## 🧪 Input Features

| Feature          | Description                  |
| ---------------- | ---------------------------- |
| Bill Length (mm) | Length of the beak           |
| Bill Depth (mm)  | Depth/thickness of the beak  |
| Flipper Length   | Wing span (mm)               |
| Body Mass        | Weight in grams              |
| Sex              | Male / Female                |
| Island           | Origin habitat (11+ options) |

---

## 🛠 Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas & NumPy
* PIL (logo handling)
* Joblib (model loading)

---

## 📦 How to Run Locally

```bash
git clone https://github.com/MrCoss/penguin-classifier.git
cd penguin-classifier

pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 UI Preview

> ![Demo Coming Soon]()

🎨 Theme: Soft Blue & White with neat typography
🧭 Sidebar navigation for model selection
📐 Intuitive sliders for input

---

## ✍️ Author

**👨‍🏫 Costas Pinto**
🎓 MCA Student & Educator
📧 costaspinto21@gmail.com

---

## 📌 License

🆓 This project is free to use for **educational** purposes only.
