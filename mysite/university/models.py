from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=124, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "faculty"

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=124, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "subject"

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=124, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "fac_group"

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=124, blank=False, null=False)
    last_name = models.CharField(max_length=124, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, blank=False, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, blank=False, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=False, null=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.first_name



class Teacher(models.Model):
    first_name = models.CharField(max_length=124, blank=False, null=False)
    last_name = models.CharField(max_length=124, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, blank=False, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, blank=False, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=False, null=True)

    class Meta:
        db_table = "teacher"

    def __str__(self):
        return self.first_name



