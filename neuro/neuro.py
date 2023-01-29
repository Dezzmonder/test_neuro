import json

with open('num.json', "r") as read:
    data = json.load(read)
num = data['matrix']

with open("weights.json", "r") as read:
    data2 = json.load(read)
weights = data2

inp = {}
for i in range(5):
    for c in range(5):
        inp[(c, i)] = 0
for i in num:
    inp[tuple(i)] = 1


class Neuron:
    def __init__(self, n):
        self.rez = 0
        self.weight = weights[f'neu{n}']
        for i in inp:
            self.rez += inp[i]*self.weight[f'{i}']

    def answer(self):
        return f'{self.rez} = {n}'


st = []
for n in range(10):
    brain = Neuron(n)
    st.append(brain.answer())
st.sort()
for i in st:
    print(i)
