import django_tables2 as tables
from .models import Item  # 目次4で定義したモデル

class ItemTable(tables.Table):
    class Meta:
        template_name = 'django_tables2/bootstrap4.html'  # 後ほどbootstrap4で可視化
        fields = ('date','col1','col2','col3','col4',)    # 表示する列column
