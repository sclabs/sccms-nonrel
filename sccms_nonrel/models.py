from django.db import models

class Comic(models.Model):
    number = models.IntegerField(primary_key = True)
    filename = models.CharField(max_length=100,
                                editable=False,
                                null=True,
                                blank=True)
    img_src = models.FileField(upload_to = 'comics/')
    title = models.CharField(max_length = 200)
    tooltip = models.TextField()
    date = models.DateField()
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.filename = self.img_src.name.rsplit('/', 1)[-1]
        super(Comic, self).save(*args, **kwargs)

    def img_url(self):
        return u'/' + self.img_src.name.split('/', 1)[1]
