from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone


class About(models.Model):
    title = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Chef(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
