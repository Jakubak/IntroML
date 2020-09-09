# driver_linearregression_logcosh.py
# Run in IntroML/Code/Version1.2

import LRegression
import matplotlib.pyplot as plt
import numpy as np
import Optimizer
import plot_results

# (1) Set up data
m = 1000
X = np.random.rand(1,m)
Y = 0.5*X + 0.25
Y = Y + 0.1*np.random.randn(m)
# (2) Define model
model = LRegression.LRegression(1,"linear")
# (3) Compile model - use logcosh loss function
optimizer = Optimizer.GradientDescent(0.5)
model.compile("logcosh",optimizer)
# (4) Train model
epochs = 50
history = model.fit(X,Y,epochs)
# (5) Results
# plot loss and accuracy
plot_results.plot_results_history(history,["loss"])
plot_results.plot_results_history(history,["accuracy"])
# plot results
plot_results.plot_results_linear(model,X,Y)
plt.show()