import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv('heart.csv')

# Splitting data into features and target
X = data.drop('target', axis=1)
y = data['target']

# Splitting into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

def predict_heart_disease():
    try:
        values = [float(entry.get()) for entry in entries]
        input_data = np.array(values).reshape(1, -1)
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            messagebox.showinfo('Result', 'The patient is likely to have heart disease. 💔')
        else:
            messagebox.showinfo('Result', 'The patient is unlikely to have heart disease. 💚')
    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter valid numbers.')

# Create UI window
root = tk.Tk()
root.title('Heart Disease Prediction')
root.geometry('550x750')
root.configure(bg='#b3b3ff')  # Light pink background

# Heading label
heading = tk.Label(root, text="HEART DISEASE PREDICTION", bg='#b3b3ff', fg='#333', font=('Arial', 24, 'bold'))
heading.grid(row=0, columnspan=2, pady=20)

# Labels and entry fields
labels = [
    'Age', 'Sex (1=Male, 0=Female)', 'Chest Pain Type (0=Typical angina, 1=Atypical angina, 2=Non-anginal pain, 3=Asymptomatic)', 
    'Resting BP (Normal range: 90–120 mm Hg)', 'Cholesterol (Normal value: < 200 mg/dL, High cholesterol: ≥ 240 mg/dL)', 'Fasting Blood Sugar (0=Normal, 1=Diabetic)', 
    'Resting ECG (0=Normal, 1=ST-T wave abnormality, 2=LVH Thickened heart wall)', 'Max Heart Rate', 
    'Exercise Induced Angina (0=NO, 1=YES)', 'Oldpeak (0.0 → No depression (normal), ≥ 1.0 → Potential heart disease)', 
    'Slope (0=Upsloping, 1=Flat, 2=Downsloping)', 
    'Number of Major Vessels(0-3) (0 = no blockages, 3 = severe blockages)', 'Thal (1 =Normal, 2 =Fixed defect, 3 =Reversible defect)'
]

entries = []

# Improved styling with light pink background
for i, label in enumerate(labels):
    tk.Label(root, text=label, bg='#b3b3ff', fg='#333', font=('Arial', 10, 'bold')).grid(row=i + 1, column=0, padx=10, pady=5, sticky='w')
    
    entry = tk.Entry(root, font=('Arial', 10))
    entry.grid(row=i + 1, column=1, padx=10, pady=5)
    entries.append(entry)

# Predict button styling
predict_btn = tk.Button(root, text='Predict', command=predict_heart_disease, bg='#6666ff', fg='white', font=('Arial', 12, 'bold'), padx=20, pady=10)
predict_btn.grid(row=len(labels) + 1, columnspan=2, pady=20)

# Run the UI loop
root.mainloop()
