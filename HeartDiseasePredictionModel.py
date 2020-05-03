#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sn
sn.set()
dataset = pd.read_csv('framingham.csv')


# In[2]:


dataset.drop(['education'], inplace=True, axis=1)
def check(c):
    count=0
    for x in dataset.index:
        if pd.isnull(dataset[c][x]):
            count = count + 1
        
    return count


# In[3]:


count=0
count1=0
summ=0
sum1=0
for x in dataset.index :
    if pd.isnull(dataset['glucose'][x]):
        pass
    else:
        if dataset['diabetes'][x] == 1:
            summ = summ + dataset['glucose'][x]
            count = count + 1
        elif dataset['diabetes'][x] == 0 :
            sum1 = sum1 + dataset['glucose'][x]
            count1 = count1 + 1
        else:
            pass
    
mean1, mean0 = summ/count, sum1/count1

print(mean1, mean0)
        
    
def impute(cols):
    glucose = cols[0]
    diabetes = cols[1]
    
    if pd.isnull(glucose):
            
        if diabetes==1:
            return mean1
        elif diabetes==0:
            return mean0
    else:
        return glucose
    
dataset['glucose'] = dataset[['glucose', 'diabetes']].apply(impute, axis=1)
check('glucose')


# In[4]:


ct=0
ct1=0
sm=0
sm1=0
for x in dataset.index :
    if pd.isnull(dataset['BMI'][x]):
        pass
    else:
        if dataset['prevalentStroke'][x] == 1:
            sm = sm + dataset['BMI'][x]
            ct = ct + 1
        elif dataset['prevalentStroke'][x] == 0 :
            sm1 = sm1 + dataset['BMI'][x]
            ct1 = ct1 + 1
    
mean11, mean00 = sm/ct, sm1/ct1

print(mean11, mean00)

def imp(cols):
    BMI = cols[0]
    stroke = cols[1]
    
    if pd.isnull(BMI):
            
        if stroke==1:
            return mean1
        elif stroke==0:
            return mean0
    else:
        return BMI
    
dataset['BMI'] = dataset[['BMI', 'prevalentStroke']].apply(imp, axis=1)
check('BMI')


# In[5]:


def calc(cols):
    bp = cols[0]
    hyp = cols[1]
    
    if pd.isnull(bp):
            
        if hyp==1:
            return 1.0
        elif hyp==0:
            return 0.0
    else:
        return bp
    
dataset['BPMeds'] = dataset[['BPMeds', 'prevalentHyp']].apply(calc, axis=1)
check('BPMeds')


# In[6]:


cnt=0
cnt1=0
tot=0
tot1=0
for x in dataset.index :
    if pd.isnull(dataset['totChol'][x]):
        pass
    else:
        if dataset['BPMeds'][x] == 1.0:
            tot = tot + dataset['totChol'][x]
            cnt = cnt + 1
        elif dataset['BPMeds'][x] == 0.0 :
            tot1 = tot1 + dataset['totChol'][x]
            cnt1 = cnt1 + 1
    
mean111, mean000 = tot/cnt, tot1/cnt1

print(mean111, mean000)

def calv(cols):
    chol = cols[0]
    bp = cols[1]
    
    if pd.isnull(chol):
            
        if bp==1.0:
            return mean111
        elif bp==0.0:
            return mean000
    else:
        return chol
    
dataset['totChol'] = dataset[['totChol', 'BPMeds']].apply(calv, axis=1)
check('totChol')


# In[7]:


cnt=0
cnt1=0
tot=0
tot1=0
for x in dataset.index :
    if pd.isnull(dataset['cigsPerDay'][x]):
        pass
    else:
        if dataset['male'][x] == 1:
            tot = tot + dataset['cigsPerDay'][x]
            cnt = cnt + 1
        elif dataset['male'][x] == 0 :
            tot1 = tot1 + dataset['cigsPerDay'][x]
            cnt1 = cnt1 + 1
    
mean1111, mean0000 = tot/cnt, tot1/cnt1

print(mean1111, mean0000)

def calt(cols):
    cig = cols[0]
    male = cols[1]
    
    if pd.isnull(cig):
            
        if male==1:
            return mean1111
        elif male==0:
            return mean0000
    else:
        return cig
    
dataset['cigsPerDay'] = dataset[['cigsPerDay', 'male']].apply(calt, axis=1)
check('cigsPerDay')


# In[8]:


total = 0
count = 0
for x in dataset.index :
    if pd.isnull(dataset['heartRate'][x]):
        pass
    else:
        if dataset['male'][x]==1:
            total = total + dataset['heartRate'][x]
            count = count + 1
            
avg = total/count
print(avg)

dataset['heartRate'][689] = avg

check('heartRate')


# In[12]:


from sklearn.linear_model import LogisticRegression as lr
x = dataset[['male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds',
       'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
       'diaBP', 'BMI', 'heartRate', 'glucose']]
y = dataset['TenYearCHD']
model = lr()
model.fit(x,y)


# In[14]:


from sklearn.externals import joblib
joblib.dump(model,'heart_disease_prediction.pk1')

