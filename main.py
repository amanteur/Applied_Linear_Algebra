import pandas as pd
import numpy as np


if __name__ == '__main__':
    path = 'C:/Amanturs new/study/1sem/1half/linal/hw/USDRUB_200904_200924.csv'
    path2 = 'C:/Amanturs new/study/1sem/1half/linal/hw/RC_F04_09_2020_T24_09_2020.xlsx'

    data = pd.read_csv(path, header=0, sep=',')
    S_open = pd.DataFrame(data['<OPEN>']).to_numpy()
    S_high = pd.DataFrame(data['<HIGH>']).to_numpy()
    S_low = pd.DataFrame(data['<LOW>']).to_numpy()
    S_close = pd.DataFrame(data['<CLOSE>']).to_numpy()

    data_cb = pd.read_excel(path2, header=0)
    print(data_cb.head())
    S_cb = pd.DataFrame(data_cb['curs']).to_numpy()

    S = np.concatenate((S_open, S_close, S_low, S_high), axis=1)
    S_pred = np.zeros((4, 1))

    t = np.full((18, 2), 1)
    t[:, 0] = np.arange(1, 19)

    t_new = np.full((15, 2), 1)
    t_days = np.array([1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21])
    t_new[:, 0] = t_days
    print(t_new)

    t_pinv = np.linalg.pinv(t)

    t_pinv_new = np.linalg.pinv(t_new)

    coef = np.ones(shape=(4, 2))
    for i in range(0, 4):
        coef = np.dot(t_pinv, S[:, i])
        print(coef[0]*19+coef[1])
    coef_cb = np.ones(shape=(1, 2))
    coef_cb = np.dot(t_pinv_new, S_cb)

    print(coef_cb[0] * 22 + coef_cb[1])
