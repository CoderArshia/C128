import csv 

data1 = []
data2 = []

with open("dataset_1.csv","r") as f:
    csvreader = csv.reader(f)
    
    for row in csvreader:
        data1.append(row)

with open ("sorted.csv","r") as f:
    csvreader = csv.reader(f)

    for row in csvreader:
        data2.append(row)

headers1 = data1[0]
planetdata1 = data1[1:]

headers2 = data2[0]
planetdata2 = data2 [1:]

headers = headers1 + headers2
planet_data = []

for index,data_row in enumerate (planetdata1):
    planet_data.append(planetdata1[index]+planetdata2[index])

with open ("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)



