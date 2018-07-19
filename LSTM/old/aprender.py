# LSTM for international airline passengers problem with regression framing
import numpy
import matplotlib.pyplot as plt
import math
import sys
import MySQLdb

from numpy.testing import assert_allclose
from pandas import read_csv
from pandas import read_sql_query
from pandas import DataFrame
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dropout, Dense
from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from pytz import timezone
from datetime import datetime
est = timezone('UTC')

#definiciones db
sql_hn      = "127.0.0.1"
sql_p       = 3306
sql_uid     = "root"
sql_pwd     = "monaco997flow09182309paramus99129river"
sql_db      = "bb_ocr"

#callbacks
#TensorBoard = TensorBoard(log_dir='curvas', histogram_freq=0, write_graph=True, write_images=False)

#conexión db
conn = MySQLdb.connect(
            host    = sql_hn,
            port    = sql_p,
            user    = sql_uid,
            passwd  = sql_pwd,
            db      = sql_db
            )

# convert an array of values into a informacion matrix
def acomodar_informacion(informacion, pasado=1):
	informacion_x, informacion_y = [], []
	for i in range(len(informacion)-pasado-1):
		a = informacion[i:(i+pasado), 0]
		informacion_x.append(a)
		informacion_y.append(informacion[i + pasado, 0])
	return numpy.array(informacion_x), numpy.array(informacion_y)


# fix random seed for reproducibility
numpy.random.seed(7)

# load the informacion
#archivo                 = read_csv('dice_amplified/primeros_10_mil.csv', usecols=[0], engine='python')
archivo                 = read_sql_query("SELECT value FROM crawler ORDER BY round DESC LIMIT 0, 2000", conn)

informacion             = archivo.values
informacion             = informacion.astype('float32')

#normalización de la información
scaler                  = MinMaxScaler(feature_range=(0, 1))
informacion             = scaler.fit_transform(informacion)

#dividimos la información que vamos a usar para aprender y la que vamos a usar para evaluar
aprender_size           = int(len(informacion) * 0.5)
evaluar_size            = len(informacion) - aprender_size
aprender, evaluar       = informacion[0:aprender_size,:], informacion[aprender_size:len(informacion),:]


#consideramos [1] valores previos para realizar las predicciones
pasado = 100
aprender_x, aprender_y  = acomodar_informacion(aprender, pasado)
evaluar_x, evaluar_y    = acomodar_informacion(evaluar, pasado)

# reshape input to be [samples, time steps, features]
aprender_x              = numpy.reshape(aprender_x, (aprender_x.shape[0], 1, aprender_x.shape[1]))
evaluar_x               = numpy.reshape(evaluar_x, (evaluar_x.shape[0], 1, evaluar_x.shape[1]))


# load the model
model = load_model("modelos/model.h5")

vec_size = 100
unidades = 100
rondas = 50

#creacion de la red neuronal con LSTM
#model = Sequential()
#model.add(LSTM(100, input_shape=(1, pasado)))
#model.add(Dense(1))
#model.compile(loss='mean_squared_error', optimizer='adam')

model = Sequential()
model.add(LSTM(unidades, input_shape=(None, vec_size), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(unidades, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(unidades))
model.add(Dropout(0.2))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')


#salvamos a medida que aprende
filepath = "modelos/model.h5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(  aprender_x,
            aprender_y,
            epochs=rondas,
            batch_size=100,
            callbacks=callbacks_list,
            validation_data=(evaluar_x, evaluar_y),
            verbose=1
            )
            
# load the model
new_model = load_model("modelos/model.h5")
#assert_allclose(model.predict(aprender_x), new_model.predict(aprender_x), 1e-5)

# fit the model
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

new_model.fit(  aprender_x,
            aprender_y,
            epochs=rondas,
            batch_size=100,
            callbacks=callbacks_list,
            validation_data=(evaluar_x, evaluar_y),
            verbose=1
            )

#realizar predicciones
aprender_prediccion     = model.predict(aprender_x)
evaluar_prediccion      = model.predict(evaluar_x)

#inversion de las predicciones ¿para que?
aprender_prediccion     = scaler.inverse_transform(aprender_prediccion)
aprender_y              = scaler.inverse_transform([aprender_y])
evaluar_prediccion      = scaler.inverse_transform(evaluar_prediccion)
evaluar_y               = scaler.inverse_transform([evaluar_y])

#calculo del nivel de error usando [RMSE]
aprender_score = math.sqrt(mean_squared_error(aprender_y[0], aprender_prediccion[:,0]))
print('periodo aprender: %.2f RMSE' % (aprender_score))
evaluar_score = math.sqrt(mean_squared_error(evaluar_y[0], evaluar_prediccion[:,0]))
print('periodo evaluar: %.2f RMSE' % (evaluar_score))

#creacion de curvas
curvas_aprender = numpy.empty_like(informacion)
curvas_aprender[:, :] = numpy.nan
curvas_aprender[pasado:len(aprender_prediccion)+pasado, :] = aprender_prediccion

#creacion de curvas
curvas_evaluar = numpy.empty_like(informacion)
curvas_evaluar[:, :] = numpy.nan
curvas_evaluar[len(aprender_prediccion)+(pasado*2)+1:len(informacion)-1, :] = evaluar_prediccion

#creacion de curvas
plt.plot(scaler.inverse_transform(informacion))
plt.plot(curvas_aprender)
plt.plot(curvas_evaluar)
plt.show()