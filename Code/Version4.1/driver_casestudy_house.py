# driver_casestudy_houseprice.py

import LRegression
import matplotlib.pyplot as plt
import numpy as np
import Optimizer
import plot_results
import load_house

# (1) Set up data
ntrain_pct = 0.8
transform = True
standardizeX = True
standardizeY = True
Xtrain,Ytrain,Xvalid,Yvalid = load_house.load_house(ntrain_pct,transform,standardizeX,standardizeY)
# (2) Define model
nfeature = Xtrain.shape[0]
np.random.seed(10)
lamb = 0.0001
model = LRegression.LRegression(nfeature,"linear",lamb)
# (3) Compile model
optimizer = Optimizer.GradientDescent(0.5)
model.compile("meansquarederror",optimizer)
# (4) Train model
epochs = 50
history = model.fit(Xtrain,Ytrain,epochs,validation_data=(Xvalid,Yvalid))
# (5) Predictions and plotting
# plot loss and accuracy
plot_results.plot_results_history(history,["loss","valid_loss"])
plot_results.plot_results_history(history,["accuracy","valid_accuracy"])
plt.show()
