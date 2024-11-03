## OTD Metrics

On-time Delivery (OTD) Predictive Modeling, Project Owner, Northeastern University Mar 2024

Software: Jupyter Notebook, Python, Streamlit app | Observations: 10K | f1-score: 0.69 | Accuracy: 68% | AUC: 0.75

Project Scope – Trained CatBoost model linked to Streamlit application to input “key variables” to predict “delivery time” for OTD metrics

### Project Background
Dataset Structure
1. 10,999 observations​
2. 12 key variables​
3. Categorical 5, Numerical 7​
4. Response Variable – Y/N​

Objective - Our motive has been to analyze this dataset, which entails customers’ journeys, and build a predictive model to make better predictions of “Reached On-time (Y/N)” under consideration of a few significant predictive features

Data Pre-processing - Loading Dataset -> Feature Categorization -> Feature Engineering -> One-hot Encoding -> Splitting Dataset -> Hyperparameter Tuning

### EDA Observations
Our EDA aimed to uncover underlying patterns and relationships within the dataset. Key observations included the distribution of customer care calls, which mostly ranged between 2 and 5, and the evenly distributed customer ratings from 1 to 5. The analysis also revealed a balanced distribution between on-time and delayed deliveries, setting a solid foundation for further investigative modeling

### Model Selection and Evaluation
The predictive models, including XGBoost, CatBoost, Random Forest, and Decision Tree, were selected based on their robustness in handling categorical and numerical data. Their performance in classifying on-time deliveries was thoroughly compared. CatBoost model demonstrated balanced performance in predicting both "False Positives" and "True Positives.

### Model Deployment
1. Streamlit Application: A user-friendly tool for inputting variables and receiving delivery time predictions, directly aiding operational decisions
2. Technical Integration: Incorporating a trained CatBoost model for predicting delivery statuses seamlessly within the application
3. User Input Processing: Collecting and processing inputs to predict delivery statuses based on warehouse block, shipment mode, and customer care calls
4. Operationalizing Insights: Empower logistic managers to make informed decisions by effectively predicting and managing delivery expectations
5. Future Enhancements: Opportunities for refining the model, integrating additional features, and improving accessibility for broader usability

### Recommendation
1. Strategic Recommendations​ - We recommend the e-commerce company fine-tune its discount strategies to mitigate the adverse impact on logistics and explore weight-based logistical planning to improve delivery efficiency
2. Future Analysis Directions​ - For a more rounded analysis, incorporating variables such as regional shipping data and seasonal factors could offer more profound insights​

### Conclusion​
This report underscores the significance of on-time delivery in achieving customer satisfaction and sustaining a competitive edge in e-commerce. It highlights the indispensable role of data-driven insights in informing strategic decisions. Although the dataset is more straightforward and structured, any additional features would improve the model’s performance.​



​

​

​

​

​

​

​

​
​

​
