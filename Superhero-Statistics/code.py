# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path
#loading data
data = pd.read_csv(path)

#replacing data in Gender Column
data.Gender.replace('-','Agender',inplace=True)

#counting different types of gender
gender_count = data.Gender.value_counts()
#print(gender_count)

#plotting bar graph
gender_count.plot(kind='bar')
 


# --------------
#counting data of Alignment column
alignment = data.Alignment.value_counts()

#plotting pie chart
plt.pie(alignment)

#setting label
plt.xlabel('Character Alignment')



# --------------
#creating subset
sc_df = data[['Strength','Combat']] 

#taking covariance between two variables
sc_covariance = np.cov(sc_df.Strength,sc_df.Combat)[0][1]

#taking standard deviation of both variable
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()

#taking correlation of them
sc_pearson = sc_covariance/(sc_strength*sc_combat)

#creating subset
ic_df = data[['Intelligence','Combat']] 

#taking covariance between two variables
ic_covariance = np.cov(ic_df.Intelligence,ic_df.Combat)[0][1]

#taking standard deviation of both variable
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()

#taking correlation of them
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

#print both
print(sc_pearson)
print(ic_pearson)


# --------------
#Calculate quantile of Total
total_high = data.Total.quantile(q=0.99)
print(total_high)

#creating subset based on value of Total greater value than total_high
super_best = data[data.Total>total_high]

#taking names from super_best
super_best_names = list(super_best.Name)

#display names
print(super_best_names)


# --------------
#Creating subplots
fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3)

#plotting boxplot for Intelligence column
data.boxplot('Intelligence',ax=ax_1)
ax_1.set_title('Intelligence')

#plotting boxplot for Speed column
data.boxplot('Speed',ax=ax_2)
ax_2.set_title('Speed')

#plotting boxplot for Power column
data.boxplot('Power',ax=ax_3)
ax_3.set_title('Power')




