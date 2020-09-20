from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published','Published'),)


    title   = models.CharField(max_length = 255)
    slug    = models.SlugField(max_length=250, unique_for_date='publish')
    text    = models.TextField()
    author  = models.ForeignKey(User,
                        on_delete=models.CASCADE,
                        related_name='blog_posts')

    publish = models.DateTimeField(default=timezone.now)
    date    = models.DateField(auto_now_add=True)
    status  = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')

    image = models.ImageField(upload_to='model/img/', blank=True, null=True)
    image_alt = models.CharField(max_length = 255, default= "")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day, self.slug])

    

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.