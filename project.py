import pandas as pd
import statistics 
import math

data = [60,61,65,63,98,99,90,95,91,96]

mean  =  statistics.mean(data)

devitions = []
for d in data:
    result =  d-mean  
    devitions.append(result)    

sqrdDeviation = []
for e in devitions:
    sqrdValue = e*e
    sqrdDeviation.append(sqrdValue)

sum = 0
for a in sqrdDeviation:
    sum = sum + a


length = len(data)
variance = sum/length

standardDaviation = math.sqrt(variance)
print(standardDaviation)

