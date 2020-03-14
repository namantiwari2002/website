from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from PIL import Image

DEPARTMENTS = (
    ("CE", "Chemical Engineering"),
    ("BioTech", "Biotechnology"),
    ("Civil", "Civil Engineering"),
    ("CSE", "Computer Science and Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EEE", "Electronics and Electrical Engineering"),
    ("EP", "Engineering Physics"),
    ("MnC", "Mathematics and Computing"),
    ("Mech", "Mechanical Engineering"),
    ("Design ", "Design "),
    ("BnB", "Biosciences and Bioengineering"),
    ("None", "None"),

)


CLUBS = (
    ("Alcher", "Alcheringa"),
    ("Cadence", "Cadence"),
    ("AnR", "Anchorenza and RadioG"),
    ("Fine Arts", "Fine Arts"),
    ("Montage", "Montage"),
    ("Lumiere", "Lumiere"),
    ("Octaves", "Octaves"),
    ("Expressions", "Expressions"),
    ("LitSoc-DebSoc", "LitSoc-DebSoc"),
    ("Aeromodelling", "Aeromodelling"),
    ("Astronomy", "Astronomy"),
    ("Coding", "Coding"),
    ("CnA", "Consulting and Analytics"),
    ("Electronics", "Electronics"),
    ("Prakriti", "Prakriti"),
    ("FnE", "Finance and Economics"),
    ("Robotics", "Robotics "),
    ("ACUMEN", "ACUMEN"),
    ("TechEvince", "TechEvince"),
    ("Green Automobile", "Green Automobile"),
    ("EDC", "Entrepreneurial Development Cell"),
    ("Udgam", "Udgam"),
    ("Techniche", "Techniche"),
    ("None", "None"),


)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    department = models.CharField(max_length=120, choices=DEPARTMENTS, default='None')
    club = models.CharField(max_length=120, choices=CLUBS, default='None')
    image = models.ImageField( default='default.jpg', upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    image1 = models.ImageField(upload_to='images/',blank=True,null=True )
    general = models.BooleanField(default=False)


    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = datetime.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image1.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image1.path)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Voter(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)