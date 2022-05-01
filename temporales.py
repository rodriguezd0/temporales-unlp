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
            tiempo = datetime.now() - self.tiempo_inicial
        else:
            tiempo = self.tiempo_detenido

        return tiempo

class temporizador:
    detenido = False

    def iniciar(self,horas=0,minutos=0,segundos=0):
        self.tiempo_inicial = datetime.now()
        self.horas = int(horas)
        self.minutos = int(minutos)
        self.segundos = int(segundos)

    def tiempo(self):
        if not (self.detenido):
            horas, minutos, segundos = str(datetime.now()-self.tiempo_inicial).split(':')
            if int(horas) == self.horas and int(minutos) == self.minutos and int(float(segundos)) == self.segundos:
                self.detenido = True
            tiempo = datetime.now() - self.tiempo_inicial

        return tiempo, self.detenido
