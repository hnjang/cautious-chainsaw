#!/usr/bin/python3

import sys
import csv
import json
from pprint import pprint

with open('input.csv') as csvfile:
    in_data = list(zip(*csv.reader(csvfile)))
in_data = in_data[1:]

data = []
for d in in_data:
    s = {'name': d[0], 'score': int(d[1]), 'city': d[2]}
    data.append(s)

with open('students.json','w') as out_f:
    json_d = json.dumps(data, indent=4)
    out_f.write(json_d)

print('Done.')

