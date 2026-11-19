# Introduce the App
st.title("Machine Learning Streamlit App")

st.write( "This app allows you to upload your own CSV dataset or use the" \
         " provided Breast Cancer Wisconsin dataset to train a Decision Tree Classifier. "\
         " You can select a target variable with two categories, adjust the model's hyperparameters,"\
         " and see how well the model performs on the testing data. To get started, use the left sidebar" \
         " to upload a dataset, select your target variable, and adjust the hyperparameters.")

# code for machine learning streamlit app

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# Upload dataset
st.sidebar.header("1. Upload Data (Classification Model)")
user_uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Load dataset
if user_uploaded_file is not None:
    df = pd.read_csv(user_uploaded_file)
else:
    st.sidebar.info("No file uploaded. Using the breast cancer dataset.")
    df = pd.read_csv("MLStreamlitApp/breastcancer.csv")
    
### CLEAN DATA

# Remove empty columns
df = df.dropna(axis=1, how="all")

# Remove rows with missing values
df = df.dropna()

# Remove ID column if present
if "id" in df.columns:
    df = df.drop(columns=["id"])

# Check for empty dataset
if df.empty:
    st.error("There is no data left after removing missing values.")
    st.stop()


### DISPLAY DATA

# Display first five rows
st.subheader("Dataset Preview")
st.dataframe(df.head())


### SELECT TARGET
# Select target variable
st.sidebar.header("2. Select Target")
target = st.sidebar.selectbox("Choose target column", df.columns)

# Define features (X) and target (y)
X = df.drop(columns=[target])
y = df[target]

# Preview features and target
st.subheader("Selected Target")
st.write("Target variable:", target)
st.write(y.head())

# Check if target is suitable for classification (two target categories)
if y.nunique() != 2:
    st.error("This app only supports binary classification. Please select a target with exactly two categories.")
    st.stop()

# Convert target categories to 0 and 1
categories = sorted(y.dropna().unique())
y = y.map({categories[0]: 0, categories[1]: 1})

# Encode categorical predictors
X = pd.get_dummies(X, drop_first=True)

# Preview features
st.subheader("Predictor Variables")
st.dataframe(X.head())




### NOW SPLIT THE DATA INTO TRAIN AND TEST
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

# Select hyperparameters
st.sidebar.header("3. Model Hyperparameters")

max_depth = st.sidebar.slider("Maximum Tree Depth", 1, 20, 4)
min_samples_split = st.sidebar.slider("Minimum Samples to Split", 2, 20, 2)

# Initialize and train tree classification model
model = DecisionTreeClassifier(random_state=42, max_depth=max_depth, min_samples_split=min_samples_split)

model.fit(X_train, y_train)



# findings
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Predict on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Model performance
st.subheader("Model Performance")

st.write("Accuracy:", round(accuracy, 2))
st.write("The model correctly classified", round(accuracy * 100, 1), "% of the" \
" observations in the testing dataset.")

st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))

# ROC and AUC
y_probs = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = roc_auc_score(y_test, y_probs)
st.write("AUC:", round(roc_auc, 2))
st.write("The model's AUC is", round(roc_auc, 2), ". This measures how well the" \
" model distinguishes between the two categories. An AUC closer to 1 indicates better performance," \
" while an AUC of 0.5 indicates performance similar to random guessing.")


# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label="AUC = " + str(round(roc_auc, 2)))
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()

st.pyplot(plt.gcf())
plt.close()

# Explain model performance
st.subheader("Understanding the Results")

st.write("The model's accuracy is", round(accuracy * 100, 1),
         "%. This means the model correctly predicted",
         round(accuracy * 100, 1),
         "% of the observations in the testing dataset.")

st.write("Precision tells us what proportion of the observations predicted to be in a certain class actually belonged to that class. The precision for each class is shown in the classification report above.")
st.write("Recall tells us what proportion of the observations that actually belonged to a certain class were correctly identified by the model. Recall is also called sensitivity for the positive class.")
st.write("The F1-score combines precision and recall into one measure. A higher F1-score indicates a better balance between the two. The F1-score for each class is shown in the classification report above.")

st.write("The model's AUC is", round(roc_auc, 2),
         ". AUC is the area under the ROC curve and measures how well the model distinguishes between the two classes. An AUC closer to 1 indicates better performance.")

# Explain hyperparameters
st.subheader("Understanding the Hyperparameters")

st.write("The maximum tree depth is currently set to", max_depth,
         ". This controls how deep the decision tree can grow. A higher value allows for a more complex tree, but can lead to overfitting.")

st.write("The minimum samples to split is currently set to", min_samples_split,
         ". This controls the minimum number of observations needed at a node for the tree to split. A higher value generally results in a simpler tree.")