import numpy as np
import math
data = np.array([[33.6,50,1],[26.6,30,0],[23.4,40,0],[43.1,67,0],[35.3,23,1],[35.9,67,1],[36.7,45,1],[25.7,46,0],[23.3,29,0],[31,56,1]])
bmi = []
age = []
sugar = []
for i in range(10):
    bmi.append(data[i][0])
    age.append(data[i][1])
    sugar.append(data[i][2])
d = []
given_bmi = 43.6
given_age = 40
k=3
for i in range(10):
    temp = ((given_bmi-bmi[i])**2 + (given_age-age[i])**2)
    d.append([i,math.sqrt(temp)])
d.sort(key=lambda x:x[1])
count1 = 0
count0 = 0
for i in range(k):
    temp = d[i][0]
    if(sugar[temp]==1):
        count1 = count1+1
    else:
        count0 = count0+1
if(count1>count0):
    print("Person with bmi 43.6 and age 40 Have sugar")
else:
    print("Have no sugar")