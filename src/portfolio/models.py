from django.db import models


def ability_directory_path(instance, filename):
    name = instance.name.lower().replace(' ', '_')
    return f'abilities/{name}/{filename}'

class Ability(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=ability_directory_path)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def social_media_directory_path(instance, filename):
    social_media = instance.social_media.lower().replace(' ', '_')
    return f'social_medias/{social_media}/{filename}'

class SocialMedia(models.Model):
    social_media = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=social_media_directory_path, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.social_media


class Portfolio(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    social_medias = models.ManyToManyField(SocialMedia, related_name='portfolio_social_medias', blank=True)
    about_me = models.TextField()
    abilities = models.ManyToManyField(Ability, related_name='portfolio_abilities', blank=True)
    contacts = models.ManyToManyField(SocialMedia, related_name='portoflio_contacts', blank=True)
    is_active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.sub_title}'
