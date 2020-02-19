from django.db import models

# Create your models here.

class CoverLetter(models.Model):
    # _no, school_name, major, type, grade, question1, question2, question3, question4
    school_name = models.CharField(max_length = 200)
    major = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    grade = models.DecimalField(max_digits = 5, decimal_places = 2)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()

    def __str__(self):
        return self.school_name

        
