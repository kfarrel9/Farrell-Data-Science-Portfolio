# Tidy Data Project: 2008 Olympic Medalists

### Project Overview
The goal of this project is to clean/ reorganzie data from the 2008 Olympics using Python and Pandas. The original dataset contains medalists names and seperate columns for difference sports and genders. By applying tidy data principles, I restructed the dataset to make it easier to analyze by sport type, medal types and genders.

Pivot tables and visulatzations are used to explore patterns in the cleaned data.

### Original Dataset

The original dataset contains 1,875 rows and 71 columns with each athlete having their own row. Each column is a seperate gender and sport, and the values list which athlete won a medal (and the medal type) for the various sports. The original format makes it confusing to comapre medal enteries between sports and genders because these variables are combined into many columns. The data set is reorganized so that each variable has its own column. The dataset was adapted from the 2008 Olympic Medalists Dataset

### Tidy Data Principles

According to Hadley Wickham's Tidy Data, the three main prinicples are:

1. Each variable forms its own column.
2. Each observation forms its own row.
3. Each type of observational unit forms its own table.

After cleaning, the dataset contains four main variables: medalist_name, medal, gender, and sport. Each variable has its own column, and each row represents an individual athlete's medal entry. Since the dataset focuses on athlete medal entries, these observations are organized into one table. This makes it easier to compare medal entries using pivot tables and visualizations.

### Data Cleaning Process

The following steps were used to reorganize the dataset:

#### Melting the Data

pd.melt() was used to convert the dataset from wide format to long format. The medalist_name column was held constant while the original sport and gender columns were combined into a new column called Gender_Sport. The values in these columns were placed into a separate column named Medal. This made it easier to work with different medal entries without having to analyze each gender/sport column individually.

#### Removing Missing Values

After melting the data, many rows contained missing medal values because athletes only earned medals in certain sports. .dropna() was used to remove rows containing missing values in the Medal column, allowing the cleaned dataset to contain only actual recorded medal entries.

#### Separating Gender and Sport

The Gender_Sport column still contained two different variables combined into one. .str.split('_') was used to separate these variables into their own columns: Gender and Sport.

#### Removing Unnecessary Columns

Now that gender and sport were stored in separate columns, the original Gender_Sport column could be removed using .drop().

#### Sorting the Cleaned Data

.sort_values() was used to put the dataset back into alphabetical order by medalist name.

### Data Analysis and Visualizations
After cleaning the dataset, I created two pivot tables using the count aggregation function to compare medal entries by sport, medal type, and gender.

#### Pivot Table 1: Medal Entries by Sport Type and Medal Type
To compare medal entries across different sports, a pivot table is created that separates gold, silver, and bronze medals into columns. Each row represents a sport, and the count function calculates how many medal enteries fall into each category. This makes it easy to compare the number of different medal types across the various sports.

#### Visualization 1: Top 10 Olympic Sports by Medal Enteries
To see which sports had the most medal entries, I used .value_counts() to count the entries for each sport. Then, I created a bar chart of the ten sports with the highest counts. This visualization allows for a comparison of medal enteries across the most commonly won sports.

#### Visual 1 Interpretations
Athletcis had the highest number of medal enteries in the dataset, followed closely by rowing and swimming. Tehse sports all include multiple events, which may contribute to explaining their higher medal counts. The graph also shows the variability of medal enteries across various Olympic sports.

#### Visualization 2: Medal Types Across the Top Sports
After identifyinf the ten sports with the highest number of medal enteries, I wanted to look more closely at how gold, silver, and bronze medals were distributed within these sports. Using the first pivot table, I created a grouped bar chart to compare the three medal types within each sport.

#### Visualization 2 Interpretations
Athletics had the highest number of enteries across all three medal types. For most sports, the number of gold, silver, and bronze entries were relatively similar, althought there were some slight differences. These differecnes could be explained by team sizes and the number of medal events that each sport has.

#### Pivot Table 2: Medal Entries by Sport and Gender
Next, I wanted to compare the number of male and female entries across Olympic sports, so I created a second pivot table that seperates the entries by sport and gender.

#### Visualization 3: Medal Entries by Sport and Gender
For the visualization, I used the second pivot table to creaet a heatmap comparing male and female medal entries across the top ten sports. The reason a heatmap was selected for the visualization of this data is becasue the different shades of reds make it very easy to see which sports have higher or lower medal amounts for each gender.

#### Visualization 3 Interpretations
The heatmap shows differences in male and female medal entries across the top ten sports. Some sports had similar numbers of entries for both genders, such as athletics and association football; however, other sports had much larger differences. These differences could be related to the opportunities offered throughout the sports to the different genders, therefore, it is not fair to assume that the medal count differeces between genders is due to athletic performance alone.

### How to Run the Project

#### Instructions
1. Download the GitHub repository
2. Open the TidyData-Project folder in VS Code
3. Install python libraries: pandas, matplotlib, seaborn, Jupyter Notebook
4. Open the code.ipynb notebook
5. Save olympics_08_medalists.csv in same folder as the code.
6. Run the code

### Conclusions

This project shows how tidy data principles can be used to reorganize a dataset so that it is easier to work with and analyze. By melting the original Olympic dataset, removing null values, and seperating gender and sport into their own columns, useful pivot tabels and visualizations were able to be created. These visualizations showed which sports had the highest number of medal enteries, and showed how medal enteries varied by gender across various sports. However, this dataset records individual athlete medal entries which means that every member on a team sport was recorded to earn a medal. This could potentially lead to a skewed medal count for team sports. A more useful dataset would include only the unique Olympic medals awarded.

### References
- [Wickham, Hadley (2014). Tidy Data] (https://vita.had.co.nz/papers/tidy-data.pdf)
- [2008 Olympic Medalists Dataset] (https://edjnet.github.io/OlympicsGoNUTS/2008/)