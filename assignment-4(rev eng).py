# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:40:24 2022

@author: bhava
"""
import pandas as pd
users=pd.read_excel("C:/Users/bhava/OneDrive/Documents/insta.xlsx")
users.head()
#users.columns=["Age_group","number of responds","percentage"]
#users.head()

import matplotlib.pyplot as plt
plt.boxplot(users)
plt.hist(users)
import numpy as np
x=np.array("Age_group")
y=np.array("percentage")
plt.plot(x)
plt.plot(y)
plt.plot(x,y)
plt.xlabel("Age_group")
plt.ylabel("Users")
plt.title("Age_group VS Users")
plt.grid(color="Yellow")
plt.bar(x,y,color='red')
plt.barh(x,y)
plt.pie(users)
plt.xlabel("Age_group")
plt.ylabel("Users")
plt.title("Age_group VS Users")

from scipy.stats import f_oneway
f_oneway(users.teenagers,users.youngadults,users.middleadults,users.agedperson)

sab=[100,80,90,70,160]
import matplotlib.pyplot as plt
plt.boxplot(sab)
import numpy as np
data=np.random.normal(80,2,100)
plt.hist(data)
plt.boxplot(data)

import numpy  as np
x=np.array([12,24,3,44,50])
y=np.array([16,17,18,19,20])
plt.plot(x)
plt.plot(y)
plt.plot(x,y)#line plot
plt.plot(x,'s:b')#dot plot(univariant)
plt.plot(y,'o:b')#dot plot(univariant)
plt.plot(x,y,'v:b')#scatter plot(bivarient)
plt.plot(y,'^-b')#runtogether to compare


plt.plot(x,y)
plt.xlabel('height')
plt.ylabel('weight')
plt.title('Height VS Weight')
plt.grid(color="red")

x=['Red','Yellow','Green','Blue','Pink']
y=[10,12,14,16,18]
plt.bar(x,y,color='red')
plt.barh(x,y)
plt.pie(y)
plt.scatter(x,y)#only numbers
plt.figure(figsize=(12,5))
plt.scatter(x,y)




