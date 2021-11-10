from django.shortcuts import render
from .models import Student, Subject, Group, Teacher, Faculty
from .serializers import GroupSerializer, FacultySerializer, \
    StudentSerializer, SubjectSerializer, TeacherSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from . import services
from rest_framework.exceptions import NotFound


"""Faculty"""

class FacultyView(GenericAPIView):
    serializer_class = FacultySerializer

    def get_object(self, *args, **kwargs):
        try:
            faculty = Faculty.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return faculty

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        faculty = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=faculty)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        faculty = self.get_object(pk=pk)
        faculty.delete()
        return Response({"detail": f"Faculty with pk= {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            faculty = services.get_faculty(faculty_id=pk)
            if not faculty:
                raise NotFound("Faculty not found!")
            return Response(faculty, status=status.HTTP_200_OK)
        else:
            faculties = services.get_faculties()
            return Response(faculties, status=status.HTTP_200_OK)


""" Subject"""

class SubjectView(GenericAPIView):
    serializer_class = SubjectSerializer

    def get_object(self, *args, **kwargs):
        try:
            subject = Subject.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return subject

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subject = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=subject)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        subject = self.get_object(pk=pk)
        subject.delete()
        return Response({"detail": f"Subject with pk= {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            subject = services.get_subject(subject_id=pk)
            if not subject:
                raise NotFound("Subject not found!")
            return Response(subject, status=status.HTTP_200_OK)
        else:
            subjects = services.get_subjects()
            return Response(subjects, status=status.HTTP_200_OK)


""" Group"""

class GroupView(GenericAPIView):
    serializer_class = GroupSerializer

    def get_object(self, *args, **kwargs):
        try:
            group = Group.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return group

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        group = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=group)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        group = self.get_object(pk=pk)
        group.delete()
        return Response({"detail": f"Group with pk= {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            group = services.get_group(group_id=pk)
            if not group:
                raise NotFound("Subject not found!")
            return Response(group, status=status.HTTP_200_OK)
        else:
            groups = services.get_groups()
            return Response(groups, status=status.HTTP_200_OK)



""" Student"""

class StudentView(GenericAPIView):
    serializer_class = StudentSerializer

    def get_object(self, *args, **kwargs):
        try:
            student = Student.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return student

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=student)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = self.get_object(pk=pk)
        student.delete()
        return Response({"detail": f"Student with pk= {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            student = services.get_student(student_id=pk)
            if not student:
                raise NotFound("Student not found!")
            return Response(student, status=status.HTTP_200_OK)
        else:
            students = services.get_students()
            return Response(students, status=status.HTTP_200_OK)



""" Teacher"""

class TeacherView(GenericAPIView):
    serializer_class = TeacherSerializer

    def get_object(self, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return teacher

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        teacher = self.get_object(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=teacher)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        teacher = self.get_object(pk=pk)
        teacher.delete()
        return Response({"detail": f"Teacher with pk= {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            teacher = services.get_teacher(teacher_id=pk)
            if not teacher:
                raise NotFound("Teacher not found!")
            return Response(teacher, status=status.HTTP_200_OK)
        else:
            teachers = services.get_teachers()
            return Response(teachers, status=status.HTTP_200_OK)