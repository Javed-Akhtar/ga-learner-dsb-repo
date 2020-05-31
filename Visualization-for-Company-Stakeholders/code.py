# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read data from path
data = pd.read_csv(path,sep=',')
#print(data.head(5))

#count Loan_Status and store in a variable
loan_status = data['Loan_Status'].value_counts()
#print(loan_status)

#plot bar chart  of loan status
loan_status.plot(kind='bar')
#Code starts here


# --------------
#grouping dataframe by Property_Area and Loan_Status
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
#print(property_and_loan)

#using size and unstack attribute of property_and_loan to form properly
property_and_loan = property_and_loan.size().unstack()
#print(property_and_loan)

#Plotting bar chart
property_and_loan.plot(kind='bar')

#Set the labels
plt.xlabel('Property Area')
plt.ylabel('Loan Status')

#Rotating xlabel
plt.xticks(rotation=45)


# --------------
#Group dataframe by Education and Loan_Status
education_and_loan = data.groupby(['Education','Loan_Status'])

#use size and unstack attribute to modify groupby data
education_and_loan = education_and_loan.size().unstack()
print(education_and_loan)

#Plot a Stacked bar chart
education_and_loan.plot(kind='bar',stacked=True)

#Set labels 
plt.xlabel('Education Status')
plt.ylabel('Loan Status')

#Rotating labels
plt.xticks(rotation=45)



# --------------
#Creating subset dataframe where Graduation is in Eduacation  
graduate = data[data['Education']=='Graduate']
#print(graduate)

#Creating subset dataframe where Not Graduation is in Eduacation
not_graduate = data[data['Education']=='Not Graduate']
#print(not_graduate)

#Plotting a density plot of graduates with respect of LoanAmount
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting a density plot of not graduates with respect of LoanAmount
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#For automatic legend display
plt.legend()


# --------------
#Create a subplot format of 3*1
fig , (ax_1,ax_2,ax_3) = plt.subplots(nrows = 3, ncols = 1)

#Scatter Plot between ApplicantsIncome and LoanAmount 
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set_title('Applicant Income')
#data['CoapplicantIncome','LoanAmount'].plot(kind='Scatter',ax=ax_1)
#Scatter Plot between CoapplicantIncome and LoanAmount
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

#Creating a new column which is sum of ApplicantIncome and CoapplicantIncome
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Scatter Plot between ToatalIncome and LoanAmount
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set_title('Total Income')


