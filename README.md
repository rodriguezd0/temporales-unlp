# Controles temporales
Mini libreria con posibilidad de crear cronómetros o temporizadores

## Uso de la librería

#### Cronómetro
###### Inicializar un cronómetro
Antes de utilizar los métodos se debe inicializar el cronómetro
```python
import temporales
c = temporales.cronometro()
```

###### Iniciar el contador del cronómetro
El cronómetro comenzará a contar desde 0 segundos
```python
c.iniciar()
```

###### Pausar el cronómetro
Detiene el cronómetro temporalmente
```python
c.pausar()
```

###### Despausar el cronómetro
```python
c.despausar()
```
###### Detener el cronómetro
Este método detiene permanentemente el cronómetro
```python
c.detener()
```
###### Obtener el tiempo
Este método retorna una variable de tipo datetime.timedelta que contiene las horas minutos, segundos y milisegundos del cronómetro
```python
c.tiempo()
```


#### Temporizador

###### Inicializar un temporizador
Antes de utilizar el método tiempo hay que inicializar el temporizador con sus respectivas variables:

```python
import temporales
t = temporales.temporizador()
```

###### Iniciar el temporizador
En este ejemplo, el temporizador es de solo 10 segundos
```python
t.iniciar(horas=0,minutos=0,segundos=10)
```

Este método retorna una tupla que contiene el tiempo y una variable que indica si el temporizador finalizó
```python
t.tiempo()
```
Ejemplo de salida
```python
print(t.tiempo())
> (datetime.timedelta(seconds=15, microseconds=188966), False)
```

## Ejemplos de programas
Saber cuánto tardó el usuario en ingresar una palabra
```python
from temporales import cronometro
import string

cronometro = cronometro()
cronometro.iniciar()
texto = input('Ingresa un texto: ')
cronometro.detener()

horas, minutos, segundos = str(cronometro.tiempo()).split(':')
print(f'{horas} horas \n{minutos} minutos \n{segundos} segundos')

```

Cuenta atras de 10 segundos
```python
from temporales import temporizador

t = temporizador()
t.iniciar(segundos=10)
tiempo = t.tiempo()
while not tiempo[1]:
    print(tiempo[0])
    tiempo = t.tiempo()
```

Redondear segundos en la cuenta atras de 10 segundos
```python
from temporales import temporizador

t = temporizador()
t.iniciar(segundos=3)
tiempo = t.tiempo()

while not tiempo[1]:
    horas, minutos, segundos = str(tiempo[0]).split(':')
    print(f'{horas}:{minutos}:{segundos.split(".")[0]}')
    tiempo = t.tiempo()
```


Imprimir caracteres aleatorios durante 1 segundo
```python
from temporales import temporizador
import random

temporizador = temporizador()
temporizador.iniciar(segundos=1)
tiempo = temporizador.tiempo()
lista_de_caracteres = "!@#$%^&*()_+{}./,"
caracteres = 0
while not tiempo[1]:
    print(random.choice(lista_de_caracteres), end='')
    caracteres+=1
    tiempo = temporizador.tiempo()

print(f'\nFinalizado, se imprimieron {caracteres} caracteres')

```

El usuario solo tiene 3 segundos para escribir algo!
```python
from temporales import temporizador
import threading

aceptar = True

def contar_tiempo():
    global aceptar
    temp = temporizador()
    temp.iniciar(segundos=3)
    tiempo = temp.tiempo()
    while not tiempo[1] and aceptar:
        tiempo = temp.tiempo()
    aceptar = False


threading1 = threading.Thread(target=contar_tiempo)
threading1.start()

while aceptar:
    texto = input('Ingresa algo, RAPIDO: ')
    if not aceptar:
        print('Tardaste mucho')
    else:
        aceptar = False
```
