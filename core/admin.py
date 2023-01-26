from django.contrib import admin

from core.models import User

# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # inlines = (GenreFilmworkInline, PersonFilmworkInline,)
    # # Отображение полей в списке
    list_display = ('username', 'email', 'first_name',
                    'last_name')

    # Фильтрация в списке
    list_filter = ('is_staff','is_active', 'is_superuser',)

    search_fields = ('emailfirst_name', 'last_name', 'username')

    exclude = ['password']
    readonly_fields = ['last_login', 'date_joined',]
