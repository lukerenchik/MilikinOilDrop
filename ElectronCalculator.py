import numpy as np

errors = []
q=0


#The Total Electrical Charge on Oil Droplets
qDrop1 = 1.113e-18
qDrop2 = 1.389e-18
qDrop3 = 6.376e-19
qDrop4 = 3.188e-19

#Loop to Index the Errors of the Electrical Charge
for i in np.arange(1e-19, 2e-19, 1e-22):
    error = (qDrop1 % i) + (qDrop2 % i) + (qDrop3 % i) + (qDrop4 % i)
    errors.insert(q,error)
    q = q + 1

#Determining the Value with the Least Error
minNum = (min(errors))
minNumIndex = errors.index(minNum)

#Testing Statements
#print(errors)
#print(minNum)
#print(minNumIndex)

print("The elementary charge of an electron is 1." + str(minNumIndex) + "e-19")