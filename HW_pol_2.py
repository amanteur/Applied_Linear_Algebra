import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    filepath = 'RC_F01_09_2020_T01_10_2020.xlsx'
    x = [[1, -3, 9],
         [1, -1, 1],
         [1, 0, 0],
         [1, 1, 1],
         [1, 3, 9]]
    y = [-4, -0.8, 1.6, 2.3, 1.5]
    x_pinv = np.linalg.pinv(x)
    print(x_pinv.dot(y))

    data_cb = pd.read_excel(filepath, header=0)
    data_cb['day'] = data_cb['data'].dt.day
    data_eval = data_cb[['day', 'curs']].copy()
    data_eval['day_sq'] = data_eval.day.apply(np.square)
    data_eval['ones'] = 1
    X_part = data_eval[['ones','day','day_sq']].copy()
    Y_part = data_eval[['curs']].copy()

    X = X_part.values
    Y = Y_part.values
    cof = np.linalg.pinv(X).dot(Y)
    print(cof)
    print(np.array([1, 32, 1024]).dot(cof))
    plt.plot(data_eval['day'], data_eval['curs'], '-ok')
    plt.plot(data_eval['day'], 74.7724008+data_eval['day']*(-0.0626611)+data_eval['day_sq']*0.006260472, 'r--')
    plt.show()


