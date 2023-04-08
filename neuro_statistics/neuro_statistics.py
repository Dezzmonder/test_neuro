import Classes.neuron_class as n
import numpy as np
import datetime
import Classes.normalize as norm

# 1 мужской, 0 женский
# начальные данные до нормализации и деления на учебный/тестовый набор
data_start = [[35, 1, 120, 80, 220, 1], [45, 0, 130, 84, 260, 1], [60, 1, 140, 90, 190, 0], [55, 0, 145, 95, 220, 1],
              [50, 1, 130, 80, 240, 0], [65, 0, 150, 92, 280, 1], [40, 1, 120, 75, 200, 0], [55, 0, 135, 88, 240, 0],
              [50, 1, 140, 85, 250, 1], [70, 0, 155, 96, 290, 1], [45, 1, 140, 92, 230, 0], [50, 0, 135, 85, 190, 0],
              [55, 1, 130, 78, 220, 1], [60, 0, 150, 95, 280, 1], [40, 1, 125, 78, 200, 0], [65, 0, 155, 98, 250, 0],
              [50, 1, 140, 86, 240, 1], [55, 0, 130, 82, 210, 0], [70, 1, 150, 94, 300, 1], [35, 0, 120, 75, 180, 0]]
data_norm = norm.normalize(data_start)
data_test = []

truth_start = [[0], [1], [1], [1], [0], [1], [0], [1], [1], [1], [1], [0], [1], [1], [0], [1], [1], [0], [1], [0]]
truth_test = []
test_count = 7 #определяем количество тестовых данных
for i in range(test_count):
    truth_test.append(truth_start.pop(-1))  # убираем истинное значение для тестовых данных
    data_test.append(data_norm.pop(-1))  # выделяем данные для теста НС

data = np.array(data_norm)
truth = np.array(truth_start)
start = datetime.datetime.now()

network = n.NeuralNetwork(6, 3, 1)
outputs = network.train(data, truth, 2000 + 1)
print(f'потрачено времени: {datetime.datetime.now() - start}')

for i, c in zip(data_test, truth_test):
    temp = network.forward(i)
    str = f'{i}\nя думаю, что это:'
    if temp[0] > 0.5:
        str += f' болен'
    else:
        str += ' здоров'
    str += f'\nУверенность: {temp}\nВерный ответ {c}'
    print(str)
