from django.contrib import admin
from comicms.models import Comic
from filetransfers.admin import FiletransferAdmin

class ComicAdmin(FiletransferAdmin):
    pass
admin.site.register(Comic, ComicAdmin)
