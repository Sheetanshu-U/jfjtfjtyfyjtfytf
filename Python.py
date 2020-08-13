# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:14:22 2020

@author: Admin
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("C:/Users/Admin/Desktop/Stats/Capstone/Dataset _1.csv")


#########https://www.youtube.com/watch?v=57vFbsiZYHg

data.isna().sum()

ab = data.dropna(how='a')

##############data summary
################complete cases
############select complete cases

##############reading selected variables in python

data.describe()


print(data.head(5))
print(data)

da = data.iloc[2:5, 1:10]
da
data.iloc[2:5, 5]

pd.set_option('display.max_rows', 30)

pd.set_option('display.max_columns', 50)

cat = data[['Currency Rate (INR - USD)', 'FII Investments (India) - Crores']]

cat2 = data.iloc[:, 2:3]

###############list, touple, dictionery


################https://www.youtube.com/watch?v=vV2KGL6W1eA
##################https://www.youtube.com/watch?v=Q06Y3DUSwz4
#################https://www.youtube.com/watch?v=NZIu0wL2v_U
#################https://www.youtube.com/watch?v=pjJPkWWxd9c


##########https://www.youtube.com/watch?v=-Bjko05HKWM
###one hot encoding



###############categorical variables in python and ow to change the data type


dat = pd.read_csv("C:/Users/Admin/Desktop/Cellphonedata.csv")

print(dat)

dat.describe()

print(dat.info())


##############https://www.datacamp.com/community/tutorials/categorical-data
###data cleaning



########https://stackoverflow.com/questions/47785101/python-convert-object-data-type-to-integer-string-or-float-based-on-data-in-d
####change data type in python









