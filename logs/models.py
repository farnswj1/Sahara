from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.timezone import now

# Create your models here.
class Log(models.Model):
    model_name = models.CharField(
        max_length=10,
        null=False,
        validators=[
            RegexValidator("^[A-Z]+$")
        ]
    )
    model_id = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(1)
        ]
    )
    action = models.CharField(
        max_length=6,
        null=False,
        validators=[
            RegexValidator("^(Create|Update|Delete)$")
        ]
    )
    timestamp = models.DateTimeField(null=False, default=now)

    def __str__(self):
        return f"{self.action} {self.model_name} (ID: {self.model_id})"

    class Meta:
        ordering = ("-timestamp",)