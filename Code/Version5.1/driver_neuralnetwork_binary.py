# driver_neuralnetwork_binary.py

import NeuralNetwork
import example_classification
import matplotlib.pyplot as plt
import metrics
import numpy as np
import Optimizer
import plot_results
import time

# (1) Set up data
nfeature = 2
m = 1000
case = "quadratic"
nclass = 2
noise = True
np.random.seed(10)
validperc = 0.2
Xtrain,Ytrain,Xvalid,Yvalid = example_classification.example(nfeature,m,case,nclass,noise,validperc)
# (2) Define model
np.random.seed(100)
lamb = 0.0
model = NeuralNetwork.NeuralNetwork(nfeature)
model.add_layer(15,"tanh",lamb)
model.add_layer(11,"tanh",lamb)
model.add_layer(8,"tanh",lamb)
model.add_layer(4,"tanh",lamb)
model.add_layer(1,"sigmoid",lamb)
# (3) Compile model and print summary
optimizer = Optimizer.Momentum(0.3,0.9)
model.compile("binarycrossentropy",optimizer)
model.summary()
# (4) Train model
epochs = 300
time_start = time.time()
history = model.fit(Xtrain,Ytrain,epochs,batch_size=1000,validation_data=(Xvalid,Yvalid))
time_end = time.time()
print("Train time: {}".format(time_end - time_start))
# (5) Results
# f1score
Yvalid_pred = model.predict(Xvalid)
f1score,precision,recall=metrics.f1score(Yvalid,Yvalid_pred)
print("For validation data: F1Score: {} - Precision: {} - Recall: {}".format(f1score,precision,recall))
# confusion matrix
metrics.confusion_matrix(Yvalid,Yvalid_pred,nclass)
# plot loss and accuracy and heatmap in x0-x1 plane
plot_results.plot_results_history(history,["loss","valid_loss"])
plot_results.plot_results_history(history,["accuracy","valid_accuracy"])
plot_results.plot_results_classification((Xtrain,Ytrain),model,nclass,validation_data=(Xvalid,Yvalid))
plt.show()