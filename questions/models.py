from django.db import models


class Question(models.Model):
    EXAM_CHOICES = [('A', 'Exam A'), ('B', 'Exam B'),
                    ('C', 'Exam C'), ('D', 'Exam D'), ('E', 'Exam A – Appendix')]

    certification = models.CharField(max_length=20, default='ctfl')
    text = models.TextField()
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    exam = models.CharField(max_length=1, choices=EXAM_CHOICES, default='A')
    correct_option = models.CharField(
        max_length=10, blank=True)  # e.g. "c" or "b,c"

    class Meta:
        ordering = ['certification', 'exam', 'order']

    def __str__(self):
        return f'[{self.exam}] {self.text[:80]}'


class ExamStructure(models.Model):
    certification = models.CharField(max_length=20)
    version = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=200)
    num_questions = models.PositiveIntegerField()
    total_points = models.PositiveIntegerField()
    passing_score = models.PositiveIntegerField()
    minutes = models.PositiveIntegerField()
    minutes_extended = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['certification', 'order']

    def __str__(self):
        return f'{self.certification} {self.version}'.strip()
