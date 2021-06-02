from django.db import models
from django.contrib.auth.models import User


class Reportes(models.Model):
    MES = (
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    )

    AÑO = (
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
    )
    nombre = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mes = models.CharField(null=True, max_length=100, choices=MES)
    año = models.CharField(null=True, max_length=100, choices=AÑO)
    archivo = models.FileField(null=True, upload_to='archivos/reportes')

    class Meta:
        verbose_name_plural = 'Reportes'

    def __str__(self):
        txt = "{0} reporte de {1} {2}"
        return txt.format(self.nombre.username, self.mes, self.año)


class Declaraciones(models.Model):
    MES = (
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    )

    AÑO = (
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
    )
    nombre = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mes = models.CharField(null=True, max_length=100, choices=MES)
    año = models.CharField(null=True, max_length=100, choices=AÑO)
    archivo = models.FileField(null=True, upload_to='archivos/declaraciones')

    class Meta:
        verbose_name_plural = 'Declaraciones'

    def __str__(self):
        txt = "{0} declaracion de {1} {2}"
        return txt.format(self.nombre.username, self.mes, self.año)
