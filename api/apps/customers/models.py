from django.db import models #type: ignore

class Gender(models.TextChoices):
    MASCULINO    =   'M'
    FEMENINO  =   'F'

class CustomerType(models.Model):
    
    # id default pk 
    name            = models.CharField(max_length=12, 
                                       unique=True)
    state           = models.BooleanField(default=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(null=True, 
                                           auto_now=True)
    
    class Meta:
        db_table = "customer_type"        
    
class Customer(models.Model):
   
    # id default pk
    first_name      =   models.CharField(max_length=100)
    last_name       =   models.CharField(max_length=180)
    sex             =   models.CharField(max_length=1,
                                         choices=Gender.choices)
    state           =   models.BooleanField(default=True)
    birthdate       =   models.DateField(null=True, default=None)
    created_date    =   models.DateTimeField(auto_now_add=True)
    updated_date    =   models.DateTimeField(null=True, 
                                             auto_now=True)
    customer_type_id    =   models.ForeignKey(CustomerType, 
                                          on_delete=models.PROTECT)
    class Meta:
        db_table = "customer"  