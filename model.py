from pickle import dump,load
from pandas import read_csv
A = read_csv("50_Startups.csv")
X = A[["RND","MKT"]]
Y = A[["PROFIT"]]
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model = lr.fit(X,Y)
dump(model,open("model.pkl","wb"))