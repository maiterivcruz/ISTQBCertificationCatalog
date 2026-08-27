from django.db import models


class Question(models.Model):
    EXAM_CHOICES = [('A', 'Exam A'), ('B', 'Exam B'),
                    ('C', 'Exam C'), ('D', 'Exam D'), ('E', 'Exam A – Appendix')]

    text = models.TextField()
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    exam = models.CharField(max_length=1, choices=EXAM_CHOICES, default='A')
    correct_option = models.CharField(
        max_length=10, blank=True)  # e.g. "c" or "b,c"

    class Meta:
        ordering = ['exam', 'order']

    def __str__(self):
        return f'[{self.exam}] {self.text[:80]}'
