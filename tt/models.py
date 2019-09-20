from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#class Users(models.Model):
#    user_email = models.EmailField(max_length=254, primary_key=True)
#    password = models.CharField(max_length = 50)
#    user_nickname = models.CharField(max_length = 200)

#    def __str__(self):
#        return self.user_nickname
    

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, primary_key=True)
    post_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('Posts')


class Like(models.Model):
    like_user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_value = models.IntegerField()
    like_date = models.DateTimeField(auto_now=True)


def __str__(self):
    return str(self.user) + ':' + str(self.post) + ':' + str(self.value)


class Meta:
    unique_together = ("user", "post", "value")
