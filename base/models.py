from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null=True)
    
    avatar = models.ImageField(null = True, default= "avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True) 
    name = models.CharField(max_length=200)
    # null = True means it can have null value and we have blank = true, which means we can have blank value in form from which it comes.
    description = models.TextField(null=True, blank=True)
    # Stores users active in the room
    participants = models.ManyToManyField(User, related_name = 'participants', blank = True)     
    # auto_now takes the snapshot every time we save 
    # auto_now_add only takes the snapshot when we create the instance.
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        # Order based on updated and created -updated -> Descending updated -> Ascending
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # If we do on_delete= models.SET_NULL, these messages will be there but values will be set to null.
    # But here we have used cascade, which means that we will delete that too in the child if deleted from the parent.
    # If a room is deleted, all the messages of that room will also be deleted.
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Order based on updated and created -updated -> Descending updated -> Ascending
        ordering = ['-updated', '-created']

    def __str__(self) :
        # In the preview, we do not want all the characters as it will be long, so we just have first 50 characters.
        return  self.body[0:50]
        
