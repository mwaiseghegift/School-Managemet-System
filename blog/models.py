from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils.text import slugify
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse
from ckeditor.fields import RichTextField

from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    view_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super(Category, self).save(*args, **kwargs)
    
    def get_tag_blogs(self):
        return Blog.objects.filter(category=self)
    
class BlogTags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super(BlogTags, self).save(*args, **kwargs)
    
    def get_tag_blogs(self):
        return Blog.objects.filter(tag=self)
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="images/blog")
    pic_thumbnail = ImageSpecField(source='pic',
                                   processors = [ResizeToFill(1920,1080)],
                                   format='JPEG',
                                   options = {'quality':100})
    content = RichTextField()
    tags = TaggableManager()
    pub_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return f"{self.uploaded_by.blog_name} - {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog,self).save(*args, **kwargs)
    
    def get_blog_tags(self):
        return self.tags.all()

    def get_blog_comments(self):
        return BlogComment.objects.filter(post=self)

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"slug":self.slug, "pk": self.pk})
    
    
class BlogComment(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, 
                null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['timestamp']

    def __str__(self):
        return f"{self.post.title} - {self.content}"
    
    