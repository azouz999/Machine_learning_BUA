# from sklearn.datasets import load_breast_cancer

# data = load_breast_cancer()
# X, y = data.data, data.target

# print("Samples:", X.shape[0])
# print("Features:", X.shape[1])
# print("Target classes:", list(data.target_names))  
# print("Feature names:", list(data.feature_names))








# from sklearn.datasets import load_breast_cancer
# import pandas as pd

# # Load dataset
# data = load_breast_cancer()

# # Create DataFrame with features
# df = pd.DataFrame(data.data, columns=data.feature_names)

# # Add target column (0 = malignant, 1 = benign)
# df['target'] = data.target

# # Display the first 5 rows
# print(df.head())








# # Import necessary libraries
# from sklearn.datasets import load_breast_cancer
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, accuracy_score
# import pandas as pd

# # Load the dataset
# data = load_breast_cancer()
# X = data.data  # Features
# y = data.target  # Target (0 = malignant, 1 = benign)
# print(data)

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Create and train logistic regression model
# model = LogisticRegression(random_state=42)
# model.fit(X_train, y_train)

# # Make predictions
# y_pred = model.predict(X_test)
# print(model.predict_proba(X_test[:5]))


# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# cm = confusion_matrix(y_test, y_pred)

# print(f"Accuracy: {accuracy:.4f}") 
# print("Confusion Matrix:")
# print(cm)





# from sklearn.metrics import classification_report

# # Calculate evaluation metrics
# tn, fp, fn, tp = cm.ravel()

# precision = tp / (tp + fp)
# recall = tp / (tp + fn)
# f1 = 2 * (precision * recall) / (precision + recall)

# print(f"Precision: {precision:.4f}")
# print(f"Recall: {recall:.4f}")
# print(f"F1-Score: {f1:.4f}")

# # Using sklearn's built-in function
# print("\nDetailed Classification Report:")
# print(classification_report(y_test, y_pred, target_names=['Malignant', 'Benign']))







# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, accuracy_score
# import pandas as pd
# # Load iris dataset
# iris = load_iris()
# X_iris = iris.data
# y_iris = iris.target

# # Split the data
# X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
#     X_iris, y_iris, test_size=0.3, random_state=42
# )

# # Create multi-class logistic regression model
# # multi_class='multinomial' enables Softmax for multi-class classification
# model_iris = LogisticRegression(multi_class='multinomial', random_state=42)
# model_iris.fit(X_train_iris, y_train_iris)

# # Predictions
# y_pred_iris = model_iris.predict(X_test_iris)

# # Evaluate
# accuracy_iris = accuracy_score(y_test_iris, y_pred_iris)
# cm_iris = confusion_matrix(y_test_iris, y_pred_iris)

# print(f"Iris Dataset Accuracy: {accuracy_iris:.4f}")
# print("Iris Confusion Matrix:")
# print(cm_iris)
# print(f"Class names: {iris.target_names}")





# from sklearn.preprocessing import StandardScaler
# import numpy as np

# # Create sample data with different scales
# np.random.seed(42)
# X_uneven = np.column_stack([
#     np.random.normal(100, 10, 100),  # Large scale (mean=100)
#     np.random.normal(0, 1, 100)      # Small scale (mean=0)
# ])
# y_uneven = (X_uneven[:, 0] + X_uneven[:, 1] > 100).astype(int)

# # Split data
# X_train_u, X_test_u, y_train_u, y_test_u = train_test_split(
#     X_uneven, y_uneven, test_size=0.3, random_state=42
# )

# # Model without scaling
# model_no_scale = LogisticRegression(random_state=42)
# model_no_scale.fit(X_train_u, y_train_u)
# accuracy_no_scale = accuracy_score(y_test_u, model_no_scale.predict(X_test_u))

# # Model with scaling
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train_u)
# X_test_scaled = scaler.transform(X_test_u)

# model_scaled = LogisticRegression(random_state=42)
# model_scaled.fit(X_train_scaled, y_train_u)
# accuracy_scaled = accuracy_score(y_test_u, model_scaled.predict(X_test_scaled))

# print(f"Accuracy without scaling: {accuracy_no_scale:.4f}")
# print(f"Accuracy with scaling: {accuracy_scaled:.4f}")
# print(f"Improvement: {accuracy_scaled - accuracy_no_scale:.4f}")
