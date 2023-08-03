
# Red Neuronal artificial aplicada a Sistemas dinámicos

Red neuronal artificial para sistema dinámico de segundo orden.




![Logo](https://1000marcas.net/wp-content/uploads/2020/11/Python-logo.jpg)




## Descripción

Se crea una red de aprendizaje, donde se debe aprender
ciertos comportamientos del sistema, en este caso son escalones aplicados a una función de transferencia de segundo orden. 
Posterior de su entrenamiento, se crea una base da datos aleatoria para probar el aprendizaje de la red, con el objetivo de ser evaluada en escalones donde no tuvo información en su proceso de aprendizaje, pero que debe responder de una muy buena manera ya que esta red está teoricamente entrenada para cada punto que se desee evaluar, dependiendo de la respuesta que de, se concluye sobre su aprendizaje.
El algoritmo de predicción implementado para la RNA utilizó dos regresores de entradas y salidas.
En este algoritmo se varian la cantidad de neuronas de entrada, capas ocultas, neuronas de capas ocultas y funciones de activación hasta obtener el mejor resultado posible. 


## Uso

Primero : Se debe crear la función de transferencia , los escalones y su duración en el archivo RedDinamica

Segundo : Se debe entrenar la red definiendo neuronas, capas , epocas, funciones de activación en Red_aprendizaje1

Tercero : Cargar la red entrenada en el archivo cargar_red

Cuarto : Se evidencia gráficamente los resultados de la red entrenada evaluandola en una base de datos aleatoria, que se genera cada vez que se ejecuta, esto debe ser en Prueba_Modelo

Nota: Se debe tener en la misma carpeta function_models, que es una librería propia, creada para múltiples propósitos.
