from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Last Name")
    )
    phone_number = models.CharField(
        max_length=15,  
        validators=[
            RegexValidator(
                regex=r'^[+]{1}(?:[0-9\-\(\)\/\.]\s?){6, 15}[0-9]{1}$',
                message=_("Phone number must be entered in the format: '+91xxxxxxxxxx'. Up to 15 digits allowed.")
            )
        ]
    )
    age = models.PositiveIntegerField(
        verbose_name=_("Age"),
        validators=[
            MinValueValidator(0, message=_("Age must be positive")),
            MaxValueValidator(100, message=_("Age must be less than or equal to 100"))
        ],
        null=True
    )
    monthly_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Monthly Salary"),
        validators=[
            MinValueValidator(0, message=_("Monthly salary cannot be negative"))
        ]
    )
    approved_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Approved Limit"),
        validators=[
            MinValueValidator(0, message=_("Approved limit cannot be negative"))
        ]
    )
    current_debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Current Debt"),
        validators=[
            MinValueValidator(0, message=_("Current debt cannot be negative"))
        ],
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
