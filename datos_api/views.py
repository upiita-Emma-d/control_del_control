#from django.shortcuts import render
# Create your views here.
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

"""Funciones necesarias para el modelado"""
def calculos_T(ADC,Aest,Aamb,Test,Tamb):
    return (Test-Tamb)/(Aest-Aamb)*(ADC-Aamb) + Tamb

""" FILTRO"""
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

"""CALCULO UNITARIO"""
def unitaria(VECTOR,f_m = 1.2):
    longitud = len(VECTOR)
    p_5p = int(longitud * 0.03)
    VECTOR_R = VECTOR[p_5p:-1]
    T_M = np.max(VECTOR_R)
    T_m = np.min(VECTOR_R)
    VECTOR_R = [ ((i -T_m)/(T_M-T_m)) for i in VECTOR_R]
    
    for i in VECTOR_R:
        if i >= 1-np.e **(-1):
            i_b_63 = i
            break
    punto_63 = (np.where(VECTOR_R ==  i_b_63) * np.array([1]))[0][0]
    MUESTRA =  punto_63+p_5p
    #Y_de_TAO = VECTOR[MUESTRA]
    TAO = (MUESTRA) * f_m
    r = p_5p * f_m
    return TAO , r

""" Metodo Cecil Smith"""
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

class Modelado(APIView):
    ''' API View para el tratamiento de datos '''
    def get(self, request,format = None):
        an_apiview = ['El servidor esta corriendo correctamente',]

        return Response({'Estado':'Ok' , 'Esp':an_apiview})
    
    def post(self,request):
        PWM_E= 500 
        PWM_A = 0 
        ''' Crear un mensaje con nuestro nombre'''
        el_dic = request.data
        VECTOR_ADC = []
        for valores in el_dic['ADC'][1:-1]:
            VECTOR_ADC.append(float(valores))
        Tmax , Tamb = (60,25)
        VECTOR_ADC = np.array(VECTOR_ADC)
        adc_max = np.max(VECTOR_ADC[1:-1])
        adc_min = np.min(VECTOR_ADC[1:-1])
        TEMPERATURA = calculos_T(VECTOR_ADC,adc_max,adc_min,Tmax,Tamb)
        TEMPERATURA_F = filtro(TEMPERATURA)
        TAO , r = unitaria(TEMPERATURA_F)
        p26,p63,k = Ide_Cecil_Smith(TEMPERATURA_F[1:-1],PWM_E,PWM_A)
        datos_modelo = {'Tao':TAO,'r' :r ,'k' : k }
        return Response({'datos_modelo':datos_modelo})
    