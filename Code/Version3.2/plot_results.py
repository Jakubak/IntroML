# plot_results.py

import matplotlib.pyplot as plt
import numpy as np

def plot_results_history(history,key_list):
    plt.figure()
    linemarker = ["r-","b-","k-","g-","c-"]
    epoch_array = np.arange(1,len(history[key_list[0]])+1)
    for count in range(len(key_list)):
        plt.plot(epoch_array,history[key_list[count]],linemarker[count],label=key_list[count])
    plt.xlabel("Epoch")
    plt.ylabel(",".join(key_list))
    plt.title(",".join(key_list))
    plt.legend(loc="upper left")

def plot_results_linear(model,Xtrain,Ytrain):
    # plot results in plane
    X0 = Xtrain[0,:]
    X0min = np.min(X0)
    X0max = np.max(X0)
    Xtest = np.reshape(np.array([X0min,X0max]),(1,2))
    Ytest_pred = model.predict(Xtest)
    # exact solution
    Xb = np.concatenate((Xtrain,np.ones(Ytrain.shape)),axis=0)
    wb = np.dot(np.dot(Ytrain,Xb.T),np.linalg.inv(np.dot(Xb,Xb.T)))
    Xtestb = np.concatenate((Xtest,np.ones((1,2))),axis=0)
    Yb = np.dot(wb,Xtestb)
    # plot regression results
    plt.figure()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Linear Regression")
    plt.plot(np.squeeze(Xtrain),np.squeeze(Ytrain),"bo",label="Training Points")
    plt.plot(np.squeeze(Xtest),np.squeeze(Ytest_pred),"r-",label="Model Prediction")
    plt.plot(np.squeeze(Xtest),np.squeeze(Yb),"k-",label="Normal Equation Prediction")
    plt.legend(loc = "upper left")

def plot_results_classification(train_data,model,nclass=2,**kwargs):
    if "validation_data" in kwargs:
        plot_results_data(train_data,nclass,validation_data=kwargs["validation_data"])
    else:
        plot_results_data(train_data,nclass)
    plot_results_heatmap(model,train_data[0])

def plot_results_data(train_data,nclass=2,**kwargs):
    # plot training data - loop over labels (0, 1) and points in dataset which have those labels
    Xtrain = train_data[0]
    Ytrain = train_data[1]
    plt.figure()
    symbol_train = ["ro","bo","go","co"]
    for count in range(nclass):
        idx_train = np.where(np.squeeze(np.absolute(Ytrain-count))<1e-10)
        strlabeltrain = "Y = " + str(count) + " train"
        plt.plot(np.squeeze(Xtrain[0,idx_train]),np.squeeze(Xtrain[1,idx_train]),symbol_train[count],label=strlabeltrain)
    if "validation_data" in kwargs:
        Xvalid = kwargs["validation_data"][0]
        Yvalid = kwargs["validation_data"][1]
        symbol_valid = ["r^","b^","g^","c^"]
        for count in range(nclass):
            idx_valid = np.where(np.squeeze(np.absolute(Yvalid-count))<1e-10)
            strlabelvalid = "Y = " + str(count) + " valid"
            plt.plot(np.squeeze(Xvalid[0,idx_valid]),np.squeeze(Xvalid[1,idx_valid]),symbol_valid[count],label=strlabelvalid)
    plt.xlabel("Feature 0")
    plt.ylabel("Feature 1")
    plt.legend(loc="upper left")
    plt.title("Data")

def plot_results_heatmap(model,Xtrain):
    # plot heat map of model results
    x0 = Xtrain[0,:]
    x1 = Xtrain[1,:]
    npoints = 100
    # create 1d grids in x0 and x1 directions
    x0lin = np.linspace(np.min(x0),np.max(x0),npoints)
    x1lin = np.linspace(np.min(x1),np.max(x1),npoints)
    # create 2d grads for x0 and x1 and reshape into 1d grids 
    x0grid,x1grid = np.meshgrid(x0lin,x1lin)
    x0reshape = np.reshape(x0grid,(1,npoints*npoints))
    x1reshape = np.reshape(x1grid,(1,npoints*npoints))
    # predict results (concatenated x0 and x1 1-d grids to create feature matrix
    yreshape = model.predict(np.concatenate((x0reshape,x1reshape),axis=0))
    # reshape results into 2d grid and plot heatmap
    heatmap = np.reshape(yreshape,(npoints,npoints))
    plt.pcolormesh(x0grid,x1grid,heatmap)
    plt.colorbar()
    plt.title("Data and Heatmap of Prediction Results")