# 💓 Heart Disease Prediction using Machine Learning

A user-friendly application that predicts the likelihood of heart disease based on clinical parameters using a trained machine learning model. Built with Python, Tkinter, and scikit-learn.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 Overview
Cardiovascular disease is one of the leading causes of death globally. Early prediction can save lives.  
This project builds a predictive model using the **Random Forest Classifier** to determine if a patient is likely to have heart disease based on input features like age, cholesterol level, max heart rate, etc.

---

## 📊 Dataset
- **Source**: [UCI Heart Disease Dataset](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
- **Features**:
  - `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`
- **Target**: `target` (1 = disease, 0 = no disease)

---

## 🚀 Features
- Intuitive **Tkinter GUI** for easy user input
- Real-time heart disease prediction
- Clean UI with a light pink theme for formal presentation
- Error handling for invalid input
- Model trained using Random Forest for accuracy

---

## 🧰 Tech Stack
- **Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, tkinter
- **Model**: RandomForestClassifier

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction

   Install dependencies:
pip install -r requirements.txt

Run the app:
python heart_disease_ui.py

▶️ Usage
Enter the required clinical values into the GUI.

Click on Predict.

The app will display whether the patient is likely to have heart disease.
Author
Shraddha Gopare
Computer Science and Engineering
Passionate about Data Science & Health Tech ❤️

