from django.contrib import admin

from .models import AuthLibrary, CodeSnippet, Comment, DownVote, UpVote

# Register your models here.

admin.site.register(CodeSnippet)
admin.site.register(AuthLibrary)
admin.site.register(Comment)
admin.site.register(DownVote)
admin.site.register(UpVote)
