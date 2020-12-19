# Data Science Customer Churn: Project Overview

* Created a tool that estimates the success rate of the Kickstarter funding project to help an entrepreneur achieve a successful campaign.
* Optimised Linear, DecisionTree, and Random Forest Regression using GridsearchCV to reach the best model.
* Built a client-facing API using flask and Heroku to view that on the web.

# Code and Resources Used

**Python Version**: 3.7

**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, flask, json, pickle

**For Web Framework Requirements**: pip install -r requirements.txt

**Data Resource (Kaggle)**: https://www.kaggle.com/emregur/churndata

# Data Cleaning and EDA

![](/images//balance.PNG)

![](/images//corr.PNG)

![](/images//Geo.PNG)

![](/images//age.PNG)

## Insight

- 97k is the average balance in the bank.
- 36% of the customers had zero bank balance. It would have been great to look their transaction history.
- Males tend to have more balance in the bank compare to Female. On Avearge Males had 98k deposited in the bank compare to female had 96k.
- 36% of the Females had zero bank balance, slightly edging males.
- There are no correlation between Estimated salary and Amount of balance in the bank. However,there is a weak correlation between age and exited.
- There are twice as many French accounts compare to Spain and Germany.
- It is interesting to see mean balance for germany accounts is 119k vs (60k+ for Spain and France).
- No Account belowing to Germany has Zero Balance in the bank.
- It looks like accounts are not closed because of less money in the account, in fact its quite the opposite.
- The mean age of churned customer is 45 compare to non churned customer is 35.

# Model Building 
First, I transformed the categorical variables into dummy variables. I also split the data into train and test sets with a test size of 20%.

I tried four different models and evaluated them using Precision, Recall and confusion matrix. I chose the confusion matrix because it is relatively easy to interpret.

I tried four different models:

Linear Logistic – Baseline for the model

Decision Tree and Kneighborsclassifier 

Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

![](/images//model1.PNG)

![](/images//model2.PNG)

![](/images//model3.PNG)

# Model Performance

The Random Forest model far outperformed the other approaches on the test and validation sets.

Random Forest :
Accurary score of 85.7% on Testing Data. 
Accurary score of 86.9% on Training Data. 


 # [Production](https://bankml.herokuapp.com/) 
 In this step, I built a client facing API endpoint and model was hosted on Heroku.
 
## Setup for Deployment of the model on Heroku:

![](/images/predict.png)

1.Procfile

![](/images/profile.png)

[2. App](https://github.com/Jaspreetsm21/Bank_churn_ML/blob/main/app.py)

python script for deploying the model using flask.

3.requirements

![](images/requirements.png)
