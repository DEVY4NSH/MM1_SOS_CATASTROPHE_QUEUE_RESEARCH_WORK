import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def equations(t, Y, params, N):
    """Defines the system of ODEs for all n."""
    lambda_, mu1, mu2, r, alpha, gamma = params
    
    R, P, Q = Y[0], Y[1:N+1], Y[N+1:]
    
    dR_dt = -lambda_ * R + mu1 * (1 - r) * P[0] + mu2 * Q[0] + alpha * gamma * (1 - R)
    dP_dt = np.zeros(N)
    dQ_dt = np.zeros(N)
    
    dP_dt[0] = -(lambda_ + mu1 + alpha * gamma) * P[0] + lambda_ * R + mu1 * (1 - r) * P[1] + mu2 * Q[1]
    dQ_dt[0] = -(lambda_ + mu2 + alpha * gamma) * Q[0] + mu1 * r * P[0]
    
    for n in range(1, N - 1):
        dP_dt[n] = -(lambda_ + mu1 + alpha * gamma) * P[n] + lambda_ * P[n-1] + mu1 * (1 - r) * P[n+1] + mu2 * Q[n+1]
        dQ_dt[n] = -(lambda_ + mu2 + alpha * gamma) * Q[n] + mu1 * r * P[n] + lambda_ * Q[n-1]
    
    dP_dt[N-1] = -(lambda_ + mu1 + alpha * gamma) * P[N-1] + lambda_ * P[N-2]
    dQ_dt[N-1] = -(lambda_ + mu2 + alpha * gamma) * Q[N-1] + mu1 * r * P[N-1] + lambda_ * Q[N-2]
    
    return np.concatenate(([dR_dt], dP_dt, dQ_dt))

def runge_kutta4(equations, Y0, t_range, h, params, N):
    """Solves ODEs using the RK4 method."""
    t_values = np.arange(t_range[0], t_range[1], h)
    Y_values = np.zeros((len(t_values), len(Y0)))
    
    Y_values[0] = Y0
    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        Y = Y_values[i - 1]
        
        k1 = h * equations(t, Y, params, N)
        k2 = h * equations(t + h/2, Y + k1/2, params, N)
        k3 = h * equations(t + h/2, Y + k2/2, params, N)
        k4 = h * equations(t + h, Y + k3, params, N)
        
        Y_values[i] = Y + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t_values, Y_values

# Define number of Pn, Qn terms
N = 500

# Initial conditions
Y0 = np.zeros(2*N + 1)
Y0[0] = 0  # Initial R value
Y0[1] = 1  # Initial P0
Y0[N+1] = 0  # Initial Q0


def solve(params):
    t_range = (0, 50)
    h = 0.01

    t_values, Y_values = runge_kutta4(equations, Y0, t_range, h, params, N)
    
    R = []
    Ls = []
    Ws = []
    Lq = []
    Wq = []
    time_stamp = []

    for j in range(10,51):
        if j%10 != 0:
            continue
        lsys = 0
        lqueue = 0
        ind = int(j/h)-1
        for k in range(N+1):
            if k==0:
                continue
            lsys+=(k)*(Y_values[ind][k]+Y_values[ind][N+k])
            lqueue+=(k-1)*(Y_values[ind][k]+Y_values[ind][N+k])

        Ls.append(lsys)
        Ws.append(lsys/params[0])
        R.append(Y_values[ind][0])
        Lq.append(lqueue)
        Wq.append(lqueue/params[0])
        time_stamp.append(j)
        
    
    df = pd.DataFrame({
        'Time Stamp': time_stamp,
        'R': R,
        'Ls': Ls,
        'Lq': Lq,
        'Ws': Ws,
        'Wq': Wq
    })
    
    latex_table = df.to_latex(index=False)
    print(latex_table)
    print(df)

    
lambda_ = 8
mu1 = 15
mu2 = 20
gamme = 0.01
alp = 0.5
r = 0.4

#Finding the numerical values corresponding too variation in any parameter 
for variation in range(4,11):
    params = [variation,mu1,mu2,r,alp,gamme]
    solve(params)