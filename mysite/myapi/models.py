from django.db import models

# Create your models here.
class Channel(models.Model):
    title = models.CharField(max_length=60)
    language = models.CharField(max_length=60)
    picture = models.BinaryField()
    #cahnnel = models.ForeignKey(self, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Content(models.Model):
    file = models.BinaryField()
    title = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    genere = models.CharField(max_length=60)
    rating = models.IntegerField()
    cahnnel = models.ForeignKey(Channel, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
