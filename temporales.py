from datetime import datetime
from datetime import timedelta
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
        self.objetivo = self.tiempo_inicial+timedelta(hours=horas,minutes=minutos,seconds=segundos)

    def tiempo(self):
        tiempo = self.objetivo - datetime.now()
        horas, minutos, segundos = str(tiempo).split(':')
        try:
            if int(horas) <= 0 and int(minutos) <= 0 and float(segundos) <= 0:
                return tiempo, True
            else:
                return tiempo, False
        except:
            return 0, True
