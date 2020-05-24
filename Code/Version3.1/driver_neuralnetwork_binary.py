# driver_neuralnetwork_binary.py

import NeuralNetwork
import example_classification
import matplotlib.pyplot as plt
import numpy as np
import Optimizer
import plot_results
import time

# (1) Set up data
nfeature = 2
m = 2000
case = "quadratic"
nclass = 2
X,Y = example_classification.example(nfeature,m,case,nclass)
# (2) Define model
model = NeuralNetwork.NeuralNetwork(nfeature)
model.add_layer(11,"tanh")
model.add_layer(8,"tanh")
model.add_layer(4,"tanh")
model.add_layer(1,"sigmoid")
# (3) Compile model and print summary
optimizer = {"method": "Momentum", "learning_rate": 0.1, "beta": 0.9}
model.compile("binarycrossentropy",optimizer)
model.summary()
# (4) Train model
epochs = 20
time_start = time.time()
history = model.train(X,Y,epochs,batchsize=64)
time_end = time.time()
print("Train time: {}".format(time_end - time_start))
# (5) Results
# plot loss and accuracy and heatmap in x0-x1 plane
plot_results.plot_results_history(history,["loss"])
plot_results.plot_results_history(history,["accuracy"])
plot_results.plot_results_classification((X,Y),model,nclass)
plt.show()