import numpy as np


class NeuralNetwork:

    def __init__(self):
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        """
        Returns the sigmoid of the input

        :param x:
        :return:
        """
        return 1 / (1 + np.exp(-x))

    def derivative(self, x):
        """
        Returns the derivative of the input

        :param x:
        :return:
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            # siphon the training data via  the neuron
            output = self.think(training_inputs)

            # computing error rate for back-propagation
            error = training_outputs - output

            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":
    # initializing the neuron class
    neural_network = NeuralNetwork()

    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    # training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[0, 0, 0],
                                [0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1],
                                [0, 0, 0],
                                [0, 1, 0],
                                [1, 0, 0]])

    training_outputs = np.array([[0, 1, 1, 1, 1, 0, 0, 0]]).T

    # training taking place
    neural_network.train(training_inputs, training_outputs, 5000)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))

    print("Considering New Situation:", user_input_one, user_input_two, user_input_three)
    print("New Output data:")
    print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
    print("Wow, we did it!")
    print("Test")
