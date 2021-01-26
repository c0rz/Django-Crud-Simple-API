from django.db import models

# Create your models here.


class Mahasiswa(models.Model):
    nama_lengkap = models.CharField(max_length=70, blank=False, default='')
    umur = models.IntegerField(blank=False, default=1)
    status = models.BooleanField(default=False)
