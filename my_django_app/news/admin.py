from django.contrib import admin
from .models import Articles, Logs, Qundylyq,Quram,Post

admin.site.register(Articles)
admin.site.register(Quram)
admin.site.register(Qundylyq)
admin.site.register(Post)
admin.site.register(Logs)

