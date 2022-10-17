from django.contrib import admin
from  .models import Blog
from django.utils.html import format_html
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('title','content','image',)
    exclude= ('is_deleted',)
    list_display= ('title','less_content','image','is_deleted','days_since_created',)
    list_display_links = ('is_deleted',)
    list_filter = ('is_deleted',)
    actions= ('delete_post',)
    def less_content(self,obj):
        return format_html(f'''<div style ="color: yellow ">
            
         {obj.content[:100]}
        <button>
        <a href="/" class="default">
        Click
        </a>
        </button>
         
         </div>''') 
    less_content.short_description = 'Content'
    def delete_post(self,request,queryset):
        queryset.update(is_deleted = True)
        self.message_user(request,'Marked elements are deleted')
    delete_post.short_description = 'Upgrade to deleted'