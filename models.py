from django.db import models


class InnovationType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'tipo_innovacion'
        verbose_name = 'Tipo de Innovacion'
        verbose_name_plural = 'Tipo de Innovaciones'

    def __str__(self):
        return self.name

class InnovationFocus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'foco_innovacion'
        verbose_name = 'Foco de Innovacion'
        verbose_name_plural = 'Focos de Innovacion'

    def __str__(self):
        return self.name


class Ideas(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    key_words = models.CharField(max_length=255, blank=True)
    resources = models.CharField(max_length=255, blank=True)
    innovation_type = models.ForeignKey(InnovationType, on_delete=models.SET_NULL, null=True)
    innovation_focus = models.ForeignKey(InnovationFocus, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(blank=False, null=False)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    file = models.FileField(upload_to='videos/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'idea'
        verbose_name = 'Idea'
        ordering = ['title']



