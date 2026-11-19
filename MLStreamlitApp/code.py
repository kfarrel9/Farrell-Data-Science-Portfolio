# code for machine learning streamlit app

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# Introduce the App and explain hwo the user can use the app
st.title("Decision Tree Explorer")

st.write( "This app allows you to upload your own CSV dataset or use the" \
         " provided Breast Cancer Wisconsin dataset to train a Decision Tree Classifier. "\
         " You can select a target variable with two categories, adjust the model's hyperparameters,"\
         " and see how well the model performs on the testing data. To get started, use the left sidebar" \
         " to upload a dataset, select your target variable, and adjust the hyperparameters.")


### UPLOAD DATA

# add a sidebar where the user can uplaod a CSV file
st.sidebar.header("1. Upload Data (Classification Model)")
user_uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# if the user uplaods a file, read that dataset
# if not, use the breast cancer dataset alreafdy included in project
if user_uploaded_file is not None:
    df = pd.read_csv(user_uploaded_file)
else:
    st.sidebar.info("No file uploaded. Using the breast cancer dataset.")
    df = pd.read_csv("MLStreamlitApp/breastcancer.csv")
    
### CLEAN DATA

# Remove empty columns
df = df.dropna(axis=1, how="all")

# Remove rows with missing values
# this ensures there are no missing observations when trauining the model
df = df.dropna()

# Remove ID column if present
# the id, seen in breast cancer data, just identifies an observation and is not useful for predicting the target
if "id" in df.columns:
    df = df.drop(columns=["id"])

# Check for empty dataset
# if all data is removed, display an error
if df.empty:
    st.error("There is no data left after removing missing values.")
    st.stop()


### DISPLAY DATA

# Display first five rows
# seperate sections of the app with a divider
st.divider()
st.subheader("Dataset Preview")
st.dataframe(df.head())


### SELECT TARGET
# allow the user to choose which column they want to predict
# the dropdown includes the columns for the cleaned dataset
st.sidebar.header("2. Select Target")
target = st.sidebar.selectbox("Choose target column", df.columns)

# Define features (X) and target (y)
# x contains all predictor variables (everything excpet target)
# y contains the target var that we are trying to predict
X = df.drop(columns=[target])
y = df[target]


# display the target var selected by the user
st.divider()
st.subheader("Selected Target")
st.write("Target variable:", target)
st.write(y.head())

# this app only uses binary classification
# check that the selected target inly has exaclty two dif categoies
# if not, the model will not run and a dif target is needed to be selected
if y.nunique() != 2:
    st.error("This app only supports binary classification. Please select a target with exactly two categories.")
    st.stop()

# Convert target categories to 0 and 1
# for example, yes/no, benign/malignant become 0 or 1
categories = sorted(y.dropna().unique())
y = y.map({categories[0]: 0, categories[1]: 1})

# convert categorical predictor variables into numerical variables
# drop_first= True removes one dummy column from each categorical variable
# numerical values are needed to train the decision tree
X = pd.get_dummies(X, drop_first=True)

# Preview features
# shows the first five rows of the predictor variables after preparation
st.divider()
st.subheader("Predictor Variables")
st.dataframe(X.head())



### NOW SPLIT THE DATA INTO TRAIN AND TEST
from sklearn.model_selection import train_test_split

# split data set into 80% training and 20% testing data
# training is used to fit the model
# testing is used to evaluate the model on the observations it has not trained on
# random state makes the random split reproducible (get the same value when you adjust hyperparamters)
# makes it less confusing for the user
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


### Train the decision TREE MODEL
from sklearn.tree import DecisionTreeClassifier

# add sliders to the slidebar for the user to adjust two hyperparameters
st.sidebar.header("3. Model Hyperparameters")

# max_depth contols how dee the decision tree can grow
# default val is 4
max_depth = st.sidebar.slider("Maximum Tree Depth", 1, 20, 4)

# min_samples_split controls how many observations a node needs before splitting
# default is two
min_samples_split = st.sidebar.slider("Minimum Samples to Split", 2, 20, 2)

# Initialize and train tree classification model
model = DecisionTreeClassifier(random_state=42, max_depth=max_depth, min_samples_split=min_samples_split)

# fir the decision tree using the training data
# whenever the user changes a slider, the app reruns and fits a new model
model.fit(X_train, y_train)


### EVALUATE MODEL

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# use the fotted model to make predictions on the testing data
y_pred = model.predict(X_test)

# Compare the predictions with the actual target values in the testing data
# accuracy gives the proportion of predictions that were correct
accuracy = accuracy_score(y_test, y_pred)

# display the model's performance
st.divider()
st.subheader("Model Performance")

# show the accuracy and explainn what it means in context of the dataset
st.write("Accuracy:", round(accuracy, 2))
st.write("The model correctly classified", round(accuracy * 100, 1), "% of the" \
" observations in the testing dataset.")

# show the classification report
# includes precision, recall, f1-score, and support
st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))


#### ROC and AUC
# calc the predicted prob of being in class 1
# rhese probs are used to cal the ROC curve and AUC
y_probs = model.predict_proba(X_test)[:, 1]


# calc false pos rate and true pos rate and area under ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = roc_auc_score(y_test, y_probs)

# display the AUC and explain what the values mean
st.write("AUC:", round(roc_auc, 2))
st.write("The model's AUC is", round(roc_auc, 2), ". This measures how well the" \
" model distinguishes between the two categories. An AUC closer to 1 indicates better performance," \
" while an AUC of 0.5 indicates performance similar to random guessing.")

# display the accuracy and AUC in metric boxes
# these make the results easier to see
st.metric("Accuracy", str(round(accuracy * 100, 1)) + "%")
st.metric("AUC", round(roc_auc, 2))

# Plot ROC curve
plt.figure(figsize=(8, 6))
# plot true pos against false pos rate

# include the AUC value in the legend
plt.plot(fpr, tpr, label="AUC = " + str(round(roc_auc, 2)))

# add a diagonal reference line for random guessing
plt.plot([0, 1], [0, 1], linestyle='--')

# label the axes and graph
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()

st.pyplot(plt.gcf())
plt.close()

### EXPLAIN MODEL PERFORMANCE

st.divider()
st.subheader("Understanding the Results")

# interpret the current accuracy value
# multiply by 100 to convert it into a percentage
st.write("The model's accuracy is", round(accuracy * 100, 1),
         "%. This means the model correctly predicted",
         round(accuracy * 100, 1),
         "% of the observations in the testing dataset.")

st.write("Precision tells us what proportion of the observations predicted to be in a certain class actually belonged to that class. The precision for each class is shown in the classification report above.")
st.write("Recall tells us what proportion of the observations that actually belonged to a certain class were correctly identified by the model. Recall is also called sensitivity for the positive class.")
st.write("The F1-score combines precision and recall into one measure. A higher F1-score indicates a better balance between the two. The F1-score for each class is shown in the classification report above.")

st.write("The model's AUC is", round(roc_auc, 2),
         ". AUC is the area under the ROC curve and measures how well the model distinguishes between the two classes. An AUC closer to 1 indicates better performance.")

### EXPLAIN HYPERPARAMETERS

# explain what each slider controls
# also display the values currently selected by the user

st.divider()
st.subheader("Understanding the Hyperparameters")

st.write("The maximum tree depth is currently set to", max_depth,
         ". This controls how deep the decision tree can grow. A higher value allows for a more complex tree, but can lead to overfitting.")

st.write("The minimum samples to split is currently set to", min_samples_split,
         ". This controls the minimum number of observations needed at a node for the tree to split. A higher value generally results in a simpler tree.")