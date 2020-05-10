# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census = np.concatenate((data,new_record),axis=0)


# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()


# --------------
#Code starts here

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

#Length of each race
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
#index of minority_race
minority_race = np.argmin([len_0,len_1,len_2,len_3,len_4])



# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here

#making of high educated ppl dataset
high = census[census[:,1]>10]

#making of low educated ppl dataset
low = census[census[:,1]<=10]

#taking avg income of high educated ppl
avg_pay_high = high[:,7].mean(axis=0)

#taking avg income of low educated ppl
avg_pay_low = low[:,7].mean(axis=0)

#display 
print (avg_pay_high>avg_pay_low)


