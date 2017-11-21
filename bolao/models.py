from django.db import models


class Time(models.Model):
    sigla = models.CharField(max_length=3)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.sigla + " - " + self.nome


class Partida(models.Model):
    local = models.CharField(max_length=50)
    time1 = models.ForeignKey(Time, related_name='time1')
    time2 = models.ForeignKey(Time, related_name='time2')
    placar_time1 = models.IntegerField(blank=True, null=True)
    placar_time2 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.time1.sigla + " X " + self.time2.sigla



class Aposta(models.Model):
    valor=models.IntegerField()
    aposta = models.ForeignKey(Partida)
    placa_1=models.IntegerField()
    placa_2=models.IntegerField()


    def __str__(self):
        return str(self.placa_1) + " X " + str(self.placa_2)
    
    

     
        
