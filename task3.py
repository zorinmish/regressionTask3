import pandas as pd
from sklearn.preprocessing import PolynomialFeatures 

#print("Loading weights of the model")
temp_df = pd.read_csv('weigths.csv')
w = temp_df["0"].to_numpy()
x0 = 0.000460648284843046
#print(w[0:5])

#print("Loading and preprocessing data...")
df = pd.read_csv('internship_hidden_test.csv')
df = df.drop("8", axis = 1)
polynomial_features = PolynomialFeatures(degree = 2, include_bias=True)
X = polynomial_features.fit_transform(df)
#print(X.shape)

#print("Calculation of target...")
y = X.dot(w) + x0

#print("Putting results in the file")
result = pd.DataFrame(y)
result.to_csv('predictionOfModel.csv')
#print("Done!")
