from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#here first we have made the 200 sample with one input & one output feature data set for linear regression using sklearn library make_regression
X,y = make_regression(n_samples=200,n_features=1,n_informative=1,n_targets=1,noise=20,random_state=13)  

#we have plot our data to see whether it's linear or not 
plt.scatter(X,y) 

# We split our data in to train & test 
X2_train,X2_test,y2_train,y2_test = train_test_split(X,y,test_size=0.2,random_state=43) 

# check our shape of train and test data 
print(X2_train.shape)
print(X2_test.shape)
print(y2_train.shape)
print(y2_test.shape)

# And finaaly this is our Class for simple Linear regression I have named it --meraLR--
class meraLR:
    
    def __init__(self):
        self.m=None
        self.b=None
    
    def fit(self,X2_train,y2_train):
        x_mean = X2_train.mean()
        y_mean = y2_train.mean()
        c=0
        d=0
        for i in zip(X2_train,y2_train):
            c = c + ((i[0] - x_mean)*(i[1] - y_mean)) 
            d = d + (i[0] - x_mean)**2
        self.m = c/d
        self.b = y_mean  - self.m*x_mean
        return print(self.m,self.b) 
    
    def predict(self,X2_test):
        return self.m*X2_test + self.b
    
    def coefficent(self):
        return print(self.m)
    
    def intercept(self):
        return print(self.b)

# Creating object.
lre = meraLR() 

# Calling fit function to fit the model on X_train & y_train 
lre.fit(X2_train,y2_train) 

# Calling predict function on our X_test to preict using model
y_pr = lre.predict(X2_test)

# Checking value of slope (m) model predicted..
lre.coefficent

# Checking value of intercept (b) model predicted..
lre.intercept












