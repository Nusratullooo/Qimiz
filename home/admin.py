from home.models import ContactMessage, Phone, Chef, About
from django.contrib import admin


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message', 'create_at']
    readonly_fields = ('name', 'surname', 'phone', 'email', 'message', 'create_at')


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone', 'create_at']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone']


class ChefAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Chef, ChefAdmin)
