from django.contrib import admin

from oat.domain.colors_token import ColorsToken
from oat.domain.user import User

class ColorsTokenAdmin(admin.ModelAdmin):
    list_display = [
        'first_color',
        'second_color',
        'date_start',
        'date_end',
        'pattern'
    ]


admin.site.register(ColorsToken, ColorsTokenAdmin)
admin.site.register(User)

