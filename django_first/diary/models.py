from django.db import models


class Diary(models.Model):


    class Meta:
        db_table = 'diary'


    title = models.CharField(max_length=100) # タイトル
    content = models.TextField(max_length=1000) # 内容
    create_at = models.DateField(auto_now_add=True) # 作成日時


    def __str__(self):
        return self.title