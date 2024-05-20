from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def email_validator(self,email):
        try:
            validate_email(email)
            return email
        except ValidationError:
            raise ValidationError(_("Please enter a valid email address"))
    
    def create_user(self, email, first_name, last_name, phone_number, password=None, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValidationError(_("Please enter a valid email address"))
        
        if not first_name:
            raise ValidationError(_("Please enter a valid first name"))
        if not phone_number:
            raise ValidationError(_("Please enter a valid phone number"))
        if not last_name:
            raise ValidationError(_("Please enter a valid last name"))
        
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValidationError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValidationError(_("Superuser must have is_superuser=True."))
        # if extra_fields.get("is_verified") is not True:
        #     raise ValidationError(_("Superuser must have is_verified=True."))
        user = self.create_user(email, first_name, last_name, phone_number, password, **extra_fields)
        user.save(using=self._db)
        return user