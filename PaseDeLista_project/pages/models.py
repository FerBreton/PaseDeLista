from django.db import models

# Create your models here.

#modelo de alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#modelo de materia
class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    periodo = models.CharField(max_length=30)
    year = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.nombre

#modelo de clase
class Clase(models.Model):
    fecha_clase = models.CharField(max_length=50)
    grupo = models.CharField(max_length=10)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.grupo

#modelo de profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#modelo de asistencia
class Asistencia(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha_asistencia = models.DateField()

    def __str__(self):
        return self.alumno.nombre