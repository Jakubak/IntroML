# driver_neuralnetwork_mnist.py

import load_spam
import NeuralNetwork
import numpy as np
import matplotlib.pyplot as plt
import metrics
import plot_results
import text_results
import time

# (1) Set up data
ntrain = 5000
nvalid = 500
Xtrain,Ytrain,Xvalid,Yvalid,Xtrain_raw,Xvalid_raw = load_spam.load_spam(ntrain,nvalid)
# (2) Define model
nfeature = Xtrain.shape[0]
np.random.seed(10)
model = NeuralNetwork.NeuralNetwork(nfeature)
model.add_layer(200,"tanh")
model.add_layer(50,"tanh")
model.add_layer(1,"sigmoid")
# (3) Compile model
optimizer = {"method": "Adam", "learning_rate": 0.02, "beta1": 0.9, "beta2": 0.999, "epsilon": 1e-7}
model.compile("binarycrossentropy",optimizer)
model.summary()
# (4) Train model
epochs = 20
time_start = time.time()
history = model.fit(Xtrain,Ytrain,epochs,batch_size=ntrain,validation_data=(Xvalid,Yvalid))
time_end = time.time()
# (5) Predictions and plotting
# confusiont matrix
Yvalid_pred = model.predict(Xvalid)
metrics.confusion_matrix(Yvalid,Yvalid_pred,2)
f1score,precision,recall = metrics.f1score(Yvalid,Yvalid_pred)
print("F1Score: {} - Precision: {} - Recall: {}".format(f1score,precision,recall))
text_results.text_results(Yvalid,Yvalid_pred,Xvalid_raw)
# plot loss and accuracy
plot_results.plot_results_history(history,["loss","valid_loss"])
plot_results.plot_results_history(history,["accuracy","valid_accuracy"])
plt.show()