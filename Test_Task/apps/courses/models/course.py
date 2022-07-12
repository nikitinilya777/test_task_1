from django.db import models
from django.utils.translation import gettext_lazy as _
from Test_Task import settings


class Course(models.Model):
    name = models.CharField(
        help_text='Название курса.',
        max_length=255,
    )
    description = models.TextField(
        help_text='Описание курса.',
    )
    start_date = models.DateTimeField(
        help_text='Дата начала курса.',
    )
    end_date = models.DateTimeField(
        help_text='Дата окончания курса.',
    )

    def __str__(self):
        return self.name


class CourseMember(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='courses',
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        verbose_name=_('Course'),
        related_name='users',
    )

    def __str__(self):
        return _('%s -> %s') % (self.user, self.course)

    class Meta:
        unique_together = (
            ('user', 'course'),
        )
