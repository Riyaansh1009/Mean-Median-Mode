import csv

with open('Data.csv', newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

newData = []
for i in range(len(data)):
    n = data[i][1]
    newData.append(float(n))

newData.sort()

length = len(newData)

if length%2==0:
    median1 = float(newData[length//2])
    median2 = float(newData[length//2 +1])
    finalMedian = (median1 + median2)/2
else:
    finalMedian = newData[length//2]

print("Median is ", finalMedian)


    

