# modificaciones recomendadas por ravikiran

# el mecanismo devuelve valores que varian del 5 al 6.
# los valores cercanos al 6 suelen ser más seguros,
# sin embargo, el verdadero indicador es si el valor asciende o decae en relación al valor previo.
# si el valor anda en en rangos de 6, y se desplaza hacia el 5, es recomendable no hacer nada,
# a la inversa, cuando anda en rangos de 5 y avanza hacia el 6, es recomendable posicionarse.
# las unidades de LSTM suben el valor de prediccion (ynew) cuando consideran que la chance subio.
# del mismo modo, el valor disminuye, cuando la probabilidad desciende.

# addendum: la variación parece ser relevancia, del mismo modo que el número.
# addendum: quizás sería bueno hacer <ynew_previo - ynew ahora> para que calcule la diferencia.

# se subio el sample
# se subio el lookback
# se salva el modelo de mayor performance

# se añade shuffle = false
# preservacion de información previa
# binario, siempre devuelve zero, lol




import numpy
import matplotlib.pyplot as plt
import math
import sys
import time
import MySQLdb

from pandas import read_csv
from pandas import read_sql_query
from pandas import DataFrame

from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
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

#conexión db
conn = MySQLdb.connect(
            host    = sql_hn,
            port    = sql_p,
            user    = sql_uid,
            passwd  = sql_pwd,
            db      = sql_db
            )

# convert an array of values into a informacion matrix
def acomodar_informacion(informacion, lookback=1):
	informacion_x, informacion_y = [], []
	for i in range(len(informacion)-lookback-1):
		a = informacion[i:(i+lookback), 0]
		informacion_x.append(a)
		informacion_y.append(informacion[i + lookback, 0])
	return numpy.array(informacion_x), numpy.array(informacion_y)

def imprimir(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()

# fix random seed for reproducibility
numpy.random.seed(7)

#variables
sample                  = 500042
verbose                 = 1
epochs                  = 1
ronda                   = 1000
lookback                = 1020

# load the informacion
archivo                 = read_sql_query("SELECT if(value >= 2, 1, 0) FROM ( SELECT * FROM crawler ORDER BY round DESC LIMIT %d) sub ORDER BY round ASC" % sample, conn)
informacion             = archivo.values
informacion             = informacion.astype('float32')

#normalización de la información
scaler                  = MinMaxScaler(feature_range=(0, 1))

#dividimos la información
aprender_size           = int(len(informacion) * 0.5)
evaluar_size            = len(informacion) - aprender_size
aprender, evaluar       = informacion[0:aprender_size,:], informacion[aprender_size:len(informacion),:]


#acomodamos la informacion
aprender_x, aprender_y  = acomodar_informacion(aprender, lookback)
evaluar_x, evaluar_y    = acomodar_informacion(evaluar, lookback)

#reshape
aprender_x              = numpy.reshape(aprender_x, (aprender_x.shape[0], 1, aprender_x.shape[1]))
evaluar_x               = numpy.reshape(evaluar_x, (evaluar_x.shape[0], 1, evaluar_x.shape[1]))

#definimos el callback
acceso          = "modelos/model.h5"
checkpoint      = ModelCheckpoint(acceso, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list  = [checkpoint]

#creacion de la red con LSTM
model = Sequential()
model.add(LSTM(32, batch_input_shape=(ronda, 1, lookback), return_sequences=True, stateful=True))
#model.add(LSTM(100, input_shape=(1, lookback), return_sequences=True, stateful=True))
model.add(LSTM(16, input_shape=(1, lookback)))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
            )


for i in range(epochs):
            
    model.fit(  aprender_x,
                aprender_y,
                epochs=1,
                batch_size=ronda,
                #callbacks=callbacks_list,
                validation_data=(evaluar_x, evaluar_y),
                verbose=verbose,
                shuffle=False
                )
            
    model.reset_states()

    
    
# re-define the batch size
ronda = 1

#creacion de la red con LSTM
new_model = Sequential()
new_model.add(LSTM(32, batch_input_shape=(ronda, 1, lookback), return_sequences=True, stateful=True))
new_model.add(LSTM(16, input_shape=(1, lookback)))
new_model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))


# copy weights
pesos_previos = model.get_weights()
new_model.set_weights(pesos_previos)

# compile model
model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
            )


# eliminamos el modelo creado
#del model 

#volcar la informacion            
#for i in range(len(aprender_x)):
	#print("causa=%s, consecuencia=%s" % (aprender_x[i], aprender_y[i]))
    

# recuperamos el modelo de mayor presición
#model = load_model('modelos/model.h5')

    
print("*******************  PREDICCIONES  *******************")

replica_xnew = None

while True:

    #pedimos la informacion
    archivo_xnew         = read_sql_query("SELECT if(value >= 2, 1, 0) FROM crawler ORDER BY round DESC LIMIT 0, %d" % lookback, conn)
    informacion_xnew     = archivo_xnew.values
    informacion_xnew     = informacion_xnew.astype('float32')
    
    #limpiamos la cache
    conn.commit()
    
    #acomodamos el array para que se vea del mismo modo
    informacion_xnew = numpy.dstack(informacion_xnew)
    
    if  ((informacion_xnew != replica_xnew).any() or replica_xnew is None) :
    
        replica_xnew = informacion_xnew

        #realizar prediccion
        ynew = new_model.predict_classes(informacion_xnew, batch_size = ronda, verbose=1)
        
        new_model.reset_states()
        
        #volcar la informacion
        for i in range(len(informacion_xnew)):
            imprimir("\n")
            imprimir("causa=%s, prediccion=%s" % (informacion_xnew[i], ynew[i]))
            
            