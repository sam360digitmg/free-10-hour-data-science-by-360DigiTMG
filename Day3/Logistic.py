import pandas as pd
import numpy as np
# import seaborn as sb
import matplotlib.pyplot as plt

import statsmodels.formula.api as sm

from sklearn import metrics

#Importing Data
claimants = pd.read_csv("C:/Datasets_BA/Logistic regression/claimants.csv",sep=",")


#removing CASENUM
claimants = claimants.drop('CASENUM', axis = 1)
claimants.head(10)

# Model building 
# import statsmodels.formula.api as sm
logit_model = sm.logit('ATTORNEY ~ CLMAGE + LOSS + CLMINSUR + CLMSEX + SEATBELT', data = claimants).fit()

logit_model.summary()

#prediction
pred = logit_model.predict(claimants.iloc[ :, 1: ])

# Creating new column 
claimants["pred"] = np.zeros(1340)

# taking threshold value as 0.5 and above the prob value will be treated as correct value 
claimants.loc[pred > 0.5, "pred"] = 1

# confusion matrix
confusion_matrix = pd.crosstab(claimants.pred, claimants['ATTORNEY'])
confusion_matrix

accuracy_train = (487 + 393)/(487 + 262 + 198 + 393)
print(accuracy_train)
