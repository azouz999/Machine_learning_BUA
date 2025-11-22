
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = load_breast_cancer()
X = data.data
y = data.target

print("Samples:", X.shape[0])
print("Features:", X.shape[1])
print("Target Classes:", list(data.target_names))


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



pipeline = Pipeline([
    ('scaler', StandardScaler()),         
    ('classifier', LogisticRegression())   
])


pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Malignant', 'Benign']))


model = pipeline.named_steps['classifier']

coefficients = model.coef_[0] 

feature_names = data.feature_names

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': coefficients,
    'Absolute Coefficient': np.abs(coefficients)
})

importance_df = importance_df.sort_values(by='Absolute Coefficient', ascending=False)

print("\nTop 10 Most Important Features:")
print(importance_df.head(10))



plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'][:10], importance_df['Absolute Coefficient'][:10])
plt.xlabel('Absolute Coefficient Value')
plt.ylabel('Feature')
plt.title('Top 10 Feature Importances in Logistic Regression (Breast Cancer)')
plt.gca().invert_yaxis()  
plt.show()
