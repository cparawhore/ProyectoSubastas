from django.db import models

class bcc(models.Model):
	pk_cu = models.IntegerField(max_length=11)
	saldo = models.FloatField()

class cloud_users(models.Model):
	cloud_user = models.CharField(max_length = 50,primary_key=True)
	enc_pass = models.CharField(max_length = 40)
	ste_acc = models.CharField(max_length = 200)
	ste_acc_trd = models.CharField(max_length=200)
	ste_acc_1 = models.CharField(max_length = 200)
	ste_acc_1_trd = models.CharField(max_length=200)
	verified = models.BooleanField(default=False)

class cl_compra(models.Model):
	cl_user = models.IntegerField(max_length=11)
	total = models.FloatField()
	estado = models.IntegerField(max_length=11)
	cant = models.IntegerField(max_length=11)
	id_compra = models.IntegerField(max_length=11)

class cl_compra_detalles(models.Model):
	id_item = models.CharField(max_length=9)
	precio = models.FloatField()
	cant = models.IntegerField(max_length=11)
	id_compra = models.IntegerField(max_length=11)

class hero_suge(models.Model):
	cuser = models.CharField(max_length=150)
	suge = models.CharField(max_length=150)

class items_cloud_d(models.Model):
	it_nombre = models.CharField(max_length=200)
	it_stock = models.IntegerField(max_length=11)
	it_precio = models.FloatField()
	it_aspecto = models.CharField(max_length=100)
	it_hero = models.CharField(max_length=100)
	it_id = models.CharField(max_length=11)
	it_img = models.CharField(max_length=500)
    #texto = models.TextField()
    #fecha = models.DateTimeField()
