import numpy as np


class Neuron:
    def __init__(self, inp_size):
        self.weights = np.random.randn(inp_size)
        self.bias = np.random.randn()

    def forward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return self.sigmoid(total)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def der_sigmoid(self, x):
        return x * (1 - x)


class NeuralNetwork:
    def __init__(self, inp_size, hidden_size, out_size):
        self.hidden_layer = []
        for i in range(hidden_size):
            self.hidden_layer.append(Neuron(inp_size))
        self.out_layer = []
        for i in range(out_size):
            self.out_layer.append(Neuron(hidden_size))

    def forward(self, inputs):
        hidden_out = []
        for n in self.hidden_layer:
            hidden_out.append(n.forward(inputs))
        out_out = []
        for n in self.out_layer:
            out_out.append(n.forward(hidden_out))
        return out_out

    def train(self, data, truth, epochs, learning_rate=0.3):
        for epoch in range(epochs):
            for inputs, label in zip(data, truth):
                # Прямое распространение
                hidden_out = [neuron.forward(inputs) for neuron in self.hidden_layer]
                out = [neuron.forward(hidden_out) for neuron in self.out_layer]
                # Вычисление ошибки
                out_error = []
                for i in range(len(out)):
                    out_error.append(label[i] - out[i])
                hidden_error = []
                for i in range(len(self.hidden_layer)):
                    for j in range(len(out_error)):
                        hidden_error.append(sum([out_error[j] * self.out_layer[j].weights[i]]))
                # Обновление весов
                for i in range(len(self.out_layer)):
                    for j in range(len(self.hidden_layer)):
                        delta = out_error[i] * self.out_layer[i].der_sigmoid(out[i])
                        self.out_layer[i].weights[j] += learning_rate * delta * hidden_out[j]
                        self.out_layer[i].bias += learning_rate * delta
                for i in range(len(self.hidden_layer)):
                    for j in range(len(inputs)):
                        delta = hidden_error[i] * self.hidden_layer[i].der_sigmoid(hidden_out[i])
                        self.hidden_layer[i].weights[j] += learning_rate * delta * inputs[j]
                        self.hidden_layer[i].bias += learning_rate * delta

            # Выводим потери на каждой эпохе
            if epoch % 100 == 0:
                loss = []
                for i in range(len(data)):
                    loss.append(np.square(truth[i] - self.forward(data[i])).mean())
                loss = sum(loss)
                print(f"Epoch {epoch}: Loss = {loss:.4f}")

# # Определяем входные данные и целевые значения
# data = np.array([[0, 0]])
# truth = np.array([[0]])
# # Создаем экземпляр нейронной сети
# network = NeuralNetwork(2, 2, 1)
# # Тренируем нейронную сеть
# network.train(data, truth, epochs=2000, learning_rate=0.3)
# # Проверяем результаты
# for inputs in data:
#     print(f"{inputs} -> {network.forward(inputs)}")
