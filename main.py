import json


def write_json(data, filename="medicine.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


with open('medicine.json') as ff:
    data = json.load(ff)
    temp = data['medicines']
    y = {"name": "panadol", "price": 25, "id": 3}
    temp.append(y)

write_json(data)
