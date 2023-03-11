import matplotlib.pyplot as plt
import csv


with open('Humidity.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    
for i, row in enumerate(data, 1):
    row['entry_number'] = i
    
humidity_data = [str(row['humidity']) for row in data]

plt.plot(range(1, len(data) + 1), humidity_data)

plt.title('Humidity over Time')

plt.xlabel('Entry Number')

plt.ylabel('Humidity (%)')

plt.show()