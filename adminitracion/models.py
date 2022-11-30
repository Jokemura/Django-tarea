from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField()

    class Meta:
        abstract = True

class Classroom(models.Model):
    teacher_id =  models.CharField(max_length=200)
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    def __str__(self) -> str:
        return self.name + ' - ' + str(self.start_time)

    class Meta:
        db_table= 'classroom'


class Student(Person):
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    grade_lab = models.FloatField(default= 0.0)
    grade_exam = models.FloatField(default=0.0)
    grade_final = models.FloatField(default=0.0)
    class Meta:
        db_table = 'Students'

class StudenProxy(Student):
    class Meta:
        ordering = ['-id']
        proxy = True
    def average(self):
        return self.grade_exam *0.1 + self.grade_lab*0.6 +self.grade_final*0.3


class Teacher(Person):
    
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    class Meta:
        db_table = 'teachers'


class TecherProxy(Teacher):
    class Meta:
        proxy = True
    
    def bonus(self):
        return self.salary + self.rating * 100

#TAREA

class Evaluacion (models.Model):
    date = models.DateField(default=" ")
    curso = models.CharField(max_length=30)
    evaluador = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Examen_Final(Evaluacion):
    duracion_examen = models.IntegerField()
    numero_preguntas = models.IntegerField()
    puntaje_total = models.IntegerField()
    
class Examen_Final_Proxy(Examen_Final):
    class Meta:
        proxy = True
        
    def puntaje_pregunta(self):
        return self.numero_preguntas/ self.puntaje_total

class Proyecto (Evaluacion):
    tema_proyecto = models.CharField(max_length=100)
    num_grupos = models.IntegerField(default=" ")

class Proyecto_Proxy(Proyecto):

    class Meta:
        proxy = True
        ordering = ["tema_prooyecto"]




