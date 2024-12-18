import os
from collections import defaultdict
import time

startTime = time.time()
filePath = os.path.join(os.path.dirname(__file__), 'measurements.txt')

with open(filePath, 'r') as file:
    lines = file.readlines()

class Record:
    def __init__(self):
        self.minTemp = float('inf')
        self.sum = 0
        self.maxTemp = float('-inf')
        self.count = 0

result = defaultdict(Record)

for line in lines:
    values = line.split(';')
    station = values[0]
    temp = float(values[1])
    result[station].minTemp = min(result[station].minTemp, temp)
    result[station].maxTemp = max(result[station].maxTemp, temp)
    result[station].sum += temp
    result[station].count += 1

for station, record in result.items():
    record.avgTemp = format(((round(record.sum * 10)) / 10) / record.count, '.1f')
    # print(f"{station}={record.minTemp}/{record.avgTemp}/{record.maxTemp}")

result = sorted(result.items(), key=lambda x:x[0])
endTime = time.time()
for station, record in result:
    print(f"{station}={record.minTemp}/{record.avgTemp}/{record.maxTemp}")
print(f"Time taken: {endTime-startTime} seconds")
