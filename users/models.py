from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
    ProhibitNullCharactersValidator
)
from django.urls import reverse

US_STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=12,
        null=False,
        validators=[
            MinLengthValidator(12),
            MaxLengthValidator(12),
            RegexValidator("^\d{3}-\d{3}-\d{4}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    street_address = models.CharField(
        max_length=40,
        null=False,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(40),
            RegexValidator("^\d{1,5} [a-zA-Z0-9\. ]+$"),
            ProhibitNullCharactersValidator()
        ]
    )
    city = models.CharField(
        max_length=25,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(25),
            RegexValidator("^[a-zA-Z\. -']+$"),
            ProhibitNullCharactersValidator()
        ]
    )
    state = models.CharField(
        max_length=2,
        null=True,
        choices=US_STATES,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(2),
            RegexValidator("^[A-Z]{2}$"),
            ProhibitNullCharactersValidator()
        ]
    )
    zipcode = models.CharField(
        max_length=5,
        null=True,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(5),
            RegexValidator("^\d{5}$"),
            ProhibitNullCharactersValidator()
        ]
    )

    @property
    def name(self):
        return self.first_name + " " + self.last_name
    
    @property
    def address(self):
        return self.street_address + ", " + self.city + ", " + self.state + " " + self.zipcode

    def get_absolute_url(self):
        return reverse("base:home")