from django.contrib import admin
from django.utils.html import format_html
from .models import Event, EventPhoto, Certificate

class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 1
    readonly_fields = ['photo_preview']
    
    def photo_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "Нет изображения"
    photo_preview.short_description = "Предпросмотр"

class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'status_display')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('status_display',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'date', 'location')
        }),
        ('Регистрация', {
            'fields': ('registration_link',),
            'classes': ('collapse',),
            'description': 'Ссылка на форму регистрации (например, Google Forms)'
        }),
        ('Результаты', {
            'fields': ('achieved_places', 'status_display'),
            'classes': ('collapse',),
            'description': 'Заполняется после завершения мероприятия'
        }),
    )
    
    inlines = [EventPhotoInline, CertificateInline]
    
    def status_display(self, obj):
        if obj.status == "upcoming":
            return format_html(
                '<span style="color: green;">Предстоящее</span>'
            )
        return format_html(
            '<span style="color: blue;">Завершенное</span>'
        )
    status_display.short_description = "Статус"

@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('event', 'description', 'photo_preview', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('event__title', 'description')
    
    def photo_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "Нет изображения"
    photo_preview.short_description = "Фото"

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('event', 'title', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('event__title', 'title')
