import os
os.chdir(r"C:\Users\Ganesh\OneDrive\Desktop\Projects\BANK_Account_IFSC_Code_Validation")
import pandas as pd
import re

#Csv File Read
df = pd.read_csv("IFSC_Account_Validation_Dataset.csv")
print(df.head(10))
Total_records = len(df)
print("Total Records :",Total_records)

# *** Data Cleaning ***

#Converting the account number and the ifsc,name,branch columns to string and remove the extra spaces and convert them to upper case,title
df['Account_Number'] = df['Account_Number'].astype('string').str.strip().str.upper()
df['IFSC_Code'] = df['IFSC_Code'].astype('string').str.strip().str.upper()
df['Customer_Name'] = df['Customer_Name'].astype('string').str.strip().str.title()
df['Branch'] = df['Branch'].astype('string').str.strip().str.title()
print(df.head(5))

#Finding the empty and NA Values in the Account_Number column in data frame
print(df[df['Account_Number'] == ''])
print(df[df['Account_Number'].isna()])
print("Length of NA values in Account_Numbers:",len(df[df['Account_Number'].isna()]))

#Convert empty values to NA values in dataframe account_number column and drop NA Values
df = df.replace({'Account_Number':''},pd.NA).dropna(subset = 'Account_Number')
print("After Removing the NA Values Length of NA values in Account_Number:",len(df[df['Account_Number'].isna()]))

#similarily remove the NA and empty values in every column in data frame
#similarily remove the NA and empty values in Customer_Name column in data frame
print("Length of NA values Customer_Name:",len(df[df['Customer_Name'].isna()]))
df = df.replace({'Customer_Name':''},pd.NA).dropna(subset = 'Customer_Name')
print("After Removing the NA Values Length of NA values in Customer_Name:",len(df[df['Customer_Name'].isna()]))

#similarily remove the NA and empty values in IFSC column in data frame
df = df.replace({'IFSC_Code':''},pd.NA).dropna(subset = 'IFSC_Code')

#similarily remove the NA and empty values in Branch column in data frame
df = df.replace({'Branch':''},pd.NA).dropna(subset = 'Branch')

# Find the length after removing the all NA Values in the DataFrame
print("Before Removing the NA Values :",Total_records)
print("After cleaning the NA Values in DataFrame The Length is :\n",len(df))

#Similarly remove the duplicates in dataframe
#finding the unique values in the columns
print("Unique Values in Account_Numbers :",df['Account_Number'].nunique())
#Droping the Duplicate account numbers
df = df.drop_duplicates(subset = 'Account_Number',keep = "first")
print(len(df))

# ** Data Cleaning Completed ***

# *** Data Validation ***

def has_sequence(acc):
    #for i in range(len(acc) - 1):
        #if (acc[i+1] - acc(i)) != 1:
           # return False
        digits = [int(ch) for ch in acc]   
        #return True
        # or
        return all(digits[ch+1]- digits[ch] == 1 for ch in range(len(digits)-1))
        
"""print(has_sequence('123456'))     
print(has_sequence('142378'))"""

def has_adjacent_repetataion(acc):
        digits = [int(ch) for ch in acc]
        return all(digits[ch] == digits[ch+1] for ch in range(len(digits)-1))

"""print(has_adjacent_repetataion('111111'))"""

print(str.isdigit('123'))


def is_valid_acc(acc):
        if not (9 <= len(acc) <= 18):
                return False
        
        if not re.match(r"^[0-9]{9,18}$",acc):
                return False
        
        if has_adjacent_repetataion(acc):
                return False
        
        if has_sequence(acc):
                return False
        
        if not acc.isdigit():
                return False
        
        return True

df['Acc_No_Check'] = df['Account_Number'].apply(lambda x: "Valid" if is_valid_acc(x) else "In Valid")
print(df.head(10))



#Now Validation for the IFSC_Code 
def check_ifsc(ifsc):
 bank_ifsc = ['SBIN', 'HDFC', 'ICIC', 'AXIS', 'PNB', 'YESB', 'KARB']
 return any(ifsc[:4] == x for x in bank_ifsc)

print(check_ifsc("SBIN014383"))

def is_valid_ifsc(ifsc):
        if not len(ifsc) == 11:
                return False
        
        if not str.isupper(ifsc):
                return False
        
        if not re.match(r"^[A-Z]{4}0[A-Z1-9]{6}$",ifsc):
                return False
        
        if not check_ifsc(ifsc):
               return False
        
        return True
        
df['Ifsc_Check'] = df['IFSC_Code'].apply(lambda x : "Correct" if is_valid_ifsc(x) else "In Correct")
print(df.head(10))

# ** Data Validation is Completed

# ** Data Summary ** 

valid_records = ((df['Acc_No_Check'] == 'Valid') & (df['Ifsc_Check'] == 'Correct')).sum()
invalid_records = ((df['Acc_No_Check'] == 'In Valid') & (df['Ifsc_Check'] == 'In Correct')).sum()
missing_records = Total_records - (valid_records + invalid_records)

print("valid Records :",valid_records)
print("In valid Records :",invalid_records)
print("Total Records :",Total_records)
print("Missing Records :",missing_records)

df_summary = pd.DataFrame({'Total Processed records ':[Total_records]
                           ,'Valid Records':[valid_records]
                           ,'In Valid records':[invalid_records]
                           ,'Missing records':[missing_records]})

print(df_summary.head())


#Convert the DataFrame into csv file
df.to_csv('Bank_Acc_Ifsc_Valid_Result.csv')
df_summary.to_csv('Bank_Acc_Ifsc_Valid_Summary.csv')

#** Data Visualization **

import matplotlib.pyplot as plt

# --- Pie Chart Visualization ---

# Labels and sizes
labels = ['Valid Records', 'Invalid Records', 'Missing Records']
sizes = [valid_records, invalid_records, missing_records]
colors = ['#4CAF50', '#FF5252', '#FFC107']  # green, red, yellow

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    colors=colors,
    textprops={'fontsize': 12, 'weight': 'bold'}
)
plt.title('Bank Account & IFSC Code Validation Summary', fontsize=14, weight='bold')
plt.axis('equal')  # Equal aspect ratio for a perfect circle
plt.show()
