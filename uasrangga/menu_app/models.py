from django.db import models


# Create your models here.

class Jenis(models.Model):
    jenis = models.CharField(max_length=30)
    macamnya = models.TextField()
    
    def __str__(self):
        return self.jenis
    
    
class Menu(models.Model):
    no = models.IntegerField(null=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
    paket = models.CharField(max_length=40)
    harga = models.IntegerField(null=True)
    gambar = models.CharField(max_length=50, null=True)
    pilihanmenu = models.TextField()
    
    def __str__(self):
        return self.paket

class Peta(models.Model):
    no = models.IntegerField(null=True)
    nama_lokasi = models.CharField(max_length=50)
    titik_koordinat = models.CharField(max_length=50)
    deskripsi = models.TextField(null=True)

    def __str__(self):
        return self.nama_lokasi    