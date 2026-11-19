# Machine Learning Streamlit App

## Project Overview
This project is an interactive Streamlit app that allows users to upload their own CSV file (or use a preloaded dataset) to train a supervised machine learning model. The app uses a Decision Tree Classifier to make predictions for a binary target variable. This means that the target must have only two categories, such as Yes/No or 0/1.

Users can select which column they want to use as the target variable. However, if the selected column does not contain exactly two categories, the app prompts the user to select a different target variable because binary classification is required for this model. Users can also adjust the model's hyperparameters and evaluate its performance using accuracy, precision, recall, F1-score, and AUC. The app then displays an ROC curve to help visualize the model's performance.

This project builds on various supervised machine learning techniques learned in Introduction to Data Science, such as data preprocessing, splitting data into training and testing sets, decision trees, hyperparameter tuning, and model evaluation.

### Streamlit App Access

[View the Live Streamlit App](https://farrell-ml-classifier.streamlit.app/)

### How to Use the App
1. Upload your own CSV dataset in the left panel of the app (If no dataset is uploaded, the provided dataset will be used- Breast Cancer Wisconsin)
2. Select which column in the dataset will serve as the target. The target must contain exactly two categories (If the selected column does not contain exactly two categories, the user will be prompted to select a new column)
3. Adjust the maximum tree depth and minimum samples to split using the sliders on the left panel
4. View the model's accuracy, classification report, AUC, and ROC curve.
5. Adjust the hyperparameters to see how the model's performance changes.

### Data Preparation

This app includes the Breast Cancer Wisconsin dataset from Kaggle as a preloaded dataset; however, users can also upload their own CSV files.

Before training the model, the dataset is processed:
- Columns that are completely empty and rows containing missing values are removed
- Columns named "id" are removed
- The target variable is checked to have only two categories
- The target categories are converted into 0 and 1's
- Uses pd.get_dummies() to encode categorical predictor variables


### Machine Learning Model

A Decision Tree Classifier from scikit-learn is used for this app. The data is split into training data (80%) and testing data (20%) using the train_test_split() command with random_state=42.

#### Hyperparameters
The hyperparameters that the user can adjust are:

- Maximum Tree Depth (max_depth): This parameter controls the max number of levels that the decision tree is able to grow to. A higher value allows the tree to make more splits; however, it may also lead to oversplitting.
- Minimum Samples to Split (min_samples_split): This parameter controls the min number of observations needed in a group before the tree is able to split. The higher the value, the simpler the tree.

Each time one of these parameters are changed, the model is retrained and the results are updated.

### Model Evaluation
The model is evaluated using the testing dataset, which contains 20% of the original data. The app displays several performance metrics to show how well the Decision Tree Classifier predicts the selected target variable using the testing data.

- Accuracy: Accuracy tells us what percentage of the observations in the testing dataset were correctly predicted by the model.
- Precision: Precision tells us what proportion of the observations predicted to be in a certain class actually belonged to that class.
- Recall: Recall tells us what proportion of the observations that actually belonged to a certain class were correctly identified by the model. Recall for the positive class is also called sensitivity.
- F1-Score: The F1-score combines precision and recall into one measure to account for both.
- AUC: AUC measures how well the model can distinguish between the two classes. An AUC closer to 1 indicates better performance.
- ROC Curve: Plots the true positive rate against the false positive rate at different classification thresholds.

### How to Run the App Locally
How to run the app on your own computer:
1. Download or clone this GitHub repository
```bash 
git clone https://github.com/kfarrel9/Farrell-Data-Science-Portfolio.git
```
2. Open the repository in VS Code
```bash
cd Farrell-Data-Science-Portfolio
```
3. Install the required libraries
```bash
pip install -r MLStreamlitApp/requirements.txt
```
4. Run the Streamlit app:
```bash
streamlit run MLStreamlitApp/code.py
```

### Libraries Used
| Library | Version |
|---|---|
| Streamlit | 1.62.0 |
| pandas | 3.0.5 |
| NumPy | 2.5.2 |
| Matplotlib | 3.11.1 |
| scikit-learn | 1.9.1 |


### References
[Breast Cancer Wisconsin Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
[Scikit-learn Decision Tree Documentation](https://scikit-learn.org/stable/modules/tree.html)
[Streamlit Documentation](https://docs.streamlit.io/)