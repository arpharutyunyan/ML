import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression 

class MyLinearRegression():

    def gradient_descent(self, x, y, iteration, learning_rate):
    # y = kx + b 
    # where X is the explanatory variable and Y is the dependent variable. The slope of the line is K, and B is the intercept (the value of y when x = 0

        k = b = 0
        n = len(x)

        for i in range(iteration):

            y_predicted = k*x + b
            cost_error = 1/n * sum([delta_y ** 2 for delta_y in (y - y_predicted)])    #  1/n  * sum[i=1 n] ((yi - (kxi + b))**2)
            dk = -(2/n) * sum(x * (y - y_predicted))
            db = -(2/n) * sum(y - y_predicted)

            k = k - learning_rate * dk
            b = b - learning_rate * db
            
            print(f"k = {k};    b = {b};    error = {cost_error}")
            # plt.plot(x, y_predicted)  



    def linearRegression_with_sklearn(self, x, y):
        # plt.plot(x, y, "bo")

        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)

        model = LinearRegression()
        z = model.fit(x,y)
        # plt.plot(x, y)

        k = model.intercept_
        b = model.coef_ 

        print(f"K is: {k};      B is: {b}")



if __name__ == "__main__":
    

    x = np.array([-10, -4, 2,6,4,5,8,2,4])
    y = np.array([2*i+5 for i in x])

    iteration = 3000
    learning_rate = 0.001

    lr = MyLinearRegression()
    lr.gradient_descent(x, y, iteration, learning_rate)

    lr.linearRegression_with_sklearn(x,y)