from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Butler, Specialties, UserButlerSpecialty

@admin.register(User)
class UsuarioAdmin(UserAdmin):
        
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined', 'created_at')}),
    )
    readonly_fields = ['created_at', 'last_login', 'date_joined']


@admin.register(Butler)
class ButlerAdmin(admin.ModelAdmin):
    model = Butler
    list_display = ('name',)


@admin.register(Specialties)
class SpecialtiesAdmin(admin.ModelAdmin):
    model = Specialties
    list_display = ('name',)

@admin.register(UserButlerSpecialty)
class UserButlerSpecialtyAdmin(admin.ModelAdmin):
    model = UserButlerSpecialty
    list_display = ('user', 'butler')