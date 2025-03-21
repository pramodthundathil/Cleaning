from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The username field to be set")
        username = self.normalize_email(username)
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user 
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault("role", "admin")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have superuser status is True ')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have staff status is True ')
        
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, verbose_name='username')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="active")
    is_staff = models.BooleanField(default=False, verbose_name="staff")
    date_joined = models.DateTimeField(auto_now_add=True)
    pro_pic = models.FileField(upload_to="profile_pic", null=True, blank=True)
    role = models.CharField(max_length=20, choices=(("user","user"),('admin',"admin"),("merchant","merchant"),("service_provider","service_provider")), default='user')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["first_name","email"]


    class Meta:
        verbose_name='user'
        verbose_name_plural = "users"




class Chat_Messages(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receiver")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-created_at"]



class Service(models.Model):
    SERVICE_CATEGORIES = (
        ('home_cleaning', 'Home Cleaning'),
        ('office_cleaning', 'Office Cleaning'),
        ('carpet_cleaning', 'Carpet Cleaning'),
        ('window_cleaning', 'Window Cleaning'),
        ('deep_cleaning', 'Deep Cleaning'),
    )
    service_category = models.CharField(max_length=255, choices=SERVICE_CATEGORIES)
    rate_per_hour = models.FloatField()
    servicer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="services")
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)


class Service_booking(models.Model):
    booked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="booking")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_book')
    description = models.TextField(null=True, blank=True)
    date_of_booking = models.DateField(auto_now_add=True)
    booked_date = models.DateField(auto_now=False)
    approve = models.BooleanField(default=False)