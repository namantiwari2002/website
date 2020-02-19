from django.db import models
from django.contrib.auth.models import User
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

BATCH = (
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
    ("2024", "2024"),
    ("None", "None"),
)
ADDRESS_TYPE = (
    ("H", "Home Address"),
    ("W", "Work/Office Address")
)



class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    is_merchant = models.BooleanField(default=False)
    department = models.CharField(max_length=120, choices=DEPARTMENTS, default='None')
    club = models.CharField(max_length=120, choices=CLUBS, default='None')
    batch = models.CharField(max_length=4, choices=BATCH, default='None')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_email(self):
        return f'{self.user.email}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, img.width*(img.height/300))
            img.thumbnail(output_size)
            img.save(self.image.path)


class Address(models.Model):
    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)
    zip = models.CharField(max_length=10, blank=False, null=False)
    house_no = models.CharField(max_length=120, blank=False, null=False)
    area = models.CharField(max_length=120, blank=False, null=False)
    city = models.CharField(max_length=120, blank=False, null=False)
    state = models.CharField(max_length=120, blank=False, null=False)
    landmark = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120, blank=False, null=False)
    mobile_no = models.CharField(max_length=10, blank=False, null=False)
    alternate_no = models.CharField(max_length=10, blank=True, null=True)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPE, default='H')

    def __str__(self):
        return str(self.user.username)

    # def get_fulladdress(self):



