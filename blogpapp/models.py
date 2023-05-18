from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.shortcuts import reverse
# Create your models here.
class Home(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	about = models.TextField()
	copyright = models.CharField(max_length=255,blank=True,null=True)
	def __str__(self):
		return self.title
		

class Contact(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255,blank=True,null=True)
	email = models.CharField(max_length=255,blank=True,null=True)
	subject = models.CharField(max_length=255,blank=True,null=True)
	message = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name        

class Category(models.Model):
		id = models.AutoField(primary_key=True)
		category_title = models.CharField(max_length=255,blank=True,null=True)
		category_slug = AutoSlugField(populate_from='category_title',null=True)
		post_count = models.IntegerField()

		def __str__(self):
			return self.category_title

class TagDict(models.Model):
	id = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=255,blank=True,null=True)
	count = models.IntegerField(default=0)
	slug =  AutoSlugField(populate_from='title',null=True)
	count = models.IntegerField(default=0)
	def __str__(self):
		return self.tag  


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super().save(*args, **kwargs)

		for tag in self.tags.all():
			tag_dict,_ = TagDict.objects.get_or_create(tag=str(tag))
			tag_dict.count += 1
			tag_dict.save()

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=1000,blank=False,null=False)
	post_description = RichTextField()
	image = models.ImageField(upload_to='images',blank=True,null=True)
	imagealt = models.CharField(max_length=255,blank=True,null=True)
	tag = TaggableManager(blank=True)
	metadsc = models.CharField(max_length=255,blank=True,null=True)
	category_id = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	updated_on = models.DateTimeField(auto_now= True)
	created_on = models.DateTimeField(auto_now_add=True)
	read_count = models.IntegerField(default=0, editable=False)
	read_time = models.IntegerField(default=0, editable=False)
	STATUS_CHOICES = (('draft', 'Save Draft'), ('published', 'Published'))
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	slug = AutoSlugField(populate_from='title',null=True)

	def __str__(self):
		return self.title  

	def get_absolute_url(self):
		return  f'/post/{self.slug}'