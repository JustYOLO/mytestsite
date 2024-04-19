from django.db import models

class Todo(models.Model):
    # todo에 대한 데이터
    
    # 제목
    title = models.CharField(max_length=100)
    # 완료 되었는지 확인하는 bool
    completed = models.BooleanField(default=False)
    # 생성 날짜를 저장
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
