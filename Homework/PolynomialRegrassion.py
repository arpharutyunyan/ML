import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures

class PolynomialRegression():

    def polynomialRegression_with_sklearn(self, x,y):
        poly_reg = PolynomialFeatures(degree=3)
        #print(x)
        print(y)
        x = x.reshape(-1, 1)
        #print(x)
        x_poly = poly_reg.fit_transform(x)
        print(x_poly)

        lr = LinearRegression()
        lr.fit(x_poly, y)

        # plt.plot(x,y, "bo")
        # plt.plot(x, lr.predict(x_poly))    


if __name__ == "__main__":
    

    x = np.arange(-10, 10)
    y = np.array([(i+5)**2 for i in x])

    pr = PolynomialRegression()
    pr.polynomialRegression_with_sklearn(x,y)