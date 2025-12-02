from django.db import models
from django.conf import settings

class StockData(models.Model):
    company_name = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=20)
    comments = models.TextField()  # 댓글을 텍스트로 저장
    analysis = models.TextField()  # ChatGPT 분석 결과
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    
class UserInterestStock(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'stock_name'], name='unique_user_stock')
        ]