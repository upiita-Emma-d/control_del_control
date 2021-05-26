import numpy as np
def filtro(T_Sucia):
    T_limpia = np.empty((1,), float)
    T1 = T_Sucia[1]
    T2 = T_Sucia[1]
    T3 = T_Sucia[1]
    T4 = T_Sucia[1]
    T5 = T_Sucia[1]
    T6 = T_Sucia[1]
    T7 = T_Sucia[1]
    T8 = T_Sucia[1]
    T9 = T_Sucia[1]
    T  = T_Sucia[1]
    for i in T_Sucia:
        T9 = T8
        T8 = T7
        T7 = T6
        T6 = T5
        T5 = T4
        T4 = T3
        T3 = T2
        T2 = T1
        if (i < T - 5):
            T1 = T1
        else:
            T1 = i
        T = (T1 + T2 + T3 + T4 + T5 + T6 + T7 + T8 + T9 ) / 9
        T_limpia = np.append(T_limpia,T,axis=None)
    return T_limpia