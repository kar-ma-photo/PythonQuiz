from django.db import models


# Create your models here.
class PythonQuesModel(models.Model):
    question = models.CharField('Вопрос', max_length=200, null=True)
    op1 = models.CharField('Вариснт 1', max_length=200, null=True)
    op2 = models.CharField('Вариснт 2',max_length=200, null=True)
    op3 = models.CharField('Вариснт 3',max_length=200, null=True)
    ans = models.CharField('Ответ',max_length=200, null=True)

    def __str__(self):
        return self.question