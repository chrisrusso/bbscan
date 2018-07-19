# example of training a final classification model
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import MinMaxScaler

# generate 2d classification dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=1, random_state=1)
#scalar = MinMaxScaler()
#scalar.fit(X)
#X = scalar.transform(X)

for i in range(len(X)):
	print("variable=%s, rango=%s" % (X[i], y[i]))

# define and fit the final model
model = Sequential()
model.add(Dense(4, input_dim=1, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X, y, epochs=200, verbose=0)


# new instances where we do not know the answer
Xnew, _ = make_blobs(n_samples=3, centers=2, n_features=1, random_state=1)
#Xnew = scalar.transform(Xnew)

# make a prediction
ynew = model.predict(Xnew)

# show the inputs and predicted outputs
for i in range(len(Xnew)):
	print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
