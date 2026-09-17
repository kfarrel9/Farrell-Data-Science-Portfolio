import pandas as pd            # Library for data manipulation
import seaborn as sns          # Library for statistical plotting
import matplotlib.pyplot as plt  # For creating custom plots
import streamlit as st         # Framework for building interactive web apps

# ================================================================================
#Missing Data & Data Quality Checks
#
# This lecture covers:
# - Data Validation: Checking data types, missing values, and ensuring consistency.
# - Missing Data Handling: Options to drop or impute missing data.
# - Visualization: Using heatmaps and histograms to explore data distribution.
# ================================================================================
st.title("Missing Data & Data Quality Checks")
st.markdown("""
This lecture covers:
- **Data Validation:** Checking data types, missing values, and basic consistency.
- **Missing Data Handling:** Options to drop or impute missing data.
- **Visualization:** Using heatmaps and histograms to understand data distribution.
""")

# ------------------------------------------------------------------------------
# Load the Dataset
# ------------------------------------------------------------------------------
# Read the Titanic dataset from a CSV file.
df = pd.read_csv("titanic.csv")

# ------------------------------------------------------------------------------
# Display Summary Statistics
# ------------------------------------------------------------------------------
# Show key statistical measures like mean, standard deviation, etc.
st.write("**Summary Statistics**")
st.dataframe(df.describe())

# ------------------------------------------------------------------------------
# Check for Missing Values
# ------------------------------------------------------------------------------
# Display the count of missing values for each column.
st.write("**Number of Missing Values by Column**")
st.dataframe(df.isnull().sum())


# ------------------------------------------------------------------------------
# Visualize Missing Data
# ------------------------------------------------------------------------------
# Create a heatmap to visually indicate where missing values occur.
st.write("Heatmap if Missing Values")
fig, ax = plt.subplots()
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
st.pyplot(fig)

st.write("Distribution of Age on Titanic")
st.pyplot(sns.displot(data = df[df["age"] <= 20]["age"], bins = 50))

# ================================================================================
# Interactive Missing Data Handling
#
# Users can select a numeric column and choose a method to address missing values.
# Options include:
# - Keeping the data unchanged
# - Dropping rows with missing values
# - Dropping columns if more than 50% of the values are missing
# - Imputing missing values with mean, median, or zero
# ================================================================================
columns = st.selectbox("Choose a colum to fill", 
                       df.select_dtypes(include = "number").columns)
# only grabs columns that have numeric variables

method = st.radio("Choose a method", ["Original DF", "Impute Mean", "Impute Median", "Impute Zero"])

df_clean = df.copy()


# Work on a copy of the DataFrame so the original data remains unchanged.

# Apply the selected method to handle missing data.

if method == "Original DF":
    pass
# Impute Mean
elif method == "Impute Mean":
    df_clean[columns] = df_clean[columns].fillna(df[columns].mean())
    # Impute Median
elif method == "Impute Median":
    df_clean[columns] = df_clean[columns].fillna(df[columns].median())
    # Impute Zero
elif method == "Impute Zero":
    df_clean[columns] = df_clean[columns].fillna(0)

st.dataframe(df_clean)

# ------------------------------------------------------------------------------
# Compare Data Distributions: Original vs. Cleaned
#
# Display side-by-side histograms and statistical summaries for the selected column.
# ------------------------------------------------------------------------------

col1, col2 = st.columns(2)

# Original Data Visualization
with col1:
    st.subheader("Original Data Distribution")
    # Pot a hoistogram (with a KDE) for the selected column from the original DataFrame.
    fig, ax = plt.subplots()
    sns.histplot(df[columns], kde=True)
    plt.title(f"Original Distributions of {columns}")
    st.pyplot(fig)
    st.subheader(f"{columns}'s Original Stats")
    # Display statistical summary for the selected column
    st.write(df[columns].describe())

# Col 2 clean 
with col2:
    st.subheader("Cleaned Data Distribution")
    # Pot a hoistogram (with a KDE) for the selected column from the original DataFrame.
    fig, ax = plt.subplots()
    sns.histplot(df_clean[columns], kde=True)
    plt.title(f"Cleaned Distributions of {columns}")
    st.pyplot(fig)
    st.subheader(f"{columns}'s Cleaned Stats")
    # Display statistical summary for the selected column
    st.write(df_clean[columns].describe())