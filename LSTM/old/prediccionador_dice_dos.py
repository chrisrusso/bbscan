# primera versión del prediccionador.
# cuando da un valor a 2, suele, con mayor frecuencia, ser un valor superior al 2.
# es necesario esperar mucho porque en verdad no dice 2 con mucha frecuencia... paciencia.
# los demás números no son de fiar.

#Raw sample:

#causa=[[1.5  2.01 8.1  1.52 2.13]], prediccion=[1.370174]
#causa=[[18.98  1.5   2.01  8.1   1.52]], prediccion=[1.7986432]
#causa=[[ 1.23 18.98  1.5   2.01  8.1 ]], prediccion=[1.9784373]
#causa=[[ 1.96  1.23 18.98  1.5   2.01]], prediccion=[1.4600116]
#causa=[[ 1.05  1.96  1.23 18.98  1.5 ]], prediccion=[1.7712449]
#causa=[[ 1.49  1.05  1.96  1.23 18.98]], prediccion=[1.769548]
#causa=[[1.03 1.49 1.05 1.96 1.23]], prediccion=[0.85954267]
#causa=[[1.81 1.03 1.49 1.05 1.96]], prediccion=[0.91789836]
#causa=[[3.95 1.81 1.03 1.49 1.05]], prediccion=[1.0807997]
#causa=[[1.36 3.95 1.81 1.03 1.49]], prediccion=[1.0908893]
#causa=[[3.43 1.36 3.95 1.81 1.03]], prediccion=[1.2239832]
#causa=[[1.19 3.43 1.36 3.95 1.81]], prediccion=[1.3040123]
#causa=[[1.16 1.19 3.43 1.36 3.95]], prediccion=[1.2262247]
#causa=[[1.11 1.16 1.19 3.43 1.36]], prediccion=[1.0158607]
#causa=[[1.23 1.11 1.16 1.19 3.43]], prediccion=[1.0167187]
#causa=[[2.43 1.23 1.11 1.16 1.19]], prediccion=[0.88712996]
#causa=[[1.82 2.43 1.23 1.11 1.16]], prediccion=[0.937869]
#causa=[[1.5  1.82 2.43 1.23 1.11]], prediccion=[0.95383847]
#causa=[[1.12 1.5  1.82 2.43 1.23]], prediccion=[0.98346585]
#causa=[[1.63 1.12 1.5  1.82 2.43]], prediccion=[1.0429902]
#causa=[[5.13 1.63 1.12 1.5  1.82]], prediccion=[1.2332774]
#causa=[[1.56 5.13 1.63 1.12 1.5 ]], prediccion=[1.1890147]
#causa=[[1.05 1.56 5.13 1.63 1.12]], prediccion=[1.1043061]
#causa=[[15.06  1.05  1.56  5.13  1.63]], prediccion=[1.6830447]
#causa=[[ 1.3  15.06  1.05  1.56  5.13]], prediccion=[1.7937119]
#causa=[[ 2.55  1.3  15.06  1.05  1.56]], prediccion=[1.4364703]
#causa=[[30.53  2.55  1.3  15.06  1.05]], prediccion=[1.8309817]
#causa=[[ 8.08 30.53  2.55  1.3  15.06]], prediccion=[2.1860821]
#causa=[[32.68  8.08 30.53  2.55  1.3 ]], prediccion=[1.8121487]
#causa=[[ 6.7  32.68  8.08 30.53  2.55]], prediccion=[2.2578003]
#causa=[[ 1.2   6.7  32.68  8.08 30.53]], prediccion=[2.141759]
#causa=[[ 1.23  1.2   6.7  32.68  8.08]], prediccion=[2.0257776]
#causa=[[12.96  1.23  1.2   6.7  32.68]], prediccion=[2.1092734]
#causa=[[26.15 12.96  1.23  1.2   6.7 ]], prediccion=[2.0215535]
#causa=[[ 2.43 26.15 12.96  1.23  1.2 ]], prediccion=[1.8290602]
#causa=[[ 1.01  2.43 26.15 12.96  1.23]], prediccion=[1.7114415]
#causa=[[ 1.07  1.01  2.43 26.15 12.96]], prediccion=[2.125041]
#causa=[[ 2.14  1.07  1.01  2.43 26.15]], prediccion=[1.8401601]
#causa=[[13.99  2.14  1.07  1.01  2.43]], prediccion=[1.5767789]
#causa=[[ 1.69 13.99  2.14  1.07  1.01]], prediccion=[1.547957]
#causa=[[ 1.33  1.69 13.99  2.14  1.07]], prediccion=[1.4241049]
#causa=[[ 1.24  1.33  1.69 13.99  2.14]], prediccion=[1.7167212]
#causa=[[ 3.4   1.24  1.33  1.69 13.99]], prediccion=[1.7774903]
#causa=[[1.27 3.4  1.24 1.33 1.69]], prediccion=[1.0505065]
#causa=[[6.97 1.27 3.4  1.24 1.33]], prediccion=[1.367261]
#causa=[[1.44 6.97 1.27 3.4  1.24]], prediccion=[1.4227158]
#causa=[[2.3  1.44 6.97 1.27 3.4 ]], prediccion=[1.4228721]
#causa=[[1.16 2.3  1.44 6.97 1.27]], prediccion=[1.3898004]
#causa=[[1.23 1.16 2.3  1.44 6.97]], prediccion=[1.3915299]
#causa=[[1.28 1.23 1.16 2.3  1.44]], prediccion=[0.9319885]
#causa=[[1.97 1.28 1.23 1.16 2.3 ]], prediccion=[0.98581284]
#causa=[[1.31 1.97 1.28 1.23 1.16]], prediccion=[0.8625751]
#causa=[[1.43 1.31 1.97 1.28 1.23]], prediccion=[0.8847961]
#causa=[[2.43 1.43 1.31 1.97 1.28]], prediccion=[1.0172104]
#causa=[[2.36 2.43 1.43 1.31 1.97]], prediccion=[1.1154613]
#causa=[[1.11 2.36 2.43 1.43 1.31]], prediccion=[1.007117]
#causa=[[1.   1.11 2.36 2.43 1.43]], prediccion=[1.0010293]
#causa=[[1.81 1.   1.11 2.36 2.43]], prediccion=[1.0721333]
#causa=[[79.78  1.81  1.    1.11  2.36]], prediccion=[1.2612094]
#causa=[[11.93 79.78  1.81  1.    1.11]], prediccion=[1.527651]
#causa=[[ 1.09 11.93 79.78  1.81  1.  ]], prediccion=[1.3300775]
#causa=[[10.85  1.09 11.93 79.78  1.81]], prediccion=[1.8415525]
#causa=[[ 1.21 10.85  1.09 11.93 79.78]], prediccion=[1.7855511]
#causa=[[ 2.34  1.21 10.85  1.09 11.93]], prediccion=[1.8193432]
#causa=[[ 2.04  2.34  1.21 10.85  1.09]], prediccion=[1.6071653]
#causa=[[ 2.1   2.04  2.34  1.21 10.85]], prediccion=[1.6758858]
#causa=[[2.84 2.1  2.04 2.34 1.21]], prediccion=[1.1890754]
#causa=[[2.51 2.84 2.1  2.04 2.34]], prediccion=[1.3069478]
#causa=[[1.19 2.51 2.84 2.1  2.04]], prediccion=[1.199388]
#causa=[[34.69  1.19  2.51  2.84  2.1 ]], prediccion=[1.540773]
#causa=[[ 1.08 34.69  1.19  2.51  2.84]], prediccion=[1.6832868]
#causa=[[ 3.72  1.08 34.69  1.19  2.51]], prediccion=[1.3605112]
#causa=[[ 1.26  3.72  1.08 34.69  1.19]], prediccion=[1.7847728]
#causa=[[ 1.1   1.26  3.72  1.08 34.69]], prediccion=[1.7745773]
#causa=[[26.18  1.1   1.26  3.72  1.08]], prediccion=[1.5689036]
#causa=[[ 9.48 26.18  1.1   1.26  3.72]], prediccion=[1.9534315]
#causa=[[ 1.07  9.48 26.18  1.1   1.26]], prediccion=[1.5921447]
#causa=[[ 2.24  1.07  9.48 26.18  1.1 ]], prediccion=[1.8912295]
#causa=[[ 1.11  2.24  1.07  9.48 26.18]], prediccion=[2.0617704]
#causa=[[10.25  1.11  2.24  1.07  9.48]], prediccion=[1.8324101]
#causa=[[ 1.46 10.25  1.11  2.24  1.07]], prediccion=[1.4519601]
#causa=[[ 1.24  1.46 10.25  1.11  2.24]], prediccion=[1.3421574]
#causa=[[ 1.48  1.24  1.46 10.25  1.11]], prediccion=[1.5010494]
#causa=[[ 3.49  1.48  1.24  1.46 10.25]], prediccion=[1.6637182]
#causa=[[1.59 3.49 1.48 1.24 1.46]], prediccion=[1.0716012]
#causa=[[2.8  1.59 3.49 1.48 1.24]], prediccion=[1.1598566]
#causa=[[1.3  2.8  1.59 3.49 1.48]], prediccion=[1.2152787]
#causa=[[2.17 1.3  2.8  1.59 3.49]], prediccion=[1.2656778]
#causa=[[14.18  2.17  1.3   2.8   1.59]], prediccion=[1.6279684]
#causa=[[ 1.04 14.18  2.17  1.3   2.8 ]], prediccion=[1.6572016]
#causa=[[ 2.11  1.04 14.18  2.17  1.3 ]], prediccion=[1.4456813]
#causa=[[ 1.    2.11  1.04 14.18  2.17]], prediccion=[1.7219555]
#causa=[[ 2.37  1.    2.11  1.04 14.18]], prediccion=[1.7131256]
#causa=[[1.   2.37 1.   2.11 1.04]], prediccion=[0.9241318]
#causa=[[21.7   1.    2.37  1.    2.11]], prediccion=[1.5540708]
#causa=[[ 1.51 21.7   1.    2.37  1.  ]], prediccion=[1.6536368]
#causa=[[ 1.81  1.51 21.7   1.    2.37]], prediccion=[1.4502747]
#causa=[[ 1.41  1.81  1.51 21.7   1.  ]], prediccion=[1.7735163]
#causa=[[ 1.01  1.41  1.81  1.51 21.7 ]], prediccion=[1.799467]
#causa=[[1.72 1.01 1.41 1.81 1.51]], prediccion=[0.9314788]
#causa=[[1.49 1.72 1.01 1.41 1.81]], prediccion=[0.9333697]
#causa=[[1.05 1.49 1.72 1.01 1.41]], prediccion=[0.83298653]
#causa=[[1.4  1.05 1.49 1.72 1.01]], prediccion=[0.8404644]
#causa=[[2.89 1.4  1.05 1.49 1.72]], prediccion=[1.0349537]
#causa=[[9.27 2.89 1.4  1.05 1.49]], prediccion=[1.4689322]
#causa=[[1.89 9.27 2.89 1.4  1.05]], prediccion=[1.4798559]
#causa=[[1.57 1.89 9.27 2.89 1.4 ]], prediccion=[1.4506612]
#causa=[[1.28 1.57 1.89 9.27 2.89]], prediccion=[1.6214161]
#causa=[[2.88 1.28 1.57 1.89 9.27]], prediccion=[1.6203468]
#causa=[[1.03 2.88 1.28 1.57 1.89]], prediccion=[1.0356952]
#causa=[[1.56 1.03 2.88 1.28 1.57]], prediccion=[0.9786058]
#causa=[[1.04 1.56 1.03 2.88 1.28]], prediccion=[0.9680397]
#causa=[[228.68   1.04   1.56   1.03   2.88]], prediccion=[1.2678269]
#causa=[[  1.45 228.68   1.04   1.56   1.03]], prediccion=[1.5023046]
#causa=[[  4.55   1.45 228.68   1.04   1.56]], prediccion=[1.1232771]
#causa=[[  3.51   4.55   1.45 228.68   1.04]], prediccion=[1.5465941]
#causa=[[  1.22   3.51   4.55   1.45 228.68]], prediccion=[1.6213045]
#causa=[[1.76 1.22 3.51 4.55 1.45]], prediccion=[1.336195]
#causa=[[2.03 1.76 1.22 3.51 4.55]], prediccion=[1.4345461]
#causa=[[3.48 2.03 1.76 1.22 3.51]], prediccion=[1.325929]
#causa=[[3.95 3.48 2.03 1.76 1.22]], prediccion=[1.3200183]
#causa=[[1.16 3.95 3.48 2.03 1.76]], prediccion=[1.3036339]
#causa=[[3.27 1.16 3.95 3.48 2.03]], prediccion=[1.4215215]
#causa=[[1.11 3.27 1.16 3.95 3.48]], prediccion=[1.4186548]
#causa=[[2.   1.11 3.27 1.16 3.95]], prediccion=[1.2603972]
#causa=[[1.71 2.   1.11 3.27 1.16]], prediccion=[1.0981201]
#causa=[[3.1  1.71 2.   1.11 3.27]], prediccion=[1.2591363]
#causa=[[1.47 3.1  1.71 2.   1.11]], prediccion=[1.0849851]
#causa=[[1.66 1.47 3.1  1.71 2.  ]], prediccion=[1.1308119]
#causa=[[5.81 1.66 1.47 3.1  1.71]], prediccion=[1.4065534]
#causa=[[6.96 5.81 1.66 1.47 3.1 ]], prediccion=[1.7011355]
#causa=[[2.64 6.96 5.81 1.66 1.47]], prediccion=[1.6109955]
#causa=[[1.44 2.64 6.96 5.81 1.66]], prediccion=[1.6419096]
#causa=[[2.34 1.44 2.64 6.96 5.81]], prediccion=[1.7654849]
#causa=[[1.95 2.34 1.44 2.64 6.96]], prediccion=[1.5681014]
#causa=[[1.94 1.95 2.34 1.44 2.64]], prediccion=[1.1826361]

#2's sample:

#causa=[[ 6.7  32.68  8.08 30.53  2.55]], prediccion=[2.2578003]    x
#causa=[[ 1.2   6.7  32.68  8.08 30.53]], prediccion=[2.141759]     x
#causa=[[ 8.08 30.53  2.55  1.3  15.06]], prediccion=[2.1860821]    ✔
#causa=[[ 1.23  1.2   6.7  32.68  8.08]], prediccion=[2.0257776]    ✔
#causa=[[12.96  1.23  1.2   6.7  32.68]], prediccion=[2.1092734]    ✔
#causa=[[26.15 12.96  1.23  1.2   6.7 ]], prediccion=[2.0215535]    ✔
#causa=[[ 1.07  1.01  2.43 26.15 12.96]], prediccion=[2.125041]     ✔
#causa=[[ 1.11  2.24  1.07  9.48 26.18]], prediccion=[2.0617704]    ✔



import numpy
import matplotlib.pyplot as plt
import math
import sys
import time
import MySQLdb

from pandas import read_csv
from pandas import read_sql_query
from pandas import DataFrame
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
sample                  = 20000
verbose                 = 1
epochs                  = 2
ronda                   = 512
lookback                = 5

# load the informacion
archivo                 = read_sql_query("SELECT value FROM ( SELECT * FROM crawler ORDER BY round DESC LIMIT %d) sub ORDER BY round ASC" % sample, conn)
informacion             = archivo.values
informacion             = informacion.astype('float32')

#normalización de la información
scaler                  = MinMaxScaler(feature_range=(0, 1))

#dividimos la información
aprender_size           = int(len(informacion) * 0.70)
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
model.add(LSTM(100, input_shape=(1, lookback), return_sequences=True))
model.add(LSTM(16, input_shape=(1, lookback)))
model.add(Dense(1))

model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
            )
            
model.fit(  aprender_x,
            aprender_y,
            epochs=epochs,
            batch_size=ronda,
            callbacks=callbacks_list,
            validation_data=(evaluar_x, evaluar_y),
            verbose=verbose
            )

#volcar la informacion            
#for i in range(len(aprender_x)):
	#print("causa=%s, consecuencia=%s" % (aprender_x[i], aprender_y[i]))
    
    
    
print("*******************  PREDICCIONES  *******************")

# load weights into new model
model.load_weights("modelos/model.h5")

model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
            )

replica_xnew = None

while True:

    #pedimos la informacion
    archivo_xnew         = read_sql_query("SELECT value FROM crawler ORDER BY round DESC LIMIT 0, 5", conn)
    informacion_xnew     = archivo_xnew.values
    informacion_xnew     = informacion_xnew.astype('float32')
    
    #limpiamos la cache
    conn.commit()
    
    #acomodamos el array para que se vea del mismo modo
    informacion_xnew = numpy.dstack(informacion_xnew)
    
    if  ((informacion_xnew != replica_xnew).any() or replica_xnew is None) :
    
        replica_xnew = informacion_xnew

        #realizar prediccion
        ynew = model.predict(informacion_xnew)
        
        #imprimir(ynew)
        
        #volcar la informacion
        for i in range(len(informacion_xnew)):
            imprimir("\n")
            imprimir("causa=%s, prediccion=%s" % (informacion_xnew[i], ynew[i]))