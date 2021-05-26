import numpy as np
def Ide_Cecil_Smith(TEM,PWM_E,PWM_A):
    max = np.max(TEM)
    min = np.min(TEM)
    k = (max-min)/(PWM_E-PWM_A)
    print('El valor de k es ' + str(k))
    punto_63 = (max-min) * 0.632 + min 
    punto_28 = (max-min) * 0.283 + min

    for i in TEM:
        if i >= punto_63:
            i_b_63 = i
            break

    for i in TEM:
        if i >= punto_28:
            i_b_28 = i
            break
    punto_63 = (np.where(TEM ==  i_b_63) * np.array([1]))[0][0]
    punto_28 = (np.where(TEM ==  i_b_28) * np.array([1]))[0][0]
    return punto_28 ,punto_63 , k