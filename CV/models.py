from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Manager personalizado sin soporte para superusuarios
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

# Modelo de usuario personalizado
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)  # Para activar/desactivar usuarios

    # Asignamos el UserManager personalizado
    objects = CustomUserManager()

    # Campo que se usa como identificador único para la autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Campos requeridos además del USERNAME_FIELD

    def __str__(self):
        return self.email

# Modelo para el perfil del usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    nationality = models.CharField(max_length=50, blank=True, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.full_name

# Modelo para la educación del usuario
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="educations")
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.degree} - {self.institution_name}"

# Modelo para la experiencia laboral del usuario
class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

# Modelo para habilidades
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=50, default='Unknown Skill')
    level = models.CharField(max_length=50, default='Beginner')

    def __str__(self):
        return self.skill_name

# Modelo para certificaciones
class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="certifications")
    certification_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.certification_name


