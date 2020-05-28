# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path,sep=',')

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
#print(banks)
print(banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)

for data_cols in banks.columns:
    banks[data_cols].fillna(banks[data_cols].mode()[0],inplace=True)


print(banks.isnull().sum())
#code ends here



# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc='mean')

print(avg_loan_amount)

# code ends here



# --------------
# code starts here


# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# code starts here

#convert loan amount term in terms of year and display
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
print(loan_term)

#checking number of big loan term and display
big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)


# code ends here


# --------------
# code starts here

#groupby dataframe by Loan_Status
loan_groupby = banks.groupby(['Loan_Status'])
print(loan_groupby)

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


