from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER1 = "USER1", "User1"
        LAWYER = "LAWYER", "Lawyer"

        NOTARY = "NOTARY", "Notary"  # Add the new role

    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if isinstance(self, Lawyer):
                self.role = User.Role.LAWYER
            elif isinstance(self, User1):
                self.role = User.Role.USER1
            elif isinstance(self, Notary):  # Set role to Notary for Notary instances
                self.role = User.Role.NOTARY
            else:
                self.role = User.Role.USER1  # Default role for regular users
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    

class Notary(User):  # Define Notary model similar to Lawyer
    # Add fields specific to Notary if needed
    Notary_license = models.CharField(max_length=50, blank=True)
    practice_areas = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    subscription_plan = models.ForeignKey('SubscriptionPlan', on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.role = User.Role.NOTARY  # Set the role to NOTARY for NOTARY instances
        super().save(*args, **kwargs)


class Lawyer(User):
    lawyer_license = models.CharField(max_length=50, blank=True)
    practice_areas = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    email_verified = models.BooleanField(default=False) 
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.role = User.Role.LAWYER  # Set the role to Lawyer for Lawyer instances
        super().save(*args, **kwargs)


class User1(User):
   
    base_role = User.Role.USER1
    
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the instance is new
            self.role = self.base_role  # Set the role to User1 for new instances
        super().save(*args, **kwargs)  # Call the save method of the base class
    class Meta:
        proxy = True

    def welcome(self):
        return "Only for users"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    subscription_end_date = models.DateTimeField(null=True, blank=True)
    subscription_plan = models.ForeignKey('SubscriptionPlan', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


            
class Message(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', null=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    file = models.FileField(upload_to='uploads/', null=True)  # Add a file field
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
         return f"Message from {self.sender_id.username} to {self.recipient.username}"



class LawyerClient(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='accepted_clients')
    user1 = models.ForeignKey(User1, on_delete=models.CASCADE, related_name='lawyer_clients')
    date = models.DateField(default=timezone.now)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    finalized = models.BooleanField(default=False,null=True)
    def __str__(self):
        return f"{self.lawyer.user.username} accepts {self.user1.user.username}"



class conseil(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class tribunal(models.Model):
    college = models.ForeignKey(conseil, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class lawyerclients(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)

    Fname = models.CharField(max_length=60)
    Sname = models.CharField(max_length=60)
    date = models.DateField()
    email = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    numcarte=models.IntegerField()
    datecarte=models.DateField()
class notaryclients(models.Model):
    notary = models.ForeignKey(Notary, on_delete=models.CASCADE)

    Fname = models.CharField(max_length=60)
    Sname = models.CharField(max_length=60)
    date = models.DateField()
    email = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    numcarte=models.IntegerField()
    datecarte=models.DateField() 
# add affair
class Aff(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='aff_lawyer_clients')
    Naff = models.IntegerField()
    Nomclient = models.CharField(max_length=60)
    NATURE_CHOICES = [
        ('مدعى', 'مدعى'),
        ('مدعى عليه', 'مدعى عليه'),
        ('جاني', 'جاني'),
        ('مجنى عليه', 'مجنى عليه'),
        # Add more choices as needed
    ]

    JUDGMENT_CHOICES = [
        ('جنائي', 'جنائي'),
        ('مدني', 'مدني'),
        ('إداري', 'إداري'),
        ('أسري', 'أسري'),
        ('تجاري', 'تجاري'),
        ('عمالي', 'عمالي'),
        # Add more choices as needed
    ]

    ETAPE_CHOICES = [
        ('ابتدائي', 'ابتدائي'),
        (' جزئي', ' جزئي'),
        ('نقض', 'نقض'),
        ('استئناف ', ' استئناف'),
        # Add more choices as needed
    ]

    ETAT_CHOICES = [
        ('منتهية', 'منتهية'),
        (' معلقة', ' معلقة'),
        ('تحت الدراسة', 'تحت الدراسة'),
        ('مرفوضة ', ' مرفوضة'),
        # Add more choices as needed
    ]
    # Assuming NATURE_CHOICES and JUDGMENT_CHOICES are defined somewhere
    CLIENT_CHOICES = NATURE_CHOICES
    typeclient = models.CharField(max_length=20, choices=CLIENT_CHOICES, default='مدعى')

    adversaire = models.CharField(max_length=60)
    adresse = models.CharField(max_length=100)
    avocat = models.CharField(max_length=100)

    # Assuming affaire_CHOICES, etape_CHOICES, etat_CHOICES are defined somewhere
    affaire_CHOICES = JUDGMENT_CHOICES
    taffaire = models.CharField(max_length=20, choices=affaire_CHOICES, default='جنائي')

    etape_CHOICES = ETAPE_CHOICES
    etapeaffaire = models.CharField(max_length=20, choices=etape_CHOICES, default='ابتدائي')

    etat_CHOICES = ETAT_CHOICES
    etataffaire = models.CharField(max_length=20, choices=etat_CHOICES, default='منتهية')

    # Define ForeignKey relationships
    conseil_associated = models.ForeignKey(conseil, on_delete=models.SET_NULL, null=True, blank=True)
    tribunal_associated = models.ForeignKey(tribunal, on_delete=models.SET_NULL, null=True, blank=True)
    sujet = models.CharField(max_length=60)
    budjet = models.FloatField()
    date=models.DateField()
    details=models.TextField() 
    tel=  models.IntegerField()

#jalssa
class Seance(models.Model):
    aff = models.ForeignKey(Aff, on_delete=models.CASCADE)
    titre = models.CharField(max_length=60)
    date = models.DateTimeField()
    remarques = models.CharField(max_length=1000)


class decision(models.Model):
   aff = models.ForeignKey(Aff, on_delete=models.CASCADE, default=None)
   date = models.DateField()
   detail = models.CharField(max_length=1000)

class paiement(models.Model):
   
    aff = models.ForeignKey(Aff, on_delete=models.CASCADE)
    versement = models.FloatField()
    date = models.DateTimeField()




class Documents(models.Model):
    aff = models.ForeignKey(Aff, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    max_accepted_clients = models.PositiveIntegerField(null=True, blank=True)
    duration = models.CharField(null=True, max_length=50, choices=[('month', 'Month'), ('1_year', '1 Year'), ('6_months', '6 Months')])

    def __str__(self):
        return self.name

class rdv(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    date = models.DateTimeField()
    remarques = models.CharField(max_length=1000)
class nrdv(models.Model):
    notary = models.ForeignKey(Notary, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    date = models.DateTimeField()
    remarques = models.CharField(max_length=1000)

    
class npaiements(models.Model):
    notary = models.ForeignKey(Notary, on_delete=models.CASCADE)
    fpartie = models.CharField(max_length=60)
    spartie = models.CharField(max_length=60)
    date = models.DateField()
    type = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    prix = models.FloatField()
    remarques = models.CharField(max_length=120)


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True)  # Add this field

    def __str__(self):
        return self.title
class NotaryClient(models.Model):
    notary = models.ForeignKey(Notary, on_delete=models.CASCADE, related_name='accepted_clients')
    user1 = models.ForeignKey(User1, on_delete=models.CASCADE, related_name='notary_clients')
    date = models.DateField(null=True)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)



    
    def _str_(self):
        return f"{self.notary.user.username} accepts {self.user1.user.username}"