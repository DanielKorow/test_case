from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    relevant = models.BooleanField(default=False)


class Question(models.Model):

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question
    
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField()
    relevant = models.BooleanField(default=True)

class SurveysDone(models.Model):

    class Meta:
        verbose_name = "SurveysDone"
        verbose_name_plural = "SurveyDones"

    def __str__(self):
        return self.survey.name
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Answer(models.Model):

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.answer

    survey_done = models.ForeignKey(SurveysDone, on_delete=models.CASCADE)    
    # survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    date_of_survay = models.DateTimeField(auto_now_add=True)

class Option(models.Model):

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"

    def __str__(self):
        return self.option
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField()
