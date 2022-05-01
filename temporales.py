from datetime import datetime
import string

class cronometro:
    pausado = False
    detenido = False

    def iniciar(self):
        self.tiempo_inicial = datetime.now()


    def pausar(self):
        self.tiempo_detenido = self.tiempo()
        self.pausado = True


    def despausar(self):
        self.tiempo_inicial = datetime.now() - self.tiempo_detenido
        self.pausado = False


    def detener(self):
        self.tiempo_detenido = self.tiempo()
        self.detenido = True


    def tiempo(self):
        if not (self.detenido or self.pausado):
            return datetime.now() - self.tiempo_inicial
        else:
            return self.tiempo_detenido

class temporizador:
    detenido = False
    def iniciar(self,horas=0,minutos=0,segundos=0):
        self.tiempo_inicial = datetime.now()
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def tiempo(self):
        horas, minutos, segundos = str(datetime.now()-self.tiempo_inicial).split(':')
        tiempo = datetime.now() - self.tiempo_inicial
        if int(horas) >= self.horas and int(minutos) >= self.minutos and int(float(segundos)) >= self.segundos:
            return tiempo, True
        else:
            return tiempo, False
