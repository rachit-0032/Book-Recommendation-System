#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
import xgboost as xgb


# In[2]:


import numpy as np
import pandas as pd


# In[4]:


X_train = pd.read_csv('./UltimateFinal/Regression/X_train.csv')
y_train = pd.read_csv('./UltimateFinal/Regression/y_train.csv')
X_test = pd.read_csv('./UltimateFinal/Regression/X_test.csv')
y_test = pd.read_csv('./UltimateFinal/Regression/y_test.csv')


# In[5]:


D_train = xgb.DMatrix(X_train, label=y_train)
D_test = xgb.DMatrix(X_test, label=y_test)


# In[6]:


regressor=xgb.XGBRegressor(eval_metric='rmse')


# In[ ]:


#=========================================================================
# exhaustively search for the optimal hyperparameters
#=========================================================================
from sklearn.model_selection import GridSearchCV
# set up our search grid
param_grid = {"max_depth":    [5, 7],
              "n_estimators": [100, 200, 500],
              "learning_rate": [0.01, 0.05]}

# try out every combination of the above values
search = GridSearchCV(regressor, param_grid, cv=5, verbose=3).fit(X_train, y_train)

print("The best hyperparameters are ",search.best_params_)


# In[ ]:


regressor=xgb.XGBRegressor(learning_rate = search.best_params_["learning_rate"],
                           n_estimators  = search.best_params_["n_estimators"],
                           max_depth     = search.best_params_["max_depth"],)

regressor.fit(X_train, y_train)


# In[7]:


predictions = regressor.predict(X_test)


# In[8]:


from sklearn.metrics import mean_squared_log_error
RMSLE = np.sqrt( mean_squared_log_error(y_test, predictions) )
print("The score is %.5f" % RMSLE )


# In[ ]:




