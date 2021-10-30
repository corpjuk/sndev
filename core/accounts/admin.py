from django.contrib import admin

# Register your models here.
from accounts.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser']

admin.site.register(Account, AccountAdmin)



# email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=30, null=True, blank=True)
#     last_name = models.CharField(max_length=70, null=True, blank=True)
#     date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
