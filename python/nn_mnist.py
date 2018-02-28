import os
import pickle

import numpy as np
from scipy.special import expit
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


test_file, train_file = 'mnist_test_10.csv', 'mnist_train_100.csv'
test_file, train_file = 'mnist_test.csv', 'mnist_train.csv'

network_file = 'mnist.pkl'


class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.i_nodes = input_nodes
        self.h_nodes = hidden_nodes
        self.o_nodes = output_nodes
        self.lr = learning_rate
        self.is_trained = False

        if os.path.exists('mnist.pkl'):
            with open(network_file, 'rb') as fh:
                network = pickle.load(fh)
            self.wih, self.who = network['wih'], network['who']
            self.is_trained = True
        else:
            self.wih = np.random.normal(
                0, pow(self.h_nodes, -0.5), (self.h_nodes, self.i_nodes)
            )
            self.who = np.random.normal(
                0, pow(self.o_nodes, -0.5), (self.o_nodes, self.h_nodes)
            )

        self.activation_func = lambda x: expit(x)

    def query(self, inputs):
        plt.show(inputs)
        inputs = np.array(inputs, ndmin=2).T

        print(inputs)
        h_inputs = np.dot(self.wih, inputs)
        print(h_inputs)
        h_outputs = self.activation_func(h_inputs)
        print(h_outputs)
        o_inputs = np.dot(self.who, h_outputs)
        print(o_inputs)
        o_outputs = self.activation_func(o_inputs)
        print(o_outputs)
        return o_outputs

    def train(self, inputs, targets):
        inputs = np.array(inputs, ndmin=2).T
        targets = np.array(targets, ndmin=2).T

        h_inputs = np.dot(self.wih, inputs)
        h_outputs = self.activation_func(h_inputs)

        o_inputs = np.dot(self.who, h_outputs)
        o_outputs = self.activation_func(o_inputs)

        o_errors = targets - o_outputs
        h_errors = np.dot(self.who.T, o_errors)
        self.who += self.lr * np.dot((o_errors * o_outputs * (1 - o_outputs)), np.transpose(h_outputs))
        self.wih += self.lr * np.dot((h_errors * h_outputs * (1 - h_outputs)), np.transpose(inputs))


# n = NueralNetwork(3, 3, 3, 0.3)
# print(n.query([0.4, -1.4, 1.1]))

# item = data[0].split(',')
# img_array = np.asfarray(item[1:]).reshape(28, 28)
# plt.imshow(img_array, cmap='Greys', interpolation='None')
# plt.show()

input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate = 0.001


n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)


with open(train_file) as fh:
    train_data = fh.readlines()

with open(test_file) as fh:
    test_data = fh.readlines()


def train(network):
    print('Training network...')
    for record in train_data:
        item = record.split(',')
        label = item[0]
        inputs = (np.asfarray(item[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(output_nodes) + 0.01
        targets[int(label)] = 0.99
        network.train(inputs, targets)
        # print(n.wih, n.who)


if not n.is_trained:
    train(n)


scorecard = []

for record in test_data:
    item = record.split(',')
    correct_label = int(item[0])

    inputs = (np.asfarray(item[1:]) / 255.0 * 0.99) + 0.01

    outputs = n.query(inputs)
    label = np.argmax(outputs)
    e
    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard_array = np.asarray(scorecard)
print("Performance = ", scorecard_array.sum() / scorecard_array.size)

network = {'wih': n.wih, 'who': n.who}

with open(network_file, 'wb') as fh:
    pickle.dump(network, fh)
