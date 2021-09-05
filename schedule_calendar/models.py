from django.db import models
from django.core.exceptions import ValidationError


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.end_date <= self.start_date:
            raise ValidationError("Erro ao criar tarefa. A data de início deve ser menor que a data do fim de uma tarefa.")
        super(Task, self).save(*args, **kwargs)

    class Meta:
        ordering = ['start_date']
