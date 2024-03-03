# Heart Disease Detection web Application
This project encompasses a comprehensive Heart Disease Detection System implemented using Python, machine learning techniques, and a user-friendly web application interface built with Streamlit.

## Data Science and Machine Learning
The data science and machine learning part of the project entail the following steps:

Data Preprocessing: The dataset containing heart disease-related data is loaded and preprocessed using pandas. Initial exploratory data analysis (EDA) is performed to understand the data's characteristics and structure.
Visualization: Visualizations such as count plots, histograms, and heatmaps are generated using Matplotlib and Seaborn libraries to gain insights into the data and explore correlations.
Model Building: Several machine learning models including Logistic Regression, Random Forest, XGBoost, K Neighbors, and Support Vector Machine (SVM) are trained and evaluated using techniques like validation curves and confusion matrices to determine the best-performing model.
Model Evaluation: Model performance is evaluated using accuracy scores and confusion matrices to assess their predictive capabilities.
Model Selection and Export: XGBoost is identified as the best-performing algorithm and is exported using joblib for integration into the Streamlit application.
## Streamlit Web Application
The Streamlit web application component enables users to interactively input their medical data and obtain predictions about the presence of heart disease. Key features of the application include:

User Interface: The user interface is designed to be intuitive and user-friendly, allowing users to input parameters such as age, gender, cholesterol levels, and other relevant factors.
Prediction: Upon user input, the application leverages the pre-trained XGBoost model to predict the likelihood of heart disease based on the provided data.
Visual Feedback: Users receive visual feedback in the form of error or success messages, indicating whether they are likely to have a heart disease based on the input parameters.

![Screenshot 2024-03-03 184358](https://github.com/yuseiff/AI-Powered-Heart-Disease-Detection-Web-App-/assets/111249341/aaaa248d-3d08-40af-ac61-5f8a17a7f925)
![Screenshot 2024-03-03 184255](https://github.com/yuseiff/AI-Powered-Heart-Disease-Detection-Web-App-/assets/111249341/e10522ba-6c10-479b-9a79-06e71fdcde0d)

![Screenshot 2024-03-03 184238](https://github.com/yuseiff/AI-Powered-Heart-Disease-Detection-Web-App-/assets/111249341/74d4f276-c7f9-4fbf-a516-301f955622df)
