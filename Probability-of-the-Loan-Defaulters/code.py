# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
#loading data
df = pd.read_csv(path)

#calculating probability of fico credit score is grater that 700
p_a = len(df.fico[df.fico>700])/len(df.fico)
print(p_a)

#calculating probability of perpose is debt_consolation
p_b = len(df.purpose[df.purpose=='debt_consolidation'])/len(df.purpose)
print(p_b)

#creating subset having purpose of debt_consolidation
df1 = df[df.purpose=='debt_consolidation']
#print(df1)

#calculating P(B|A)
p_a_b = (len(df1[df1.fico>700])/len(df))/p_a
p_b_a = (len(df1[df1.fico>700])/len(df))/p_b
#print(p_a_b)
#print(p_b_a)

#checking the result
result = p_b_a == p_a
print(result)

# code ends here


# --------------
# code starts here
#calculate probability for having paid.back.loan == Yes
prob_lp = len(df[df['paid.back.loan']=='Yes'])/len(df)
print(prob_lp)

#calculate probability for having credit.plocy == Yes
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df)
print(prob_cs)

#creating subset 
new_df = df[df['paid.back.loan']=='Yes']
#print(new_df)

#calculating P(A|B)
prob_pd_cs = (len(new_df[new_df['credit.policy']=='Yes'])/len(df))/prob_lp
print(prob_pd_cs)

#calculating conditional probability i.e. P(B|A)
bayes = prob_pd_cs*prob_lp/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here
#plot bar graph
df.purpose.value_counts(normalize=True).plot(kind='bar')
#creating subset
df1 = df[df['paid.back.loan']=='No']
#creating bar graph
df1.purpose.value_counts(normalize=True).plot(kind='bar')

plt.show()
# code ends here


# --------------
# code starts here
#calculate median of installment
inst_median = df.installment.median()
print(inst_median)

#calculate mean of installment
inst_mean = df.installment.mean()
print(inst_mean)

#plot histogram for installment
plt.hist(df['installment'])
plt.axvline(inst_mean,color='red')
plt.axvline(inst_median,color='green')
plt.show()

#plot histogram for log annual income
plt.hist(df['log.annual.inc'])
plt.axvline(df['log.annual.inc'].mean(),color='red')
plt.axvline(df['log.annual.inc'].median(),color='green')
plt.show()

# code ends here


