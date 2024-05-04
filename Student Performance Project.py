#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Students Performance In Exams Analysis

This project is a comprehensive overview of a student's performance in different subjects and aims to find any relevant trends that could potentially explain the success and failures of students. 

We will also see if there's a correlation between student performance in exams and parent influence. However, it's crucial to understand that there could be bias behind these findings and that any reason found should not be taken as the sole determinent.
# In[ ]:


--------------------------------------------------------------------------------------------------


# In[ ]:


# Preparing & Cleaning Data


# In[1]:


import pandas as pd 
import seaborn as sns 
import matplotlib as plt


# In[17]:


# Reading File 
student_performance = pd.read_csv("StudentsPerformance.csv")
student_performance.head(10)


# In[3]:


# Number of Rows and Columns 

student_performance.shape


# In[4]:


# Checking For Missing Values 

student_performance.isnull().sum()


# In[5]:


# Describing Data 

student_performance.describe()


# In[18]:


# Renaming Columns 

student_performance = student_performance.rename(
                        columns = {"parental level of education": "parent education", 
                                   "test preparation course": "test preparation"})
student_performance.head(5)


# In[19]:


# Adding Average Score Column 

student_performance['average_score'] = student_performance[
                   ['math score', 'writing score', 'reading score']].mean(axis=1).round(2)
student_performance['average_score'].head(5)


# In[20]:


# Information About Dataset 

student_performance.info()


# In[ ]:


--------------------------------------------------------------------------------------------------


# In[ ]:


# Basic Statistical Analysis


# In[12]:


# 1.) What was the average score in all subjects based on parent's education level ?

student_performance.groupby("parent education")["average_score"].mean().round(2)


# In[10]:


# 2.) What was the average math score by test preparation? 

student_performance.groupby("test preparation")["math score"].mean().round(2)


# In[14]:


# 3.) What was the average score across all subjects by test preparation?

student_performance.groupby("test preparation")["average_score"].mean().round(2)


# In[17]:


# 4.) How many students recieved a passing grade based on parent's education level? 
#     Passings grades are considered 'C' and above. 

passing_grade = student_performance.loc[student_performance["Grade"].isin(['A','B','C'])]
passing_grade.groupby("parent education")["Grade"].count()


# In[18]:


# 5.) What was the average score across all subjects based on lunch status.

student_performance.groupby("lunch")["average_score"].mean().round(2)


# In[ ]:


--------------------------------------------------------------------------------------------------


# In[ ]:


# Graphical Analysis


# In[38]:


# 1.) Number of students who recieved a passing grade based on parents with an associate's, bachelors's, master's degree.

grouped_data = student_performance.groupby("parent education")["average_score"].mean().round(2)
                                            
ax = sns.barplot(filtered_degrees, x = "parent education", y = "average_score", hue = "parent education")
ax.set(title = "Average Score by Parent Education", xlabel = "Parent Education", ylabel = "Average Score")


# In[20]:


# 2.) Number of students who have recieved a standard lunch and who have passed & failed by parent's education level.

filtered_grades = student_performance.loc[(student_performance["Grade"].isin(['A', 'B', 'C']))
                & (student_performance["lunch"] == "standard")]
ax = sns.countplot(data = filtered_grades, x = "parent education", hue = "Grade", dodge = True)
ax.set(title = "Passing Grades by Parent Education Level", xlabel = "Parent Education Level", ylabel = "Count of Grades")


# In[28]:


# 3.) Math grades based on test preperation as a box plot. 

ax = sns.boxplot(data = student_performance, x = "math score", y = "test preparation", hue = "test preparation")
ax.set(title = "Math Grades Based on Test Preparation", xlabel = "Math Score", ylabel = "Test Preparation")


# In[20]:


# 3.) Number of students who recieved a passing grade by test preparation. 

filtered_grade_prep = student_performance.loc[student_performance["Grade"].isin(['A','B','C'])]
hue_order = ['C', 'B', 'A']
ax = sns.countplot(filtered_grade_prep, x = "test preparation", hue = "Grade", hue_order = hue_order)
ax.set(title = "Number of Students Who Passed by Test Preparation", xlabel = "Test Preparation", 
       ylabel = "Number of Students")


# In[28]:


# 4.) Distribution of Parent Education by Average Score Using Violin Plot.

ax = sns.violinplot(student_performance, x = "average_score", y = "parent education", 
                    hue = "parent education")
ax.set(title = "Distribution of Parent Education Level by Average Score") 


# In[30]:


# 5.) Number of students who has a standard lunch by race / ethnicity

filtered_test_prep = student_performance.loc[(student_performance["test preparation"] == "completed"), 
                    ["race/ethnicity", "test preparation"]]
ax = sns.countplot(filtered_test_prep, x = "race/ethnicity", hue = "test preparation")
ax.set(title = "Number of Students Who Has a Standard Lunch by Race / Ethnicity", xlabel = "Race / Ethnicity", 
       ylabel = "Count")


# In[ ]:


--------------------------------------------------------------------------------------------------


# In[9]:


# Creating Grade Calculation Function  

def grade(average_score): 

    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 50:
        return 'D'
    elif average_score < 50:
        return 'F'


# In[10]:


# Creating Letter Grade Column 

student_performance["Grade"] = student_performance.apply(
                    lambda x : grade(x['average_score']), axis = 1)
student_performance["Grade"].head(5)


# In[ ]:




