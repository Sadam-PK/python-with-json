import json

with open('medicine.json') as f:
    data = json.load(f)
    root = data['medicines']
    add = {"name": "paracatamol", "price": 25, "id": 3}
    root.append(add)


def write_json(mydata):
    with open('medicine.json', 'w') as ff:
        json.dump(mydata, ff)


write_json(data)
