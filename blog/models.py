from django.db import models
# 다른 파일에 있는 것을 추가 하세요 
from django.utils import timezone


# Post 클래스 정의 
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	# 게시 함수 
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

# Create your models here.
