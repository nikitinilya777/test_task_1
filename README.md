

      for course in Course.objects.all():
        print(course.start_date - timezone.now() - timedelta(hours=1))
        if timedelta(milliseconds=0) <= course.start_date - timezone.now() - timedelta(hours=1) <= timedelta(milliseconds=2):
          emails = list()
          for member in CourseMember.objects.filter(course=course):
            emails += [member.user.email]

          scheduled_time = timezone.now() + timedelta(seconds=2)
          message = f'Через час начнётся курс {course.name}!'
          subject = 'Напоминаниею'
          mail.send(
            emails,
            'ilya@ilya.com',
            subject=subject,
            message=message,
            scheduled_time=scheduled_time,
          )
