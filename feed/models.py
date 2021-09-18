from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='uploads', blank=True)
	upvote = models.ManyToManyField(User, related_name='upvote')
	downvote = models.ManyToManyField(User, related_name='downvote')

	def number_of_upvotes(self):
		return self.upvote.count()

	def number_of_downvotes(self):
		return self.downvote.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})


