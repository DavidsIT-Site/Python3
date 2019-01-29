# Reading and writing JSON data
import json

data = {
    'Symbol': 'AA',
    'Price': '39.48',
    'Change': '-.18'
}
json_str = json.dumps(data)
print(data)
print(json_str)
data_j2d = json.loads(json_str)

with open('ch6_2.json', 'w') as f:
    json.dump(data, f)

with open('ch6_2.json', 'r') as f:
    data_readin = json.load(f)

print(data_readin)


#doesn't work
#json link bad