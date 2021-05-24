from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	Bio =models.CharField(max_length=500, null=True)
	Organization=models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.name



class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class event(models.Model):
	CATEGORY = (
			('web', 'Web Development'),
			('AI & ML', 'AI & ML'),('industry 4.0','Industry 4.0'),('cyber','Cyber Security'),('other','Others'),
			) 

	Event_Title = models.CharField(max_length=200,unique=True, null=True)
	Event_Date= models.DateField(null=True)
	Event_Time=models.TimeField(null=True)
	Event_Location= models.CharField(max_length=800, null=True)
	Max_NO_Participants=models.IntegerField()
	Event_Banner=models.ImageField()
	description = models.TextField(null=True)
	Meet_link=models.CharField(blank=True,max_length=2000,default='none')
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# tags = models.ManyToManyField(Tag)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	count=models.IntegerField(null=True,)
	count2=models.IntegerField(null=True,)
	cancel_event=models.BooleanField(null=True, default=False)
	

	def __str__(self):
		return self.Event_Title







class register(models.Model):
	STATUS = (
			
			('YES', 'YES'),
			('MAYBE','MAYBE'),
			('NO', 'NO'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL,)
	event_name = models.ForeignKey(event, null=True, on_delete= models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	Organization=models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='NO')
	count=models.IntegerField(null=True,)
	

	def __str__(self):
		return self.name
