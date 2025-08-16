class Neuron:
    def __init__(self):
        self.weight = 0.1
        self.last_error = 1.1
        self.smothing = 0.0000001

    def get_last_error(self):
        return self.last_error
    
    def get_smothing(self):
        return self.smothing
    
    def get_weight(self):
        return self.weight
    

    def neuron_calculate_value(self, input_data):
        return input_data * self.weight
    
    def train(self, input, exspected_result):
        result = input * self.weight

        self.last_error = exspected_result - result
        correction = self.last_error / result
        correction = correction * self.smothing

        self.weight += correction

    def train_result(self):
        if(self.last_error > self.smothing or self.last_error < -self.smothing):
            return True
        else:
            return False
        
neuron = Neuron()

input_data = 200 # Dollar
exspected_result = 170.42 # Euro
print(neuron.neuron_calculate_value(input_data))

iteration = 1

while (neuron.train_result()):
    neuron.train(input_data, exspected_result)

    iteration += 1


print('--- Successfully Trained ---')
print(neuron.get_weight())
print(neuron.neuron_calculate_value(input_data))