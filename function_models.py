import matplotlib.pyplot as plt
import numpy as np
import random

def step_resp(k, Wn,E, delta):
    u = 0
    y = 0
    t = 0
    z = []
    tt = []
    uu = []

    while t<=1000: 
            if t % 100 == 0:
                u = random.random() * 100
                
                
            uu.append(u)
            z.append(y)
            tt.append(t)
            t=t+1
            A=(1/(1/delta**2)+((E*Wn)/delta))
            B=(Wn**2)*k
            C=(Wn**2)-(2/delta**2)
            D=(1/delta**2)-((E*Wn)/(delta))
            y=(1/A)*(B*uu[t-1]-C*z[t-1]-D*z[t-2])
            #print(y)

    '''Grafica respuesta escalon'''
    tt = np.transpose(tt)
    plt.plot(z, color = "red")
    plt.plot(uu, color = "blue")
    plt.legend()
    plt.show()
    return uu, z, tt

def normalizacion(z, uu):
    z_max = max(z)
    z_min = min(z)
    u_max = max(uu)
    u_min = min(uu)
    UY_min_max = list(np.array([u_min, u_max, z_min, z_max]))
    #np.savetxt('UY_min_max.txt', UY_min_max)
    '''inicializo los vectores para llenar al normalizar'''
    u_norm = []
    z_norm = []

    '''Normalizo y lleno los vectores con el ciclo'''
    for i in range(len(z)):
        z_norm.append((z[i] - z_min)/(z_max - z_min))
        u_norm.append((uu[i] - u_min)/(u_max -  u_min))
    '''tamaño de las matrices'''
    len_z = len(z_norm)
    len_u = len(u_norm)
    return z_norm, u_norm, len_z, len_u

def out_matriz(z_norm, u_norm, len_z, len_u):
    '''organizo las matrices de igual tamaño'''
    '''genero las matrices eliminando los retardos'''
    yk_2 = np.delete(z_norm, (len_z - 2, len_z - 1))
    yk_1 = np.delete(z_norm, (0, len_z - 1))
    uk_2 = np.delete(u_norm, (len_u - 2, len_u - 1))
    uk_1 = np.delete(u_norm, (0, len_u - 1))
    target_matriz = np.delete(z_norm, (0, 1))
    out_random = list(target_matriz)
    np.savetxt('out_random.txt', out_random)

    '''organizo la matriz de salida y de tiempo'''
    training_matriz = np.array([uk_1, uk_2, yk_1, yk_2])
    training_matriz = np.transpose(training_matriz)
    matriz = list(training_matriz)
    np.savetxt('in_random.txt', matriz, delimiter = '    ')
    #save('matriz.txt')
    #plt.plot(training_matriz)
    #plt.show()
    return target_matriz, training_matriz

def step_aleat(k, Wn,E, delta):
    u = 0
    y = 0
    t = 0
    z = []
    tt = []
    uu = []

    while t<=1000: 
            if t % 100 == 0:
                u = random.random() * 100
                
                
            uu.append(u)
            z.append(y)
            tt.append(t)
            t=t+1
            A=(1/(1/delta**2)+((E*Wn)/delta))
            B=(Wn**2)*k
            C=(Wn**2)-(2/delta**2)
            D=(1/delta**2)-((E*Wn)/(delta))
            y=(1/A)*(B*uu[t-1]-C*z[t-1]-D*z[t-2])
            #print(y)
    '''Grafica respuesta escalon'''
    tt = np.transpose(tt)
    plt.plot(z, color = "red")
    plt.plot(uu, color = "blue")
    plt.legend()
    plt.show()
    
    [z_norm, u_norm, len_z, len_u] = normalizacion(z, uu)
    [target_matriz, training_matriz] = out_matriz(z_norm, u_norm, len_z, len_u)
    return target_matriz, training_matriz
    
def only_u(k, Wn,E, delta):
    u = 0
    y = 0
    t = 0
    z = []
    tt = []
    uu = []

    while t<=1000: 
            if t % 100 == 0:
                u = random.random() * 100
                
                
            uu.append(u)
            z.append(y)
            tt.append(t)
            t=t+1
            A=(1/(1/delta**2)+((E*Wn)/delta))
            B=(Wn**2)*k
            C=(Wn**2)-(2/delta**2)
            D=(1/delta**2)-((E*Wn)/(delta))
            y=(1/A)*(B*uu[t-1]-C*z[t-1]-D*z[t-2])
            #print(y)

           
    '''guardar txt de entradas'''
    inputs = list(uu)
    np.savetxt('inputs.txt', inputs)
    outputs = list(z)
    np.savetxt('outputs.txt', outputs)

    '''Grafica respuesta escal
    on'''
    tt = np.transpose(tt)
    plt.plot(z, color = "red")
    plt.plot(uu, color = "blue")
    plt.legend()
    plt.show()

#def input_norm(vec, u_min, u_max):
