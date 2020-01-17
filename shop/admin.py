from django.contrib import admin
from .models import Item # 현재 디렉토리의 models에서 Item import 한다고

admin.site.register(Item)
list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
list_display_links = ['name']
list_filter = ['is_publish']
search_fields = ['name', 'updated_at']
def short_desc(self, item):
    return item.desc[:20]


