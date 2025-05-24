from django.db import models

class Question(models.Model):
    key = models.CharField(max_length=50, unique=True)   # 題目代號（例如 "sweet_1"）
    text = models.CharField(max_length=300)              # 題目文字
    tag = models.CharField(max_length=50)                # 這題對應的偏好標籤（例如 "甜分派"）

    def __str__(self):
        # 在 admin 顯示的名稱
        return f"[{self.key}] {self.text[:30]}…"
