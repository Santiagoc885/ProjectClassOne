from django.db import models
from django.contrib.auth.models import User

class Ideas(models.Model):
    INNOVATION_TYPES = [
        ('Incremental', 'Incremental'),
        ('Radical', 'Radical'),
        ('Transformacional', 'Transformacional'),
        ('Otro', 'Otro'),
    ]

    INNOVATION_FOCUS = [
        ('Modelo de Negocios', 'Modelo de Negocios'),
        ('Productos', 'Productos'),
        ('Servicios', 'Servicios')

    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    key_words = models.CharField(max_length=255, blank=True)
    resources = models.CharField(max_length=255, blank=True)
    innovation_type =  models.CharField(max_length=50, choices=INNOVATION_TYPES, default='Tipo de Innovación')
    innovation_focus= models.CharField(max_length=50, choices=INNOVATION_FOCUS, default='Foco de Innovación')
    created_at = models.DateField(blank=False, null=False) 
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    file = models.FileField(upload_to='videos/', null=True, blank=True)

        

    class Meta:
        db_table = 'tbl_ideas'
        verbose_name = 'Ideas'
        ordering=['title']


    def __str__(self):
        return self.title
