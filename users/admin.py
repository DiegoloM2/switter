from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



# Register your models here.
from .models import CustomUser

#First, inherit from UserAdmin
class CustomUserAdmin(UserAdmin):

    #Then, override the 'list_display' attribute so that only fields that exist are displayed.
    list_display = ('email', 'date_joined', "last_login", "is_admin", "is_staff",)

    #Then create the search fields you want.
    search_field = ("email",)

    readonly_fields = ('date_joined', "last_login",)


    #These are all default UserAdmin attributes that we have to change 
    #in order not to have errors (since the default User Admin has a 'username' field)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),    
    )

    ordering = ("email",)


#Last, add to the admin site
admin.site.register(CustomUser, CustomUserAdmin)

