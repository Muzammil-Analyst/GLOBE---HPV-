#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[6]:


dataHPV = pd.read_csv("LS_Error_Checks.csv", encoding='utf-8-sig')


# In[7]:


dataHPV.head()


# In[8]:


dataHPV.info()


# In[9]:


def duplicate_check(dataANC):
    duplicate=dataANC.duplicated().any()
    return duplicate


# In[11]:


# Get the count of null values for each column
null_counts = dataHPV.isnull().sum()

print("Null value counts for each column:")
for column, count in null_counts.items():
    print(f"{column}: {count}")


# In[12]:


def create_error_check(dataHPV, condition, field_name, error_value, remarks):
    selected_columns = ['el_studyid','el_interviewer']
    error_checks = dataHPV.loc[condition , selected_columns]
    error_checks['Field Name'] = field_name  # Combine field names if multiple
    error_checks['Error Value'] = error_value  # Convert to strings and join
    error_checks['Remarks'] = remarks



    pd.set_option('display.max_rows', 1000)
    return error_checks


# In[14]:


remarks = " Question 4.2 is greater then Question 4.9 marked as 1 and 4.16 marked as 1 error"
condition =(dataHPV['sb_sex_count_last']  >  (dataHPV['sb_sex_period']== 1) & (dataHPV['sb_relation_period']== 1))
field_name = 'sb_sex_period'
error_value = dataHPV['sb_sex_count_last']

result = create_error_check(dataHPV, condition, field_name, error_value, remarks)



#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'Do you have any children is marked as No Who Lives Most of the time marked as own Children .xlsx'
#result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)


# In[30]:


remarks = 'Question 0.2 found Null Error'+dataHPV['el_age'].astype(str)
condition =(dataHPV['el_age']).isnull()
dataHPV['el_interviewer'] = pd.to_numeric(dataHPV['el_interviewer'], errors='coerce')
field_name = 'el_age'
error_value = dataHPV['el_age']
result = create_error_check(dataHPV, condition, field_name, error_value, remarks)



#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'Do you have any children is marked as No Who Lives Most of the time marked as own Children .xlsx'
#result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)
#No-Error


# In[20]:


remarks   = "Question 1.21 is yes and Question 1.20 is living most of the time with Husband error"+dataHPV['sc_live_with_partner'].astype(str)
condition =  (dataHPV['sc_partner_night_out'] == 1 ) & (dataHPV['sc_live_with_partner'] == 2 )
field_name =  'sc_partner_night_out'
error_value = dataHPV['sc_live_with_partner']
result = create_error_check(dataHPV, condition, field_name, error_value, remarks)



#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result_output_file = 'Spend_4_Nights_live_most_of_time.xlsx'
result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)


# In[21]:


remarks = 'Question 1.8ismarked as 1 and Question 1.12 is not marked as partner or Husband error'+dataHPV['sc_married'].astype(str)
condition =(dataHPV['sc_married'] == 1 )  & (dataHPV['sc_most_live_mm___1'] == 0)
field_name = 'sc_married'
error_value = dataHPV['sc_most_live_mm___1']
result = create_error_check(dataHPV, condition, field_name, error_value, remarks)


#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'Do you have any children is marked as No Who Lives Most of the time marked as own Children .xlsx'
#result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)
#No-Error


# In[33]:


remarks = 'Question 0.6 Duartion of Living is Greater then your Birth Date'+dataHPV['el_live_year'].astype(str)
condition =(dataHPV['el_age'])  >  (dataHPV['el_live_year'])
field_name = 'el_age'
error_value = dataHPV['el_live_year']
result = create_error_check(dataHPV, condition, field_name, error_value, remarks)


#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'Do you have any children is marked as No Who Lives Most of the time marked as own Children .xlsx'
#result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)
#No-Error


# In[40]:


remarks = 'Question:0.9 Have you ever been married is Yes and Question:1.9 is Null Error'+dataHPV['sc_age_at_married'].astype(str)
condition = (dataHPV['el_vaginal_sex'] == 1) & (dataHPV['sc_age_at_married'].isnull())
field_name = 'el_vaginal_sex'
error_value = dataHPV['sc_age_at_married']
result = create_error_check(dataHPV, condition, field_name, error_value, remarks)


#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'Do you have any children is marked as No Who Lives Most of the time marked as own Children .xlsx'
#result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)
#No-Error


# In[43]:


remarks = "Question 1.10 is No and Question 1.12 is marked as 5 (Own Children) Count as error"+dataHPV['sc_most_live_mm___5'].astype(str)
condition =(dataHPV['sc_have_children'] == 4) & (dataHPV['sc_most_live_mm___5']== 1)
field_name = 'sc_have_children'
error_value = dataHPV['sc_most_live_mm___5']

result = create_error_check(dataHPV, condition, field_name, error_value, remarks)



#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'Do you have any children is marked as No Who Lives Most of the time marked as own Children .xlsx'
result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)


# In[46]:


remarks = "Question:4.25 is Previously pregnant and Question:4.26 is greater then Q4.27 error" + dataHPV['sb_preg_times'].astype(str)
condition = (dataHPV['sb_preg'] ==2) & (dataHPV['sb_preg_times'] < dataHPV['sb_pr_livebirth'])
field_name = 'sb_pr_livebirth'
error_value = dataHPV['sb_preg_times']

result = create_error_check(dataHPV, condition, field_name, error_value, remarks)


#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result_output_file = 'Q4.25 is Previously pregnant and Q4.26 is greater then Q4.27 count as error.xlsx'
result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)


# In[49]:


remarks = "Question 0.6 Should be less then or equal to 0.2 if not found error"
condition = (dataHPV['el_live_year']) > (dataHPV['el_age'])
field_name = 'el_age'
error_value = dataHPV['el_live_year']

result = create_error_check(dataHPV, condition, field_name, error_value, remarks)


#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
#result_output_file = 'How long have you lived here? Should be less than or equal to Q0.2- How old were you at your last birthday?.xlsx'
#result.to_excel(result_output_file, index=True)
result
#result.to_excel('error_report_A1.xlsx', index=True)


# In[ ]:




