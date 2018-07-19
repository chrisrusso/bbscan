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



#causa=[[ 4.86 17.59 10.69 ...  1.63  7.25  1.06]], prediccion=[6.6772413]
#causa=[[1.25 1.32 2.1  ... 1.41 1.3  1.31]], prediccion=[6.2349424]               | decrese  |
#causa=[[25.42  1.25  1.32 ...  1.81  1.41  1.3 ]], prediccion=[5.95535]           | decrese  |
#causa=[[ 2.4  25.42  1.25 ...  3.7   1.81  1.41]], prediccion=[6.0726333]         | increase | ✔
#causa=[[10.79  2.4  25.42 ... 12.94  3.7   1.81]], prediccion=[6.305819]          | increase | ✔
#causa=[[ 3.18 10.79  2.4  ...  3.61 12.94  3.7 ]], prediccion=[6.6679688]         | increase | ✘
#causa=[[ 1.36  3.18 10.79 ...  1.69  3.61 12.94]], prediccion=[6.3308315]         | decrese  |
#causa=[[1.04 1.36 3.18 ... 2.72 1.69 3.61]], prediccion=[6.6011014]               | increase | ✔
#causa=[[11.72  1.04  1.36 ...  7.04  2.72  1.69]], prediccion=[6.587915]          | decrese  |
#causa=[[ 1.21 11.72  1.04 ...  1.9   7.04  2.72]], prediccion=[6.299929]          | decrese  |
#causa=[[ 2.02  1.21 11.72 ...  1.33  1.9   7.04]], prediccion=[6.514153]          | increase | ✔
#causa=[[3.82 2.02 1.21 ... 1.   1.33 1.9 ]], prediccion=[6.3291473]               | decrese  |
#causa=[[1.65 3.82 2.02 ... 6.17 1.   1.33]], prediccion=[6.2007775]               | decrese  |
#causa=[[1.68 1.65 3.82 ... 6.43 6.17 1.  ]], prediccion=[6.435634]                | increase | ✔
#causa=[[2.19 1.68 1.65 ... 7.41 6.43 6.17]], prediccion=[6.5201287]               | increase | ✔
#causa=[[10.83  2.19  1.68 ...  1.47  7.41  6.43]], prediccion=[6.438373]          | decrese  |
#causa=[[ 1.17 10.83  2.19 ...  1.02  1.47  7.41]], prediccion=[6.2926836]         | decrese  |
#causa=[[ 2.56  1.17 10.83 ...  3.38  1.02  1.47]], prediccion=[6.594214]          | increase | ✘
#causa=[[1.08 2.56 1.17 ... 1.31 3.38 1.02]], prediccion=[6.699945]                | increase | ✔
#causa=[[8.59 1.08 2.56 ... 7.67 1.31 3.38]], prediccion=[6.118062]                | decrese  |
#causa=[[4.04 8.59 1.08 ... 1.97 7.67 1.31]], prediccion=[6.438801]                | increase | ✔
#causa=[[2.05 4.04 8.59 ... 1.5  1.97 7.67]], prediccion=[6.086519]                | decrese  |
#causa=[[ 4.84  2.05  4.04 ... 21.63  1.5   1.97]], prediccion=[6.5127635]         | increase | ✔
#causa=[[67.29  4.84  2.05 ...  2.37 21.63  1.5 ]], prediccion=[6.7355747]         | increase | ✔
#causa=[[ 8.52 67.29  4.84 ...  1.32  2.37 21.63]], prediccion=[6.093475]          | decrese  |
#causa=[[ 2.43  8.52 67.29 ...  1.64  1.32  2.37]], prediccion=[6.4250426]         | increase | ✘
#causa=[[1.94 2.43 8.52 ... 1.32 1.64 1.32]], prediccion=[6.7672696]               | increase | ✘
#causa=[[1.1  1.94 2.43 ... 5.28 1.32 1.64]], prediccion=[6.462262]                | decrese  |
#causa=[[1.55 1.1  1.94 ... 1.05 5.28 1.32]], prediccion=[6.4632134]               | increase | ✔
#causa=[[3.14 1.55 1.1  ... 1.   1.05 5.28]], prediccion=[6.4258757]               | decrese  |
#causa=[[1.25 3.14 1.55 ... 1.64 1.   1.05]], prediccion=[6.184064]                | decrese  |
#causa=[[1.12 1.25 3.14 ... 1.66 1.64 1.  ]], prediccion=[6.511156]                | increase | ✘
#causa=[[1.11 1.12 1.25 ... 1.61 1.66 1.64]], prediccion=[6.53168]                 | increase | ✔
#causa=[[4.   1.11 1.12 ... 1.13 1.61 1.66]], prediccion=[6.3763876]               | decrese  |
#causa=[[1.66 4.   1.11 ... 2.21 1.13 1.61]], prediccion=[6.3728766]               | decrese  |
#causa=[[3.66 1.66 4.   ... 3.82 2.21 1.13]], prediccion=[6.6097565]               | increase | ✔
#causa=[[3.05 3.66 1.66 ... 3.25 3.82 2.21]], prediccion=[6.288253]                | decrese  |
#causa=[[1.01 3.05 3.66 ... 1.31 3.25 3.82]], prediccion=[6.2183385]               | decrese  |
#causa=[[1.   1.01 3.05 ... 1.08 1.31 3.25]], prediccion=[6.564011]                | increase | ✔
#causa=[[2.18 1.   1.01 ... 1.33 1.08 1.31]], prediccion=[6.1810007]               | decrese  |
#causa=[[2.5  2.18 1.   ... 1.44 1.33 1.08]], prediccion=[6.2104425]               | increase | ✔
#causa=[[2.36 2.5  2.18 ... 1.92 1.44 1.33]], prediccion=[6.4487143]               | increase | ✘
#causa=[[1.28 2.36 2.5  ... 4.2  1.92 1.44]], prediccion=[6.156814]                | decrese  |
#causa=[[1.03 1.28 2.36 ... 2.44 4.2  1.92]], prediccion=[6.552446]                | increase | ✔
#causa=[[6.98 1.03 1.28 ... 1.17 2.44 4.2 ]], prediccion=[6.502436]                | decrese  |
#causa=[[ 1.38  6.98  1.03 ... 30.3   1.17  2.44]], prediccion=[6.425912]          | decrese  |
#causa=[[ 1.94  1.38  6.98 ...  5.64 30.3   1.17]], prediccion=[6.5766835]         | increase | ✘
#causa=[[ 1.07  1.94  1.38 ...  1.28  5.64 30.3 ]], prediccion=[6.20017]           | decrese  |
#causa=[[2.4  1.07 1.94 ... 2.77 1.28 5.64]], prediccion=[6.2360296]               | increase | ✔
#causa=[[2.23 2.4  1.07 ... 3.01 2.77 1.28]], prediccion=[6.43255]                 | increase | ✘
#causa=[[1.14 2.23 2.4  ... 5.45 3.01 2.77]], prediccion=[6.445481]                | increase | ✘
#causa=[[1.16 1.14 2.23 ... 2.34 5.45 3.01]], prediccion=[6.4806695]               | increase | ✘
#causa=[[1.45 1.16 1.14 ... 1.33 2.34 5.45]], prediccion=[6.2532363]               | decrese  |
#causa=[[1.2  1.45 1.16 ... 1.23 1.33 2.34]], prediccion=[6.4214883]               | increase | ✔
#causa=[[2.79 1.2  1.45 ... 2.   1.23 1.33]], prediccion=[6.555929]                | increase | ✘
#causa=[[1.   2.79 1.2  ... 2.57 2.   1.23]], prediccion=[6.2893515]               | decrese  |
#causa=[[2.56 1.   2.79 ... 1.87 2.57 2.  ]], prediccion=[6.6096053]               | increase | ✘
#causa=[[1.85 2.56 1.   ... 3.29 1.87 2.57]], prediccion=[6.058769]                | decrese  |
#causa=[[ 3.76  1.85  2.56 ... 10.76  3.29  1.87]], prediccion=[6.355071]          | increase | ✔
#causa=[[42.79  3.76  1.85 ...  1.44 10.76  3.29]], prediccion=[6.494027]          | increase | ✘
#causa=[[ 1.2  42.79  3.76 ... 14.37  1.44 10.76]], prediccion=[6.3482575]         | decrese  |
#causa=[[ 1.27  1.2  42.79 ...  1.67 14.37  1.44]], prediccion=[6.6480646]         | increase | ✘
#causa=[[ 1.03  1.27  1.2  ...  4.48  1.67 14.37]], prediccion=[6.6633134]         | increase | ✘
#causa=[[1.43 1.03 1.27 ... 5.32 4.48 1.67]], prediccion=[6.664973]                | increase | ✘
#causa=[[1.14 1.43 1.03 ... 1.   5.32 4.48]], prediccion=[6.545299]                | decrese  |
#causa=[[6.77 1.14 1.43 ... 7.08 1.   5.32]], prediccion=[6.4004736]               | decrese  |
#causa=[[1.09 6.77 1.14 ... 2.73 7.08 1.  ]], prediccion=[6.6162605]               | increase | ✘
#causa=[[ 1.45  1.09  6.77 ... 83.34  2.73  7.08]], prediccion=[6.1438074]         | decrese  |
#causa=[[ 1.19  1.45  1.09 ...  1.36 83.34  2.73]], prediccion=[6.5912995]         | increase | ✔
#causa=[[22.1   1.19  1.45 ...  1.68  1.36 83.34]], prediccion=[6.6032033]         | increase | ✘
#causa=[[ 1.54 22.1   1.19 ...  5.78  1.68  1.36]], prediccion=[6.6265044]         | increase | ✔
#causa=[[ 7.92  1.54 22.1  ... 54.08  5.78  1.68]], prediccion=[6.4428716]         | decrese  |
#causa=[[ 3.38  7.92  1.54 ...  1.01 54.08  5.78]], prediccion=[6.518398]          | increase | ✘
#causa=[[ 1.55  3.38  7.92 ...  2.87  1.01 54.08]], prediccion=[6.3882027]         | decrese  |
#causa=[[2.07 1.55 3.38 ... 1.45 2.87 1.01]], prediccion=[6.6043005]               | increase | ✔
#causa=[[8.57 2.07 1.55 ... 3.24 1.45 2.87]], prediccion=[6.3992543]               | decrese  |
#causa=[[1.   8.57 2.07 ... 3.45 3.24 1.45]], prediccion=[6.3788934]               | decrese  |
#causa=[[11.41  1.    8.57 ...  9.28  3.45  3.24]], prediccion=[6.6099]            | increase | ✘
#causa=[[ 1.58 11.41  1.   ...  2.9   9.28  3.45]], prediccion=[6.4242754]         | decrese  |
#causa=[[ 2.19  1.58 11.41 ...  3.49  2.9   9.28]], prediccion=[6.432927]          | increase | ✔
#causa=[[5.82 2.19 1.58 ... 2.02 3.49 2.9 ]], prediccion=[6.496781]                | increase | ✘
#causa=[[1.03 5.82 2.19 ... 4.52 2.02 3.49]], prediccion=[6.6258965]               | increase | ✘
#causa=[[ 1.26  1.03  5.82 ... 28.18  4.52  2.02]], prediccion=[6.5242615]         | decrese  |
#causa=[[ 2.8   1.26  1.03 ...  1.31 28.18  4.52]], prediccion=[6.4217896]         | decrese  |
#causa=[[ 1.04  2.8   1.26 ...  7.72  1.31 28.18]], prediccion=[6.468828]          | increase | ✔
#causa=[[82.95  1.04  2.8  ...  1.11  7.72  1.31]], prediccion=[6.360006]          | decrese  |
#causa=[[ 3.68 82.95  1.04 ...  9.76  1.11  7.72]], prediccion=[6.6852126]         | increase | ✘
#causa=[[ 1.38  3.68 82.95 ...  3.74  9.76  1.11]], prediccion=[6.021569]          | decrese  |
#causa=[[123.89   1.38   3.68 ...   1.44   3.74   9.76]], prediccion=[6.4289412]   | increase | ✔
#causa=[[  5.29 123.89   1.38 ...   1.68   1.44   3.74]], prediccion=[6.4080157]   | decrese  |
#causa=[[  1.72   5.29 123.89 ...   1.24   1.68   1.44]], prediccion=[6.2651243]   | decrese  |
#causa=[[1.38 1.72 5.29 ... 5.03 1.24 1.68]], prediccion=[6.2496324]               | decrese  |
#causa=[[6.03 1.38 1.72 ... 1.75 5.03 1.24]], prediccion=[6.0209546]               | decrese  |
#causa=[[6.65 6.03 1.38 ... 2.1  1.75 5.03]], prediccion=[6.6680875]               | increase | ✘
#causa=[[1.98 6.65 6.03 ... 3.04 2.1  1.75]], prediccion=[6.630469]                | decrese  |
#causa=[[1.98 1.98 6.65 ... 1.94 3.04 2.1 ]], prediccion=[6.4467826]               | decrese  |
#causa=[[5.45 1.98 1.98 ... 4.06 1.94 3.04]], prediccion=[6.349032]                | decrese  |
#causa=[[1.32 5.45 1.98 ... 1.35 4.06 1.94]], prediccion=[6.0981803]               | decrese  |
#causa=[[1.65 1.32 5.45 ... 1.52 1.35 4.06]], prediccion=[6.6286182]               | increase | ✔
#causa=[[9.6  1.65 1.32 ... 3.79 1.52 1.35]], prediccion=[6.315363]                | decrese  |
#causa=[[8.25 9.6  1.65 ... 1.28 3.79 1.52]], prediccion=[6.6835017]               | increase | ✘
#causa=[[1.08 8.25 9.6  ... 1.12 1.28 3.79]], prediccion=[6.3633127]               | decrese  |
#causa=[[1.02 1.08 8.25 ... 2.02 1.12 1.28]], prediccion=[6.41433]                 | increase | ✘
#causa=[[1.67 1.02 1.08 ... 1.87 2.02 1.12]], prediccion=[6.2105865]               | decrese  |
#causa=[[14.84  1.67  1.02 ...  2.46  1.87  2.02]], prediccion=[6.3014603]         | increase | ✔
#causa=[[11.88 14.84  1.67 ...  4.27  2.46  1.87]], prediccion=[6.083673]          | decrese  |
#causa=[[ 2.81 11.88 14.84 ...  1.37  4.27  2.46]], prediccion=[6.2597604]         | increase | ✔
#causa=[[ 3.44  2.81 11.88 ...  1.32  1.37  4.27]], prediccion=[6.4561853]         | increase | ✘
#causa=[[1.59 3.44 2.81 ... 1.02 1.32 1.37]], prediccion=[6.3631864]               | decrese  |
#causa=[[2.86 1.59 3.44 ... 1.61 1.02 1.32]], prediccion=[6.3287873]               | decrese  |
#causa=[[1.2  2.86 1.59 ... 1.32 1.61 1.02]], prediccion=[6.445797]                | increase | ✘
#causa=[[1.9  1.2  2.86 ... 1.7  1.32 1.61]], prediccion=[6.351001]                | decrese  |
#causa=[[1.84 1.9  1.2  ... 4.64 1.7  1.32]], prediccion=[6.5415707]               | increase | ✔
#causa=[[22.75  1.84  1.9  ...  2.81  4.64  1.7 ]], prediccion=[6.278867]          | decrese  |
#causa=[[ 4.28 22.75  1.84 ...  2.27  2.81  4.64]], prediccion=[5.9926243]         | decrese  |
#causa=[[ 1.13  4.28 22.75 ...  2.2   2.27  2.81]], prediccion=[6.3585343]         | increase | ✘
#causa=[[ 1.71  1.13  4.28 ... 26.38  2.2   2.27]], prediccion=[6.388146]          | increase | ✘
#causa=[[ 1.7   1.71  1.13 ...  1.26 26.38  2.2 ]], prediccion=[6.659692]          | increase | ✘
#causa=[[ 1.26  1.7   1.71 ...  3.23  1.26 26.38]], prediccion=[6.403067]          | decrese  |
#causa=[[ 2.2   1.26  1.7  ... 14.48  3.23  1.26]], prediccion=[6.5375977]         | increase | ✘
#causa=[[ 1.28  2.2   1.26 ... 10.86 14.48  3.23]], prediccion=[6.264456]          | decrese  |
#causa=[[  2.81   1.28   2.2  ... 101.25  10.86  14.48]], prediccion=[6.3704057]   | increase | ✘
#causa=[[  1.15   2.81   1.28 ...   3.59 101.25  10.86]], prediccion=[6.7792697]   | increase | ✔
#causa=[[  2.76   1.15   2.81 ...  17.6    3.59 101.25]], prediccion=[6.1073403]   | decrese  |
#causa=[[ 1.86  2.76  1.15 ...  1.26 17.6   3.59]], prediccion=[6.4619875]         | increase | ✔
#causa=[[ 2.53  1.86  2.76 ...  1.89  1.26 17.6 ]], prediccion=[6.4773273]         | increase | ✔
#causa=[[2.87 2.53 1.86 ... 3.33 1.89 1.26]], prediccion=[6.6477456]               | increase | ✔
#causa=[[13.49  2.87  2.53 ...  1.24  3.33  1.89]], prediccion=[6.4823256]         | decrese  |
#causa=[[16.28 13.49  2.87 ...  3.91  1.24  3.33]], prediccion=[5.975121]          | decrese  |
#causa=[[ 3.16 16.28 13.49 ... 13.56  3.91  1.24]], prediccion=[6.1763263]         | increase | ✔
#causa=[[ 2.17  3.16 16.28 ...  1.06 13.56  3.91]], prediccion=[6.7989225]         | increase | ✔
#causa=[[ 3.54  2.17  3.16 ...  1.2   1.06 13.56]], prediccion=[6.595823]          | decrese  |
#causa=[[27.69  3.54  2.17 ...  1.87  1.2   1.06]], prediccion=[6.2591724]         | decrese  |
#causa=[[ 3.16 27.69  3.54 ...  3.45  1.87  1.2 ]], prediccion=[6.425097]          | increase | ✔
#causa=[[ 3.06  3.16 27.69 ...  5.86  3.45  1.87]], prediccion=[6.416021]          | decrese  |
#causa=[[3.06 3.06 3.16 ... 1.46 5.86 3.45]], prediccion=[6.4337053]               | increase | ✘
#causa=[[1.05 3.06 3.06 ... 1.41 1.46 5.86]], prediccion=[6.3975477]               | decrese  |
#causa=[[ 1.51  1.05  3.06 ... 19.3   1.41  1.46]], prediccion=[6.284749]          | decrese  |
#causa=[[ 2.54  1.51  1.05 ...  2.55 19.3   1.41]], prediccion=[6.4373617]         | increase | ✔
#causa=[[ 2.1   2.54  1.51 ...  1.25  2.55 19.3 ]], prediccion=[6.3087196]         | decrese  |
#causa=[[1.75 2.1  2.54 ... 2.14 1.25 2.55]], prediccion=[6.4407353]               | increase | ✔
#causa=[[14.95  1.75  2.1  ...  1.71  2.14  1.25]], prediccion=[5.8787146]         | decrese  |
#causa=[[364.49  14.95   1.75 ...   1.14   1.71   2.14]], prediccion=[6.504489]    | increase | ✘
#causa=[[  1.92 364.49  14.95 ...   8.29   1.14   1.71]], prediccion=[6.2889376]   | decrese  |
#causa=[[  1.34   1.92 364.49 ...   1.34   8.29   1.14]], prediccion=[6.2228556]   | decrese  |
#causa=[[4.65 1.34 1.92 ... 1.17 1.34 8.29]], prediccion=[6.1751914]               | decrese  |
#causa=[[ 1.28  4.65  1.34 ... 16.4   1.17  1.34]], prediccion=[6.0590596]         | decrese  |
#causa=[[ 6.1   1.28  4.65 ...  3.46 16.4   1.17]], prediccion=[6.4257054]         | increase | ✘
#causa=[[ 1.69  6.1   1.28 ...  1.99  3.46 16.4 ]], prediccion=[6.2666087]         | decrese  |
#causa=[[1.34 1.69 6.1  ... 1.21 1.99 3.46]], prediccion=[6.343335]                | increase | ✘
#causa=[[1.24 1.34 1.69 ... 3.07 1.21 1.99]], prediccion=[6.0313706]               | decrese  |
#causa=[[2.63 1.24 1.34 ... 1.14 3.07 1.21]], prediccion=[6.0767074]               | increase | ✘
#causa=[[1.63 2.63 1.24 ... 2.02 1.14 3.07]], prediccion=[6.5230875]               | increase | ✔
#causa=[[17.05  1.63  2.63 ...  2.24  2.02  1.14]], prediccion=[6.4449873]         | decrese  |
#causa=[[ 2.08 17.05  1.63 ...  3.96  2.24  2.02]], prediccion=[6.3903503]         | decrese  |
#causa=[[ 3.74  2.08 17.05 ... 12.89  3.96  2.24]], prediccion=[6.3422256]         | decrese  |
#causa=[[ 3.51  3.74  2.08 ...  2.02 12.89  3.96]], prediccion=[6.515119]          | increase | ✘
#causa=[[ 1.27  3.51  3.74 ...  1.3   2.02 12.89]], prediccion=[6.461135]          | decrese  |
#causa=[[1.18 1.27 3.51 ... 1.46 1.3  2.02]], prediccion=[6.503974]                | increase | ✔
#causa=[[2.71 1.18 1.27 ... 2.41 1.46 1.3 ]], prediccion=[6.581463]                | increase | ✘
#causa=[[1.14 2.71 1.18 ... 1.   2.41 1.46]], prediccion=[6.5308905]               | decrese  |
#causa=[[2.02 1.14 2.71 ... 1.7  1.   2.41]], prediccion=[6.614926]                | increase | ✘
#causa=[[1.4  2.02 1.14 ... 4.15 1.7  1.  ]], prediccion=[6.348063]                | decrese  |
#causa=[[6.19 1.4  2.02 ... 1.91 4.15 1.7 ]], prediccion=[6.539205]                | increase | ✔
#causa=[[3.55 6.19 1.4  ... 1.76 1.91 4.15]], prediccion=[6.1584053]               | decrese  |
#causa=[[1.07 3.55 6.19 ... 1.26 1.76 1.91]], prediccion=[6.0621634]               | decrese  |
#causa=[[ 2.66  1.07  3.55 ... 16.72  1.26  1.76]], prediccion=[6.296217]          | increase | ✔
#causa=[[ 3.14  2.66  1.07 ...  1.62 16.72  1.26]], prediccion=[6.2414155]         | decrese  |
#causa=[[ 2.68  3.14  2.66 ...  1.37  1.62 16.72]], prediccion=[6.7197347]         | increase | ✔
#causa=[[5.36 2.68 3.14 ... 1.82 1.37 1.62]], prediccion=[6.213267]                | decrese  |
#causa=[[1.67 5.36 2.68 ... 1.86 1.82 1.37]], prediccion=[5.8007317]               | decrese  |
#causa=[[3.45 1.67 5.36 ... 1.09 1.86 1.82]], prediccion=[6.301687]                | increase | ✘
#causa=[[1.88 3.45 1.67 ... 2.07 1.09 1.86]], prediccion=[6.3988643]               | increase | ✔
#causa=[[50.1   1.88  3.45 ...  1.53  2.07  1.09]], prediccion=[6.727245]          | increase | ✘
#causa=[[ 1.93 50.1   1.88 ...  1.51  1.53  2.07]], prediccion=[6.4288063]         | decrese  |
#causa=[[ 1.34  1.93 50.1  ...  2.19  1.51  1.53]], prediccion=[6.154322]          | decrese  |
#causa=[[13.31  1.34  1.93 ...  1.66  2.19  1.51]], prediccion=[6.555101]          | increase | ✔
#causa=[[ 2.55 13.31  1.34 ...  1.29  1.66  2.19]], prediccion=[6.329008]          | decrese  |
#causa=[[ 1.54  2.55 13.31 ...  8.45  1.29  1.66]], prediccion=[6.284314]          | decrese  |
#causa=[[2.5  1.54 2.55 ... 1.18 8.45 1.29]], prediccion=[6.4359183]               | increase | ✘
#causa=[[1.12 2.5  1.54 ... 1.8  1.18 8.45]], prediccion=[6.118804]                | decrese  |
#causa=[[3.48 1.12 2.5  ... 1.99 1.8  1.18]], prediccion=[6.073465]                | decrese  |




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
sample                  = 520000
verbose                 = 1
epochs                  = 30
ronda                   = 256
lookback                = 2000

# load the informacion
archivo                 = read_sql_query("SELECT value FROM ( SELECT * FROM crawler ORDER BY round DESC LIMIT %d) sub ORDER BY round ASC" % sample, conn)
informacion             = archivo.values
informacion             = informacion.astype('float32')

#normalización de la información
scaler                  = MinMaxScaler(feature_range=(0, 1))

#dividimos la información
aprender_size           = int(len(informacion) * 0.80)
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

# eliminamos el modelo creado
del model 

#volcar la informacion            
#for i in range(len(aprender_x)):
	#print("causa=%s, consecuencia=%s" % (aprender_x[i], aprender_y[i]))
    

# recuperamos el modelo de mayor presición
model = load_model('modelos/model.h5')

    
print("*******************  PREDICCIONES  *******************")

replica_xnew = None

while True:

    #pedimos la informacion
    archivo_xnew         = read_sql_query("SELECT value FROM crawler ORDER BY round DESC LIMIT 0, %d" % lookback, conn)
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
            
            