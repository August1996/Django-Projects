from django.contrib import admin
from blog.models import User,Article,Tag,Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	class Media:
		js = (
			'/static/js/kindeditor/kindeditor.js',
			'/static/js/kindeditor/lang/zh_CN.js',
			'/static/js/kindeditor/config.js',
			)


admin.site.register(User)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)

