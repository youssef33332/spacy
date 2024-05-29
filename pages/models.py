from django.db import models

# Create your models here.

#CV ---database API

#database------model AI       (score points)

#model AI --------database

#model AI ------output   API

#make model --------serializer(make it in json)----------restframwork(make API).

from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv_pdfs/')

    def __str__(self):
        return self.name
#*****************************************************************************************************************************







