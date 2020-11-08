# Credit Card Fraud Model

## Introduction
Credit card fraud is an important issue that requires large amounts of effort to fight against. Capital One incurrs the losses from fradualent transactions, but there is also a customer aspect. When a customer is impacted directly they may lose faith in our efforts to combat this problem and leave to a competitor. Therefore, it is important to focus our efforts in detecting and preventing fraud.

## User Changes

Modify the notebooks local directory where you have saved the dats and the pyscript.

The file name function_call.py contains custom functions used throughout the notebook. To quickly view the functions execute the following line:

        - %load function_call

## Project Performance Summary

![](https://github.com/StevenLoaiza/Fraudmodel/blob/main/ROC_Curve.png?raw=true)

We build two models above to predict fraud. The first model was a naive logistic regression. All we did was throw the data into the model and checked the performance. As expected, the model did not do well. It failed to identify any fraudlant cases. Instead the model predicted that all the transactions were non fraudualant.

Next, we did some feature engineering and dealt with our unbalanced dataset. This new dataset was then used in a Random forest classification model. Given that our logistic regression performed terrible and was our baseline, all the random forest model needed to do was marginally predict that some transaction are in fact fraudulant.

### Success

We are going to present the ROC Curve as the models success metric. The ROC curve tells us how well our model is at distingushing between the two classes. If the Curve has an AUC = 1.0 then the model does an amazing job of seperating out the classes, but an AUC=0.5 means it has no capabilities of seperating out the classes. When the model was used to make predictions on the test set, the AUC= 0.67. The metric is good, given that our baseline model was unable to detect fraud at all.

### Model Failure

The model performance metric does exceptionally well on the training dataset and does poorly on the test set (in contrast). This leads me to believe that our model is failing to generalize well to unseen data. My conjecture is that our random forest model is overfitting the training dataset (learning more than just the underlying structure, also fitting to the noise), therefore it will underperform on the test dataset.

### Future Implementation

Below are some future implementation we will look into:
1. New Features (e.g. Time elapse from Account open to the transaction)
2. Other sampling techniques
3. Cross Validation to tune the random forest hyperparameters (e.g max_depth, number of trees etc)

I am confident that the model would be able to generalize better to unseen data and have higher success metrics.
