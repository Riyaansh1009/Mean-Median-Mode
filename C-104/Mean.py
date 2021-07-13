import csv 

with open('Data.csv', newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)
# print(data[0])
data.pop(0)
newData = []

for i in range(len(data)):
    n = data[i][2]
    newData.append(float(n))

quantity = len(newData)
total = 0
for x in newData:
    total += x
mean = total/quantity
print('mean is ',mean)
