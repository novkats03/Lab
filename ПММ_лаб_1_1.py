import numpy as np


dx = 0.02 #
dt = 0.001 

D_1 = 0.1 
D_2 = 0.2

tmax = 4.0 
L = 1.0 

x = np.arange(0,1+dx,dx).round(3) # Массив с отрезками расстояния
t = np.arange(0,tmax+dt,dt).round(3) # Массив с отрезками времени
nx = len(x) # Количество шагов по x
nt = len(t) # Количество шагов по t

# Начальные и граничные условия
initialConditions = np.arange(L,0-dx,-dx).round(3)
boundaryConditions = [0,0]

# Создание нулевой матрицы
T = np.zeros((nx, nt))

# Задание начальных и граничных условий
T[:, 0] = initialConditions

# Расчет температуры, явная схема
for j in range(1, nt):
    # Первая половина отрезка
    for i in range(1, (int)(nx/2)):
        T[i, j] = D_1 * T[i-1, j-1] + (1 - 2 * D_1) * T[i, j-1] + D_1 * T[i+1, j-1]
    # Вторая половина отрезка
    for i in range((int)(nx/2), nx-1):
        T[i, j] = D_2 * T[i-1, j-1] + (1 - 2 * D_2) * T[i, j-1] + D_2 * T[i+1, j-1]
    # Граничные условия
    T[0,j] = T[1,j]
    T[-1, j] = T[-2, j]

