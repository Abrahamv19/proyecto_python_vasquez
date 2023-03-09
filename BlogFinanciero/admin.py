from django.contrib import admin
from BlogFinanciero.models import Post_bloguero, Post_lector, Post_temas

# Register your models here.
admin.site.register(Post_bloguero)
admin.site.register(Post_lector)
admin.site.register(Post_temas)

