import json

with open('num.json', "r") as read:
    data = json.load(read)
num = data['matrix']

with open("weights.json", "r") as read:
    data2 = json.load(read)
weights = data2


right =
wrong =

for i in num:
    we = weights[f'neu{right}'][f"{tuple(i)}"]
    weights[f'neu{right}'][f"{tuple(i)}"] += 0.15
for i in num:
    we = weights[f'neu{wrong}'][f"{tuple(i)}"]
    weights[f'neu{wrong}'][f"{tuple(i)}"] -= 0.15

data2 = weights

with open("weights.json", "w") as write:
    json.dump(data2, write, indent=0)
