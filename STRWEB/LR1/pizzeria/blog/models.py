from django.db import models


class CompanyInfo(models.Model):
    description = models.TextField()

    def __str__(self):
        return "Company Information"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Review(models.Model):
    user_name = models.CharField(max_length=200)
    title = models.TextField()
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review


class LogoCompanies(models.Model):
    company_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.company_name
