from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    use = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # use==user
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/%y/%m/%d", blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.slug} - {self.created}'

    def get_absolute_url(self):
        return reverse('home:postdetail', args=(self.id, self.slug))

    def likes_count(self):
        return self.post_vote.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply_comment', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:20]}'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vote')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_vote')

    def __str__(self):
        return f'{self.user} liked {self.post.slug}'
