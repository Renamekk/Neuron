# 🧠 Simple Neuron Trainer (by Renamekk)

A simple and lightweight neuron simulator written in Python. It allows training a single neuron to approximate a given input-output relationship using a basic error correction method. Currently works with one input and one output. Multi-neuron support is planned for future versions.

---

## 🚀 Getting Started

### 1. Installation

1. Clone or download this repository.
2. Make sure you have **Python 3.10+** installed.
3. Install all dependencies by running:

```
python main.py

```

### 2. Neuron Overview

The Neuron class provides the following features:

- Weight = The current weight of the neuron.
- Last Error = The last error calculated during training.
- Smoothing = A small factor to control weight adjustments.
- Calculate Output = Computes the neuron output for a given input.
- Train = Adjusts the neuron weight to minimize the error.
- Check Training Status = Determines if further training is required.

| Method                             | Description                                                 |
| ---------------------------------- | ----------------------------------------------------------- |
| neuron_calculate_value(input_data) | Returns the neuron's output for a given input.              |
| train(input, expected_result)      | Trains the neuron based on the input and expected output.   |
| train_result()                     | Checks if training should continue based on the last error. |
| get_weight()                       | Returns the current weight of the neuron.                   |
| get_last_error()                   | Returns the last error value.                               |
| get_smothing()                     | Returns the smoothing factor.                               |

### 3. Example Usage

#### 💻 Training a Neuron for Currency Conversion

```

neuron = Neuron()

input_data = 200        # Dollar
exspected_result = 170.42  # Euro
print(neuron.neuron_calculate_value(input_data))

iteration = 1

while neuron.train_result():
    neuron.train(input_data, exspected_result)
    iteration += 1

print('--- Successfully Trained ---')
print(neuron.get_weight())
print(neuron.neuron_calculate_value(input_data))

```

#### Output:

- Initial output before training.
- Final trained weight.
- Predicted output close to the expected result.

### 👤 Author

#### Developed by Renamekk

### 📝 License

#### This project is licensed under the [MIT License](LICENSE).

#### You are free to:

- Use the code for personal or commercial projects

- Modify it as you see fit

- Distribute your own versions

### However:

- Any modifications or forks are not affiliated with or endorsed by the original author. (Renamekk)
