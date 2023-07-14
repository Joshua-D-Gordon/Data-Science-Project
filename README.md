# Data Science Project

## Project Overview
This project consists of two parts: a classification model and a regression model.

### Part One: Classification Model
In this part, a KNN model is built to predict the year (between 2015 - 2019) in which a survey was conducted based on nine features from the World Happiness report dataset. The goal is to classify the survey year as a 5-class classification problem. The project involves merging five datasets, one from each year, and adding a column for the respective year. The following steps were performed:

1. Data cleaning: To ensure consistency, unique column headings were dropped, and only the shared headings and data were retained across all five datasets.
2. Feature understanding: The dataset contains features such as overall rank, country/region, score, GDP per capita, social support, healthy life expectancy, freedom of choices, generosity, perceptions of corruption, and the year.
3. Data merging: The cleaned datasets were merged into a single dataframe to create a comprehensive dataset for model training and evaluation.
4. Data preprocessing: Null values were checked, missing values were filled, and categorical features (country/region) were converted into numerical values.
5. Model training and evaluation: The KNN classifier model was trained on the merged dataset. The data was split into training and testing sets (80/20 split). The model's accuracy was evaluated against Sklearn's dummy classifier. Hyperparameter tuning was performed using k-fold validation to find the optimal value of k.
6. Performance improvement: As the classification accuracy was initially low due to the low variance in survey results across years, attempts were made to improve the model's performance.

### Part Two: Regression Model
In this part, the goal is to predict the writing score on a test based on various features, including gender, parental level of education, lunch, test preparation course, math score, and reading score. The dataset was analyzed, and the distributions of the features were plotted. The "race/ethnicity" feature, which had no clear meaning and could introduce bias, was dropped. The focus was on predicting the writing score label.

## Data Description
### Part One
The features in the World Happiness report dataset include overall rank, country/region, score, GDP per capita, social support, healthy life expectancy, freedom of choices, generosity, perceptions of corruption, and the year.

### Part Two
The features for the dataset in Part Two include gender, parental level of education, lunch, test preparation course, math score, reading score, and writing score.

## Methodology
The methodology employed in this project includes data cleaning, exploratory data analysis, data merging, preprocessing, model training, evaluation, and performance improvement.

### Data Cleaning
The datasets were imported and cleaned, ensuring consistent column headings and dropping irrelevant columns.

### Exploratory Data Analysis
The distributions of features were analyzed and plotted to gain insights into the data.

### Data Merging
The datasets from each year were merged into a single dataframe to create a comprehensive dataset for analysis and modeling.

### Preprocessing
Null values were checked and filled. Categorical features were converted into numerical values.

### Model Training and Evaluation
The KNN classifier model was trained on the merged dataset. The data was split into training and testing sets using an 80/20 split. The accuracy of the model was evaluated against Sklearn's dummy classifier. Hyperparameter tuning was performed using k-fold validation.

### Performance Improvement
Efforts were made to improve the model's performance by selecting appropriate features and optimizing hyperparameters.

## Results
The results of the classification model showed low accuracy due to the low variance in survey results across years. However, by using a subset of features and optimizing the model, an accuracy of 54.43% was achieved, outperforming the initial classifier and the standard dummy classifier.

## Conclusion
In conclusion, this project involved building a classification model to predict the year of a survey based on World Happiness report data. The results highlighted the challenges of classifying the survey year accurately due to low variance across years. However, through feature selection and model optimization, the accuracy was improved. The regression model focused on predicting the writing score based on various features. The project provides insights into the data and presents potential directions for future research and improvement.
