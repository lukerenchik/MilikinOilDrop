import numpy as np
import matplotlib.pyplot as plt
import math

#Declarations
errors_2 = []
errors_3 = []
errors_4 = []
errors_5 = []
errors_6 = []
errors_7 = []
errors_8 = []
errors_9 = []
errors_10 = []

#The Total Electrical Charge on Oil Droplets
qDrop1 = 1.113e-18
qDrop2 = 1.389e-18
qDrop3 = 6.376e-19
qDrop4 = 3.188e-19
qDrop5 = 3.183e-19
qDrop6 = 6.355e-19
qDrop7 = 2.031e-18


#Finding Elementary Charge with 2 Trials
q = 0
for i in np.arange(1e-19, 2e-19, 1e-23):
    error_2 = (qDrop1 % i) + (qDrop2 % i)
    errors_2.insert(q,error_2)
    q = q + 1

minNumTwoDrop = (min(errors_2))
minNumIndexTwo = errors_2.index(minNumTwoDrop)
elementaryChargeTwoDrop =  float("1" +"." + str(minNumIndexTwo))*10**-19

#Finding Elementary Charge with 3 Trials
q = 0
for i in np.arange(1e-19, 2e-19, 1e-23):
    error_3 = (qDrop1 % i) + (qDrop2 % i) + (qDrop3 % i)
    errors_3.insert(q,error_3)
    q = q + 1

minNumThreeDrop = (min(errors_3))
minNumIndexThree = errors_3.index(minNumThreeDrop)
elementaryChargeThreeDrop = float("1" +"." + str(minNumIndexThree))*10**-19

#Finding Elementary Charge with 4 Trials
q = 0
for i in np.arange(1e-19, 2e-19, 1e-23):
    error_4 = (qDrop1 % i) + (qDrop2 % i) + (qDrop3 % i) + (qDrop4 % i)
    errors_4.insert(q,error_4)
    q = q + 1

minNumFourDrop = (min(errors_4))
minNumIndexFour = errors_4.index(minNumFourDrop)
elementaryChargeFourDrop = float(("1" +"." + str(minNumIndexFour)))*10**-19

#Finding Elementary Charge with 5 Trials
q = 0
for i in np.arange(1e-19, 2e-19, 1e-23):
    error_5 = (qDrop1 % i) + (qDrop2 % i) + (qDrop3 % i) + (qDrop4 % i) + (qDrop5 % i)
    errors_5.insert(q, error_5)
    q = q + 1

minNumFiveDrop = (min(errors_5))
minNumIndexFive = errors_5.index(minNumFiveDrop)
elementaryChargeFiveDrop = float(("1" +"." + str(minNumIndexFive)))*10**-19

#Finding Elementary Charge with 6 Trials
q = 0
for i in np.arange(1e-19, 2e-19, 1e-23):
    error_6 = (qDrop1 % i) + (qDrop2 % i) + (qDrop3 % i) + (qDrop4 % i) + (qDrop5 % i) + (qDrop6 % i)
    errors_6.insert(q, error_6)
    q = q + 1

minNumSixDrop = (min(errors_6))
minNumIndexSix = errors_6.index(minNumSixDrop)
elementaryChargeSixDrop = float(("1" +"." + str(minNumIndexSix)))*10**-19

#Finding Elementary Charge with 6 Trials
q = 0
for i in np.arange(1e-19, 2e-19, 1e-23):
    error_7 = (qDrop1 % i) + (qDrop2 % i) + (qDrop3 % i) + (qDrop4 % i) + (qDrop5 % i) + (qDrop6 % i) + (qDrop7 % i)
    errors_7.insert(q, error_7)
    q = q + 1

minNumSevenDrop = (min(errors_7))
minNumIndexSeven = errors_7.index(minNumSevenDrop)
elementaryChargeSevenDrop = float(("1" +"." + str(minNumIndexSeven)))*10**-19

#Final Output
print("The calculated elementary charge of an electron with 2 trials is " + str(elementaryChargeTwoDrop))
print("The calculated elementary charge of an electron with 3 trials is " + str(elementaryChargeThreeDrop))
print("The calculated elementary charge of an electron with 4 trials is " + str(elementaryChargeFourDrop))
print("The calculated elementary charge of an electron with 5 trials is " + str(elementaryChargeFiveDrop))
print("The calculated elementary charge of an electron with 5 trials is " + str(elementaryChargeSixDrop))
print("The calculated elementary charge of an electron with 5 trials is " + str(elementaryChargeSevenDrop))
#Plotting the Data
x_val = [2, 3, 4, 5, 6, 7]
y_val = [elementaryChargeTwoDrop, elementaryChargeThreeDrop, elementaryChargeFourDrop, elementaryChargeFiveDrop, elementaryChargeSixDrop, elementaryChargeSevenDrop]
x_val = np.array(x_val)
y_val = np.array(y_val)
a, b = np.polyfit(x_val, y_val, 1)
plt.plot(x_val,a*x_val+b, label="Line of Best Fit", color="Black", linestyle="dashed")
plt.scatter(x_val, y_val, edgecolors="red",color='black', s=75)
plt.axhline(1.602e-19, color='orange', xmin=0, xmax=8, linestyle="dotted", label="Charge of Electron")
plt.xlabel("Number of Oil Drops Examined")
plt.ylabel("Coulombs (C) e-19")
plt.title("Calculated Elementary Charge of Electron")
plt.legend()
plt.show()

#Finding the Number of Charges in Each Oil Drop
NumChargeDrop1 = qDrop1 / elementaryChargeFiveDrop
NumChargeDrop2 = qDrop2 / elementaryChargeFiveDrop
NumChargeDrop3 = qDrop3 / elementaryChargeFiveDrop
NumChargeDrop4 = qDrop4 / elementaryChargeFiveDrop
NumChargeDrop5 = qDrop5 / elementaryChargeFiveDrop
NumChargeDrop6 = qDrop6 / elementaryChargeSixDrop
NumChargeDrop7 = qDrop7 / elementaryChargeSevenDrop

print(NumChargeDrop1)
print(NumChargeDrop2)
print(NumChargeDrop3)
print(NumChargeDrop4)
print(NumChargeDrop5)
print(NumChargeDrop6)
print(NumChargeDrop7)

#Plotting Number of Charges on Each Oil Drop
x_val_1 = [1, 2, 3, 4, 5, 6, 7]
y_val_1 = [NumChargeDrop1, NumChargeDrop2, NumChargeDrop3, NumChargeDrop4, NumChargeDrop5, NumChargeDrop6, NumChargeDrop7]
x_val_1 = np.array(x_val_1)
y_val_1 = np.array(y_val_1)
a, b = np.polyfit(x_val_1, y_val_1, 1)
plt.scatter(x_val_1, y_val_1, edgecolors="black",color='red', s=75)
plt.axhline(1, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(2, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(3, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(4, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(5, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(6, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(7, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(8, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(9, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(10, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(11, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(12, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(13, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.axhline(14, color='black', xmin=0, xmax=8, linestyle="solid", label="n=q/e")
plt.xlabel("Drop Number")
plt.ylabel("n = Q/e")
plt.title("Number of Electrons in Each Oil Drop")

plt.show()







