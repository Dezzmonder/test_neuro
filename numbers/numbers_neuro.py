import numpy as np
import json
import datetime

import neuron_class as n
start = datetime.datetime.now()
network = n.NeuralNetwork(15, 30, 10)
with open('saves/data.json', 'r') as read:
    saves = json.load(read)
data = np.array(saves['data'])
truth = np.array(saves['truth'])
outputs = network.train(data, truth, 1000 + 1)

print(f'Потрачено времени: {datetime.datetime.now() - start}')

# for t, i in enumerate(data):
#     str = f'цифра {t}\n'
#     temp = network.forward(i)
#     str += f'я думаю, что это:{temp.index(max(temp))}\nУверенность: {max(temp)}\n'
#     print(str)
