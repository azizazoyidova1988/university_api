from contextlib import closing
from django.db import connection
from collections import OrderedDict


def get_faculty(faculty_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from faculty where id=%s""", [faculty_id])
        faculty = dict_fetchone(cursor)
        return faculty


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from faculty """)
        faculties = dict_fetchall(cursor)
        return faculties


def get_subject(subject_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select subject.*,faculty.id as faculty_id, faculty.name as faculty_name 
        from subject left JOIN faculty 
        ON subject.faculty_id=faculty.id where subject.id=%s""", [subject_id])
        subject = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', subject['id']),
                ('name', subject['name']),
                ('faculty', OrderedDict(
                    [
                        ('id', subject['faculty_id']),
                        ('name', subject['faculty_name']),
                    ]
                ))
            ]
        )


def get_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select subject.*,faculty.id as faculty_id, faculty.name as faculty_name 
        from subject left JOIN faculty 
        ON subject.faculty_id=faculty.id """)
        subjects = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', subject['id']),
                ('name', subject['name']),
                ('faculty', OrderedDict(
                    [
                        ('id', subject['faculty_id']),
                        ('name', subject['faculty_name']),
                    ]
                ))
            ]
        ) for subject in subjects]


def get_group(group_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select fac_group.*,faculty.id as faculty_id, faculty.name as faculty_name 
        from fac_group left JOIN faculty 
        ON fac_group.faculty_id=faculty.id where fac_group.id=%s""", [group_id])
        group = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', group['id']),
                ('name', group['name']),
                ('description', group['description']),
                ('faculty', OrderedDict(
                    [
                        ('id', group['faculty_id']),
                        ('name', group['faculty_name']),
                    ]
                ))
            ]
        )


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select fac_group.*,faculty.id as faculty_id, faculty.name as faculty_name 
        from fac_group left JOIN faculty 
        ON fac_group.faculty_id=faculty.id """)
        groups = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', group['id']),
                ('name', group['name']),
                ('description', group['description']),
                ('faculty', OrderedDict(
                    [
                        ('id', group['faculty_id']),
                        ('name', group['faculty_name']),
                    ]
                ))
            ]
        ) for group in groups]


def get_student(student_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select student.*,faculty.id as faculty_id, faculty.name as faculty_name,
        subject.id as subject_id, subject.name as subject_name,fac_group.id as group_id, 
        fac_group.name as group_name from student left JOIN faculty ON student.faculty_id=faculty.id 
        left join subject on student.subject_id = subject.id 
        left join fac_group on student.group_id=fac_group.id where student.id=%s""", [student_id])
        student = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', student['id']),
                ('first_name', student['first_name']),
                ('last_name', student['last_name']),
                ('description', student['description']),
                ('faculty', OrderedDict(
                    [
                        ('id', student['faculty_id']),
                        ('name', student['faculty_name']),
                    ]
                )),
                ('subject', OrderedDict(
                    [
                        ('id', student['subject_id']),
                        ('name', student['subject_name']),
                    ]
                )),
                ('group', OrderedDict(
                    [
                        ('id', student['group_id']),
                        ('name', student['group_name']),
                    ]
                )),
            ]
        )


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select student.*,faculty.id as faculty_id, faculty.name as faculty_name,
           subject.id as subject_id, subject.name as subject_name,fac_group.id as group_id, 
           fac_group.name as group_name from student left JOIN faculty ON student.faculty_id=faculty.id 
           left join subject on student.subject_id = subject.id 
           left join fac_group on student.group_id=fac_group.id """)
        students = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', student['id']),
                ('first_name', student['first_name']),
                ('last_name', student['last_name']),
                ('description', student['description']),
                ('faculty', OrderedDict(
                    [
                        ('id', student['faculty_id']),
                        ('name', student['faculty_name']),
                    ]
                )),
                ('subject', OrderedDict(
                    [
                        ('id', student['subject_id']),
                        ('name', student['subject_name']),
                    ]
                )),
                ('group', OrderedDict(
                    [
                        ('id', student['group_id']),
                        ('name', student['group_name']),
                    ]
                )),
            ]
        ) for student in students]


def get_teacher(teacher_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select teacher.*,faculty.id as faculty_id, faculty.name as faculty_name,
        subject.id as subject_id, subject.name as subject_name,fac_group.id as group_id, 
        fac_group.name as group_name from teacher left JOIN faculty ON teacher.faculty_id=faculty.id 
        left join subject on teacher.subject_id = subject.id 
        left join fac_group on teacher.group_id=fac_group.id where teacher.id=%s""", [teacher_id])
        teacher = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', teacher['id']),
                ('first_name', teacher['first_name']),
                ('last_name', teacher['last_name']),
                ('description', teacher['description']),
                ('faculty', OrderedDict(
                    [
                        ('id', teacher['faculty_id']),
                        ('name', teacher['faculty_name']),
                    ]
                )),
                ('subject', OrderedDict(
                    [
                        ('id', teacher['subject_id']),
                        ('name', teacher['subject_name']),
                    ]
                )),
                ('group', OrderedDict(
                    [
                        ('id', teacher['group_id']),
                        ('name', teacher['group_name']),
                    ]
                )),
            ]
        )


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select teacher.*,faculty.id as faculty_id, faculty.name as faculty_name,
        subject.id as subject_id, subject.name as subject_name,fac_group.id as group_id, 
        fac_group.name as group_name from teacher left JOIN faculty ON teacher.faculty_id=faculty.id 
        left join subject on teacher.subject_id = subject.id 
        left join fac_group on teacher.group_id=fac_group.id """)
        teachers = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', teacher['id']),
                ('first_name', teacher['first_name']),
                ('last_name', teacher['last_name']),
                ('description', teacher['description']),
                ('faculty', OrderedDict(
                    [
                        ('id', teacher['faculty_id']),
                        ('name', teacher['faculty_name']),
                    ]
                )),
                ('subject', OrderedDict(
                    [
                        ('id', teacher['subject_id']),
                        ('name', teacher['subject_name']),
                    ]
                )),
                ('group', OrderedDict(
                    [
                        ('id', teacher['group_id']),
                        ('name', teacher['group_name']),
                    ]
                )),
            ]
        ) for teacher in teachers]


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
