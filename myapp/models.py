from django.db import models

# Create your models here.



class Region(models.Model):
    regionName = models.CharField( max_length=100, verbose_name='viloyat nomi')
   
    def __str__(self):
        return self.regionName
    
    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'


class Gender(models.Model):
    genders = models.CharField( max_length=100, verbose_name='Jinsi nomi')

    def __str__(self):
        return self.genders
    
    class Meta:
        verbose_name = 'Jins'
        verbose_name_plural = 'Jinslar'


class ApplicationType(models.Model):
    name = models.CharField( max_length=100, verbose_name='Murojat turi')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Murojat turi'
        verbose_name_plural = 'Murojat turi'


class Post(models.Model):
    username = models.CharField( max_length=100, verbose_name='Familiya')
    name = models.CharField( max_length=100, verbose_name='ism')
    address = models.CharField( max_length=200, verbose_name='Manzil')
    tel_number = models.CharField(max_length=15, verbose_name="Tell raqam")
    email = models.EmailField( max_length=254, verbose_name='email')
    topic = models.CharField(blank=True, null=True, max_length=255, verbose_name="Murajatni qisqacha mazmuni")
    body = models.TextField(blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    application_type = models.ForeignKey(ApplicationType, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'So\'rovlar'
        verbose_name_plural = 'So\'rovlar'
        ordering = ['-id']