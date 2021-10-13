from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify
from admissions.models import Student, Teacher
from .utils import grade_score
from core.models import StudentClass, AcademicSession, AcademicTerm
# Create your models here.
    
class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    hod = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

class ExamBank(models.Model):
    name = models.CharField(max_length=254)
    examination_date = models.DateTimeField()
    class_level = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    class Meta:
        ordering = ['subject']

    def __str__(self):
        return f"{self.student} {self.session} {self.term} {self.subject}"

    def total_score(self):
        return self.test_score + self.exam_score

    def grade(self):
        return grade_score(self.total_score())

    