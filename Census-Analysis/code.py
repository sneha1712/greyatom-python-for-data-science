# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(np.shape(data))
census=np.concatenate((data,new_record))
print(np.shape(census))

# --------------
#Code starts here

age=np.array(census[:,0])
print(age)

max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(round(age_mean,2))
age_std = np.std(age)
print(round(age_std,2))

print("So the Country seems to be YOUNG")

# --------------
#Code starts here

race_0 = census[census[:,2]==0]

race_1 = census[census[:,2]==1]

race_2 = census[census[:,2]==2]

race_3 = census[census[:,2]==3]

race_4 = census[census[:,2]==4]


len_0 = len(race_0)

len_1 = len(race_1)

len_2 = len(race_2)

len_3 = len(race_3)

len_4 = len(race_4)

lengths = [len_0,len_1,len_2,len_3,len_4]

minority_race = min(lengths)

minority_race = lengths.index(min(lengths))
print("Minority Race is " + str(minority_race))

# --------------
#Code starts here

senior_citizens = census[census[:,0]>60]

working_hours_sum = np.sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens)

avg_working_hours  = working_hours_sum/senior_citizens_len

print(round(avg_working_hours,2))
print("Yes,The govt. policy is followed")

# --------------
#Code starts here

high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(round(avg_pay_high,2))
print(round(avg_pay_low,2))

print("Better education leads to better pay is TRUE")















